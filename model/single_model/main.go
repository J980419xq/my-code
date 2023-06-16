// 一个类型只有一个实例时，并提供一个全局的访问点
// 配置管理器 日志记录器 数据库连接池 线程池 状态管理器
package main

import "fmt"

func main() {
	s1 := GetInstance()
	fmt.Printf("%p\n", s1)
	s3 := GetSecondInstance()
	fmt.Println(s3)
	s2 := GetLazyInstance()
	fmt.Println(s2.a)
	s4 := GetInstance()
	fmt.Printf("%p\n", s4)
}
