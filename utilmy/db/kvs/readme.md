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

|name           |time    |
|---            |---     |
|SetRedis       |5.98s   |
|GetRedis       |5.96s   |
|SetKeydDb      |4.95s   |
|GetKeyDb       |5.07s   |
|SetDragonfly   |5.47s   |
|GetDragonfly   |5.57s   |

### example2
- cpu: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- 20 clients
- 10.000 operations / client
- 10 length of key and 500 length of value

|name           |time    |
|---            |---     |
|SetRedis       |1.57s   |
|GetRedis       |1.75s   |
|SetKeydDb      |1.82s   |
|GetKeyDb       |2.16s   |
|SetDragonfly   |1.83s   |
|GetDragonfly   |1.79s   |
