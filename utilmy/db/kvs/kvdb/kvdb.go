package kvdb

import (
	"context"
	"math/rand"
	"net"
	"strings"
	"sync"

	"github.com/No3371/go-skytable"
	"github.com/go-redis/redis/v8"
)

const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_"

var (
	keys map[int][]string = map[int][]string{}
	vals map[int][]string = map[int][]string{}
)

func GenerateRandomString(n int) string {
	sb := strings.Builder{}
	sb.Grow(n)
	for i := 0; i < n; i++ {
		sb.WriteByte(charset[rand.Intn(len(charset))])
	}
	return sb.String()
}

func CreateKeyValForUser(x int, y int) {
	for i := 0; i < x; i++ {
		keys[i] = make([]string, y)
		vals[i] = make([]string, y)
		for j := 0; j < y; j++ {
			keys[i][j] = GenerateRandomString(10)
			vals[i][j] = GenerateRandomString(500)
		}
	}
}

func RunSetXClientsYTimes(x int, y int, port string) {
	var wg sync.WaitGroup
	CreateKeyValForUser(x, y)

	for i := 0; i < x; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			client := redis.NewClient(&redis.Options{
				Addr:     "localhost:" + port,
				Password: "", // no password set
				DB:       0,  // use default DB
			})

			ctx := context.Background()
			for j := 0; j < y; j++ {
				err := client.Set(ctx, keys[i][j], vals[i][j], 0).Err()
				if err != nil {
					panic(err)
				}
			}
		}(i)
	}
	wg.Wait()
}

func RunGetXClientsYTimes(x int, y int, port string) {
	var wg sync.WaitGroup

	for i := 0; i < x; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			client := redis.NewClient(&redis.Options{
				Addr:     "localhost:" + port,
				Password: "", // no password set
				DB:       0,  // use default DB
			})

			ctx := context.Background()

			for j := 0; j < y; j++ {
				res := client.Get(ctx, keys[i][j])
				if res.Val() != vals[i][j] {
					panic(res)
				}
			}
		}(i)
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
