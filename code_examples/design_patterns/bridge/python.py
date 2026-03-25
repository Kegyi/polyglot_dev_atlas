from dataclasses import dataclass
from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> None: ...


class EmailSender:
    def send(self, message: str) -> None:
        print(f"email: {message}")


class SmsSender:
    def send(self, message: str) -> None:
        print(f"sms: {message}")


@dataclass
class AlertNotification:
    sender: Sender

    def notify(self, message: str) -> None:
        self.sender.send(f"alert -> {message}")


AlertNotification(EmailSender()).notify("CPU high")
AlertNotification(SmsSender()).notify("CPU high")
