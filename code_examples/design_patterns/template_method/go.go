package main

import "fmt"

type DataProcessor interface {
	ReadData()
	ParseData()
	WriteData()
	Process()
}

type BaseProcessor struct {
	processor DataProcessor
}

func (b *BaseProcessor) Process() {
	b.processor.ReadData()
	b.processor.ParseData()
	b.processor.WriteData()
}

type CSVProcessor struct {
	BaseProcessor
}

func (c *CSVProcessor) ReadData() {
	fmt.Println("Reading CSV data")
}

func (c *CSVProcessor) ParseData() {
	fmt.Println("Parsing CSV")
}

func (c *CSVProcessor) WriteData() {
	fmt.Println("Writing processed CSV")
}

type JSONProcessor struct {
	BaseProcessor
}

func (j *JSONProcessor) ReadData() {
	fmt.Println("Reading JSON data")
}

func (j *JSONProcessor) ParseData() {
	fmt.Println("Parsing JSON")
}

func (j *JSONProcessor) WriteData() {
	fmt.Println("Writing processed JSON")
}

func main() {
	csv := &CSVProcessor{}
	csv.processor = csv
	csv.Process()

	json := &JSONProcessor{}
	json.processor = json
	json.Process()
}
