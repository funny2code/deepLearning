package kvdb_test

import (
	"testing"

	"github.com/arita37/myutil/utilmy/db/kvs/kvdb"
)

var x = 100
var y = 1000

func BenchmarkSetRedis(b *testing.B) {
	kvdb.RunSetXClientsYTimes(x, y, "6379")
}

func BenchmarkGetRedis(b *testing.B) {
	kvdb.RunGetXClientsYTimes(x, y, "6379")
}

func BenchmarkSetKeydDb(b *testing.B) {
	kvdb.RunSetXClientsYTimes(x, y, "6380")
}

func BenchmarkGetKeyDb(b *testing.B) {
	kvdb.RunGetXClientsYTimes(x, y, "6380")
}

func BenchmarkSetDragonfly(b *testing.B) {
	kvdb.RunSetXClientsYTimes(x, y, "6381")
}

func BenchmarkGetDragonfly(b *testing.B) {
	kvdb.RunGetXClientsYTimes(x, y, "6381")
}

// func BenchmarkSetSkyTable(b *testing.B) {
// 	clientCount := 100
// 	setCount := 10000
// 	kvdb.SkyTableRunSetXClientsYTimes(clientCount, setCount)
// }

// func BenchmarkGetSkyTable(b *testing.B) {
// 	clientCount := 100
// 	getCount := 10000
// 	kvdb.SkyTableRunGetXClientsYTimes(clientCount, getCount)
// }
