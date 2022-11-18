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

var keyVal map[string]string

func initKeyVal(n int) {
	keyVal = make(map[string]string)
	for i := 0; i < n; i++ {
		keyVal[GenerateRandomString(10)] = GenerateRandomString(100)
	}
}

func GenerateRandomString(n int) string {
	sb := strings.Builder{}
	sb.Grow(n)
	for i := 0; i < n; i++ {
		sb.WriteByte(charset[rand.Intn(len(charset))])
	}
	return sb.String()
}

func RunSetXClientsYTimes(x int, y int, port string) {
	var wg sync.WaitGroup
	initKeyVal(y)

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
			for key, value := range keyVal {
				err := client.Set(ctx, key, value, 0).Err()
				if err != nil {
					panic(err)
				}
			}
		}()
	}
	wg.Wait()
}

func RunGetXClientsYTimes(x int, y int, port string) {
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

			for key, val := range keyVal {
				res := client.Get(ctx, key)
				if res.Val() != val {
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
