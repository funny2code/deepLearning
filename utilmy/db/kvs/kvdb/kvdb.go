package kvdb

import (
	"context"
	"net"
	"sync"

	"github.com/No3371/go-skytable"
	"github.com/go-redis/redis/v8"
)

func RunSetXClientsYTimes(x, y int, port string) {
	var wg sync.WaitGroup

	for i := 0; i < x; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			client := redis.NewClient(&redis.Options{
				Addr:     "localhost:" + port,
				Password: "", // no password set
				DB:       0,  // use default DB
			})

			ctx := context.Background()
			for j := 0; j < y; j++ {
				err := client.Set(ctx, "foo", "bar", 0).Err()
				if err != nil {
					panic(err)
				}
			}
		}()
	}
	wg.Wait()
}

func RunGetXClientsYTimes(x, y int, port string) {
	var wg sync.WaitGroup

	for i := 0; i < x; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			client := redis.NewClient(&redis.Options{
				Addr:     "localhost:" + port,
				Password: "", // no password set
				DB:       0,  // use default DB
			})

			ctx := context.Background()
			err := client.Set(ctx, "foo", "bar", 0).Err()
			if err != nil {
				panic(err)
			}

			for j := 0; j < y; j++ {
				res := client.Get(ctx, "foo")
				if res.Val() != "bar" {
					panic(res)
				}
			}
		}()
	}
	wg.Wait()
}

func SkyTableRunSetXClientsYTimes(x int, y int) {
	var wg sync.WaitGroup

	for i := 0; i < x; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			localAddr := &net.TCPAddr{IP: []byte{172, 17, 0, 1}, Port: 6382}

			client, err := skytable.NewConn(localAddr)
			if err != nil {
				panic(err)
			}

			ctx := context.Background()
			for j := 0; j < y; j++ {
				err := client.Set(ctx, "foo", "bar")
				if err != nil {
					panic(err)
				}
			}
		}()
	}
	wg.Wait()
}

func SkyTableRunGetXClientsYTimes(x int, y int) {
	var wg sync.WaitGroup

	for i := 0; i < x; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			localAddr := &net.TCPAddr{IP: []byte{172, 17, 0, 1}, Port: 6382}

			client, err := skytable.NewConn(localAddr)
			if err != nil {
				panic(err)
			}

			ctx := context.Background()
			err = client.Set(ctx, "foo", "bar")
			if err != nil {
				panic(err)
			}

			for j := 0; j < y; j++ {
				res, _ := client.Get(ctx, "foo")
				if res.Value != "bar" {
					panic(res)
				}
			}
		}()
	}
	wg.Wait()
}
