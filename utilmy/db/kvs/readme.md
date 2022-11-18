## Running the tests
```bash
    docker compose up -d
    go mod download
    go install  golang.org/x/perf/cmd/benchstat
    go test ./... -bench=. -cpu 4 >/tmp/out
    benchstat /tmp/out
```

## example output
### example1
- cpu: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- 100 clients
- 10.000 operations / client
- 10 length of key and 500 length of value

|name                 |time    |
|---                  |---     |
|SetRedis             |6.05s   |
|GetRedis             |5.90s   |
|SetKeydDb            |7.26s   |
|GetKeyDb             |4.66s   |
|SetDragonfly         |5.13s   |
|GetDragonfly         |5.13s   |


### example2
- cpu: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- 20 clients
- 10.000 operations / client
- 10 length of key and 500 length of value

|name                   |time    |
|---                    |---     |
|SetRedis               |1.28s   |
|GetRedis               |1.25s   |
|SetKeydDb              |1.36s   |
|GetKeyDb               |1.31s   |
|SetDragonfly           |1.47s   |
|GetDragonfly           |1.49s   |
