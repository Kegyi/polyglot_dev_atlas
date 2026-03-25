from dataclasses import dataclass


class Printer:
    def print(self, message: str) -> None:
        raise NotImplementedError


class JsonLogger:
    def write_json(self, payload: str) -> None:
        print(payload)


@dataclass
class JsonLoggerAdapter(Printer):
    logger: JsonLogger

    def print(self, message: str) -> None:
        self.logger.write_json(f'{{"message":"{message}"}}')


JsonLoggerAdapter(JsonLogger()).print("build finished")
