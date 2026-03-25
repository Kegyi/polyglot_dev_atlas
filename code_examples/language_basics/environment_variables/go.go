package main

import (
	"fmt"
	"os"
)

func main() {
	mode, hasMode := os.LookupEnv("APP_MODE")
	if !hasMode {
		mode = "development"
	}

	port, hasPort := os.LookupEnv("APP_PORT")
	if !hasPort {
		port = "8080"
	}

	fmt.Println("mode:", mode)
	fmt.Println("port:", port)
	fmt.Println("has APP_MODE:", hasMode)
}
