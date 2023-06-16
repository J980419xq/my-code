package main

import "math/rand"

type hungry struct {
	a int
}

var b *hungry

func init() {
	b = &hungry{a: rand.Int()}
}

func GetInstance() *hungry {
	return b
}
