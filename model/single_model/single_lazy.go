package main

import (
	"sync"
	"sync/atomic"
)

var initialized uint32

type lazy struct {
	a int
}

var instance *lazy

func GetLazyInstance() *lazy {
	if atomic.LoadUint32(&initialized) == 1 {
		return instance
	}
	var mu sync.Mutex
	mu.Lock()
	defer mu.Unlock()
	if initialized == 0 {
		instance = &lazy{a: 0}
		atomic.StoreUint32(&initialized, 1)
	}
	return instance
}
