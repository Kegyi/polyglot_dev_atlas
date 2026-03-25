package main

import "fmt"

type Button interface{ Render() string }
type Dialog interface{ Render() string }

type WidgetFactory interface {
	CreateButton() Button
	CreateDialog() Dialog
}

type LightButton struct{}

func (LightButton) Render() string { return "light button" }

type LightDialog struct{}

func (LightDialog) Render() string { return "light dialog" }

type DarkButton struct{}

func (DarkButton) Render() string { return "dark button" }

type DarkDialog struct{}

func (DarkDialog) Render() string { return "dark dialog" }

type LightFactory struct{}

func (LightFactory) CreateButton() Button { return LightButton{} }
func (LightFactory) CreateDialog() Dialog { return LightDialog{} }

type DarkFactory struct{}

func (DarkFactory) CreateButton() Button { return DarkButton{} }
func (DarkFactory) CreateDialog() Dialog { return DarkDialog{} }

func showScreen(factory WidgetFactory) {
	button := factory.CreateButton()
	dialog := factory.CreateDialog()
	fmt.Printf("%s + %s\n", button.Render(), dialog.Render())
}

func main() {
	showScreen(LightFactory{})
	showScreen(DarkFactory{})
}
