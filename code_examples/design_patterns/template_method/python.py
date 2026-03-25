from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process(self) -> None:
        self.read_data()
        self.parse_data()
        self.write_data()
    
    @abstractmethod
    def read_data(self) -> None:
        pass
    
    @abstractmethod
    def parse_data(self) -> None:
        pass
    
    @abstractmethod
    def write_data(self) -> None:
        pass

class CSVProcessor(DataProcessor):
    def read_data(self) -> None:
        print("Reading CSV data")
    
    def parse_data(self) -> None:
        print("Parsing CSV")
    
    def write_data(self) -> None:
        print("Writing processed CSV")

class JSONProcessor(DataProcessor):
    def read_data(self) -> None:
        print("Reading JSON data")
    
    def parse_data(self) -> None:
        print("Parsing JSON")
    
    def write_data(self) -> None:
        print("Writing processed JSON")

csv = CSVProcessor()
csv.process()

json = JSONProcessor()
json.process()
