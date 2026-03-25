#!/usr/bin/env python3
from enum import Enum


class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"


MAX_RETRIES = 3


def main() -> None:
    status = Status.RUNNING
    print("status:", status.value)
    print("max retries:", MAX_RETRIES)


if __name__ == "__main__":
    main()
