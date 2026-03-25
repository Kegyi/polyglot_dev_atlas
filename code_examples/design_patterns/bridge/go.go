package main

import "fmt"

type Sender interface {
	Send(message string)
}

type EmailSender struct{}

func (EmailSender) Send(message string) {
	fmt.Println("email:", message)
}

type SMSSender struct{}

func (SMSSender) Send(message string) {
	fmt.Println("sms:", message)
}

type AlertNotification struct {
	sender Sender
}

func (n AlertNotification) Notify(message string) {
	n.sender.Send("alert -> " + message)
}

func main() {
	AlertNotification{sender: EmailSender{}}.Notify("CPU high")
	AlertNotification{sender: SMSSender{}}.Notify("CPU high")
}
