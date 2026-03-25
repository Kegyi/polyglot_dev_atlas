#!/usr/bin/env python3
from datetime import datetime, timedelta


def main() -> None:
    now = datetime.now()
    later = now + timedelta(minutes=90)

    print("now:", now.isoformat(timespec="seconds"))
    print("later:", later.isoformat(timespec="seconds"))
    print("later > now:", later > now)


if __name__ == "__main__":
    main()
