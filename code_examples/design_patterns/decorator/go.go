package main

import "fmt"

type Notifier interface {
	Send(message string)
}

type EmailNotifier struct{}

func (EmailNotifier) Send(message string) {
	fmt.Println("email:", message)
}

type SMSDecorator struct {
	inner Notifier
}

func (d SMSDecorator) Send(message string) {
	d.inner.Send(message)
	fmt.Println("sms:", message)
}

func main() {
	notifier := SMSDecorator{inner: EmailNotifier{}}
	notifier.Send("deployment done")
}
