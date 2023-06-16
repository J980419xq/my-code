package main

import "sync"

type singleton struct {
}

var i *singleton
var o sync.Once

func GetSecondInstance() *singleton {
	o.Do(func() {
		i = &singleton{}
	})
	return i
}
