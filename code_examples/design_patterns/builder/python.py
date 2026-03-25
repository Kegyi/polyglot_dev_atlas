from dataclasses import dataclass, field


@dataclass
class Report:
    title: str = ""
    sections: list[str] = field(default_factory=list)


class ReportBuilder:
    def __init__(self) -> None:
        self._report = Report()

    def title(self, value: str) -> "ReportBuilder":
        self._report.title = value
        return self

    def section(self, value: str) -> "ReportBuilder":
        self._report.sections.append(value)
        return self

    def build(self) -> Report:
        return self._report


report = (
    ReportBuilder()
    .title("Daily Build")
    .section("tests: green")
    .section("deploy: staged")
    .build()
)

print(report.title)
for section in report.sections:
    print(f"- {section}")