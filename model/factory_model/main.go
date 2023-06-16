package main

import "fmt"

func main() {
	printer1 := NewPrinter("en")
	fmt.Println(printer1.Print("jxq"))
	printer2 := NewPrinter("cn")
	fmt.Println(printer2.Print("俞月荷"))
	/* var factory PrinterFactory
	var printer Printer
	factory = &EnPrinterFactory{}
	printer = factory.Create()
	fmt.Println(printer.Print("jxq"))
	factory = &CnPrinterFactory{}
	fmt.Println(printer.Print("俞月荷")) */
	var factory AbstractFactory
	var greet IGreeting
	var love ILove
	factory = &EnFactory{}
	greet = factory.CreateGreeing()
	love = factory.CreatLove()
	fmt.Println(greet.Greet("Yyh"))
	fmt.Println(love.Love("Yyh"))

	factory = &CnFactory{}
	greet = factory.CreateGreeing()
	love = factory.CreatLove()
	fmt.Println(greet.Greet("俞月荷"))
	fmt.Println(love.Love("俞月荷"))
}
