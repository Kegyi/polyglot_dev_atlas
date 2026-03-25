package main

import "fmt"

type Printer interface {
	Print(message string)
}

type JSONLogger struct{}

func (JSONLogger) WriteJSON(payload string) {
	fmt.Println(payload)
}

type JSONLoggerAdapter struct {
	logger JSONLogger
}

func (a JSONLoggerAdapter) Print(message string) {
	a.logger.WriteJSON(fmt.Sprintf("{\"message\":\"%s\"}", message))
}

func main() {
	printer := JSONLoggerAdapter{logger: JSONLogger{}}
	printer.Print("build finished")
}
