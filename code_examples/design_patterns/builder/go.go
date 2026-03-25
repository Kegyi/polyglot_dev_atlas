package main

import "fmt"

type Report struct {
	Title    string
	Sections []string
}

type ReportBuilder struct {
	report Report
}

func (b *ReportBuilder) Title(value string) *ReportBuilder {
	b.report.Title = value
	return b
}

func (b *ReportBuilder) Section(value string) *ReportBuilder {
	b.report.Sections = append(b.report.Sections, value)
	return b
}

func (b *ReportBuilder) Build() Report {
	return b.report
}

func main() {
	report := (&ReportBuilder{}).
		Title("Daily Build").
		Section("tests: green").
		Section("deploy: staged").
		Build()

	fmt.Println(report.Title)
	for _, section := range report.Sections {
		fmt.Println("-", section)
	}
}
