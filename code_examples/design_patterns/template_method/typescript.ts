abstract class DataProcessor {
    process(): void {
        this.readData();
        this.parseData();
        this.writeData();
    }
    
    protected abstract readData(): void;
    protected abstract parseData(): void;
    protected abstract writeData(): void;
}

class CSVProcessor extends DataProcessor {
    protected readData(): void {
        console.log("Reading CSV data");
    }
    
    protected parseData(): void {
        console.log("Parsing CSV");
    }
    
    protected writeData(): void {
        console.log("Writing processed CSV");
    }
}

class JSONProcessor extends DataProcessor {
    protected readData(): void {
        console.log("Reading JSON data");
    }
    
    protected parseData(): void {
        console.log("Parsing JSON");
    }
    
    protected writeData(): void {
        console.log("Writing processed JSON");
    }
}

const csv = new CSVProcessor();
csv.process();

const json = new JSONProcessor();
json.process();
