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
|SetRedis             |6.96s   |
|SetAndGetRedis       |15.9s   |
|SetKeydDb            |6.58s   |
|SetAndGetKeyDb       |16.4s   |
|SetDragonfly         |6.34s   |
|SetAndGetDragonfly   |17.7s   |


### example2
- cpu: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- 20 clients
- 10.000 operations / client
- 10 length of key and 500 length of value
|name                   |time    |
|---                    |---     |
|SetRedis               |1.52s   |
|SetAndGetRedis         |3.35s   |
|SetKeydDb              |1.58s   |
|SetAndGetKeyDb         |3.55s   |
|SetDragonfly           |1.80s   |
|SetAndGetDragonfly     |4.02s   |
