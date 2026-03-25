interface Parser {
  parse(): string;
}

class JsonParser implements Parser {
  parse(): string {
    return 'parsed json';
  }
}

class CsvParser implements Parser {
  parse(): string {
    return 'parsed csv';
  }
}

abstract class ImportJob {
  run(): string {
    return this.createParser().parse();
  }

  protected abstract createParser(): Parser;
}

class JsonImportJob extends ImportJob {
  protected createParser(): Parser {
    return new JsonParser();
  }
}

class CsvImportJob extends ImportJob {
  protected createParser(): Parser {
    return new CsvParser();
  }
}

for (const job of [new JsonImportJob(), new CsvImportJob()]) {
  console.log(job.run());
}