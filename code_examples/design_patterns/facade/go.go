package main

import "fmt"

type Compiler struct{}

func (Compiler) Run() { fmt.Println("compile") }

type TestRunner struct{}

func (TestRunner) Run() { fmt.Println("test") }

type Packager struct{}

func (Packager) Run() { fmt.Println("package") }

type ReleaseFacade struct {
	compiler Compiler
	tests    TestRunner
	packager Packager
}

func (f ReleaseFacade) Deploy() {
	f.compiler.Run()
	f.tests.Run()
	f.packager.Run()
}

func main() {
	ReleaseFacade{}.Deploy()
}
