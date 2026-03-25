type Report = {
  title: string;
  sections: string[];
};

class ReportBuilder {
  private report: Report = { title: '', sections: [] };

  title(value: string): this {
    this.report.title = value;
    return this;
  }

  section(value: string): this {
    this.report.sections.push(value);
    return this;
  }

  build(): Report {
    return this.report;
  }
}

const report = new ReportBuilder()
  .title('Daily Build')
  .section('tests: green')
  .section('deploy: staged')
  .build();

console.log(report.title);
for (const section of report.sections) {
  console.log(`- ${section}`);
}