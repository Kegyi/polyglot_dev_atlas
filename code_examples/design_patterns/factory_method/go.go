package main

import "fmt"

type Parser interface{ Parse() string }

type JSONParser struct{}

func (JSONParser) Parse() string { return "parsed json" }

type CSVParser struct{}

func (CSVParser) Parse() string { return "parsed csv" }

type ImportJob interface {
	Run() string
	createParser() Parser
}

type JSONImportJob struct{}

func (JSONImportJob) createParser() Parser { return JSONParser{} }
func (j JSONImportJob) Run() string        { return j.createParser().Parse() }

type CSVImportJob struct{}

func (CSVImportJob) createParser() Parser { return CSVParser{} }
func (j CSVImportJob) Run() string        { return j.createParser().Parse() }

func main() {
	jobs := []ImportJob{JSONImportJob{}, CSVImportJob{}}
	for _, job := range jobs {
		fmt.Println(job.Run())
	}
}
