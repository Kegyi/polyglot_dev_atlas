package main

import (
	"encoding/json"
	"fmt"
)

type User struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {
	user := User{Name: "Alice", Age: 29}
	data, err := json.Marshal(user)
	if err != nil {
		panic(err)
	}

	var parsed User
	if err := json.Unmarshal(data, &parsed); err != nil {
		panic(err)
	}

	fmt.Println("json:", string(data))
	fmt.Println("parsed name:", parsed.Name)
}
