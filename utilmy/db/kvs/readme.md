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
|SetRedis             |88.7s   |
|GetRedis             |6.67s   |
|SetKeydDb            |88.6s   |
|GetKeyDb             |5.41s   |
|SetDragonfly         |88.3s   |
|GetDragonfly         |5.63s   |

### example2
- cpu: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- 20 clients
- 10.000 operations / client
- 10 length of key and 500 length of value

|name                   |time    |
|---                    |---     |
|SetRedis               |9.82s   |
|GetRedis               |1.37s   |
|SetKeydDb              |11.2s   |
|GetKeyDb               |1.57s   |
|SetDragonfly           |9.80s   |
|GetDragonfly           |1.61s   |
