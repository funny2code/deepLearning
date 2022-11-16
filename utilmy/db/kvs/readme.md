## Running the tests
```bash
    docker compose up -d
    go mod download
    go test ./... -bench=. -cpu 4
```