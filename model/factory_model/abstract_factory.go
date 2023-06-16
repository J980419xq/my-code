package main

import "fmt"

type AbstractFactory interface {
	CreateGreeing() IGreeting
	CreatLove() ILove
}
type IGreeting interface {
	Greet(name string) string
}
type ILove interface {
	Love(name string) string
}
type CnFactory struct{}

func (ef *CnFactory) CreateGreeing() IGreeting {
	return &CnGreet{}
}
func (ef *CnFactory) CreatLove() ILove {
	return &CnLove{}
}

type CnGreet struct{}

func (*CnGreet) Greet(name string) string {
	return fmt.Sprintf("你好，%s", name)
}

type CnLove struct{}

func (*CnLove) Love(name string) string {
	return fmt.Sprintf("我爱你，%s", name)
}

type EnFactory struct{}

func (ef *EnFactory) CreateGreeing() IGreeting {
	return &EnGreet{}
}
func (ef *EnFactory) CreatLove() ILove {
	return &EnLove{}
}

type EnGreet struct{}

func (*EnGreet) Greet(name string) string {
	return fmt.Sprintf("Hello, %s", name)
}

type EnLove struct{}

func (*EnLove) Love(name string) string {
	return fmt.Sprintf("I Love You, %s", name)
}
