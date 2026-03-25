from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def parse(self) -> str: ...


class JsonParser(Parser):
    def parse(self) -> str:
        return "parsed json"


class CsvParser(Parser):
    def parse(self) -> str:
        return "parsed csv"


class ImportJob(ABC):
    def run(self) -> str:
        return self.create_parser().parse()

    @abstractmethod
    def create_parser(self) -> Parser: ...


class JsonImportJob(ImportJob):
    def create_parser(self) -> Parser:
        return JsonParser()


class CsvImportJob(ImportJob):
    def create_parser(self) -> Parser:
        return CsvParser()


for job in (JsonImportJob(), CsvImportJob()):
    print(job.run())