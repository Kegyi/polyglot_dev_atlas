interface Printer {
  print(message: string): void;
}

class JsonLogger {
  writeJson(payload: string): void {
    console.log(payload);
  }
}

class JsonLoggerAdapter implements Printer {
  constructor(private readonly logger: JsonLogger) {}

  print(message: string): void {
    this.logger.writeJson(`{"message":"${message}"}`);
  }
}

new JsonLoggerAdapter(new JsonLogger()).print('build finished');
