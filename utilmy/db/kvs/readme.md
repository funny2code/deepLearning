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
|SetRedis             |14.9s   |
|GetRedis             |6.61s   |
|SetKeydDb            |15.3s   |
|GetKeyDb             |5.03s   |
|SetDragonfly         |13.4s   |
|GetDragonfly         |5.37s   |

### example2
- cpu: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- 20 clients
- 10.000 operations / client
- 10 length of key and 500 length of value

|name                   |time    |
|---                    |---     |
|SetRedis               |88.7s   |
|GetRedis               |6.67s   |
|SetKeydDb              |88.6s   |
|GetKeyDb               |5.41s   |
|SetDragonfly           |88.3s   |
|GetDragonfly           |5.63s   |

