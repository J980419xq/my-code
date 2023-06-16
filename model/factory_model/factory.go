package main

import "fmt"

// 产品接口
type Printer interface {
	Print(name string) string
}

// 产品基类，封装公共方法和属性
type BasePrinter struct {
}

// 具体产品
type CnPrinter struct {
	*BasePrinter
}
type EnPrinter struct {
	*BasePrinter
}

func (*CnPrinter) Print(name string) string {
	return fmt.Sprintf("你好，%s", name)
}

func (*EnPrinter) Print(name string) string {
	return fmt.Sprintf("Hello, %s", name)
}
