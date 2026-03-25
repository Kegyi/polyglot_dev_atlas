package main

import (
	"fmt"
	"sync"
)

type Config struct {
	Env string
}

var (
	once   sync.Once
	shared *Config
)

func Instance() *Config {
	once.Do(func() {
		shared = &Config{Env: "dev"}
	})
	return shared
}

func main() {
	Instance().Env = "prod"
	fmt.Println(Instance().Env)
}
