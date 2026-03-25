from dataclasses import dataclass
from typing import Protocol


class Notifier(Protocol):
    def send(self, message: str) -> None: ...


class EmailNotifier:
    def send(self, message: str) -> None:
        print(f"email: {message}")


@dataclass
class SmsDecorator:
    inner: Notifier

    def send(self, message: str) -> None:
        self.inner.send(message)
        print(f"sms: {message}")


SmsDecorator(EmailNotifier()).send("deployment done")
