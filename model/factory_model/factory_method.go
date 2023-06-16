package main

// 抽象工厂
type PrinterFactory interface {
	Create() Printer
}

// 具体工厂
type CnPrinterFactory struct{}

func (cf *CnPrinterFactory) Create() Printer {
	return &CnPrinter{
		BasePrinter: &BasePrinter{},
	}
}

//具体工厂
type EnPrinterFactory struct{}

func (ef *EnPrinterFactory) Create() Printer {
	return &EnPrinter{
		BasePrinter: &BasePrinter{},
	}
}
