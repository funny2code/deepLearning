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
|SetRedis             |6.31s   |
|GetRedis             |6.11s   |
|SetKeydDb            |4.88s   |
|GetKeyDb             |4.98s   |
|SetDragonfly         |5.29s   |
|GetDragonfly         |5.30s   |

### example2
- cpu: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- 20 clients
- 10.000 operations / client
- 10 length of key and 500 length of value

|name                   |time    |
|---                    |---     |
|SetRedis               |1.35s   |
|GetRedis               |1.32s   |
|SetKeydDb              |1.43s   |
|GetKeyDb               |1.36s   |
|SetDragonfly           |1.54s   |
|GetDragonfly           |1.49s   |