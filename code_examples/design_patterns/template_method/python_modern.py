# Modern Python Template Method using higher-order functions
# No abstract base class - the template is a plain function that takes callables.
from typing import Callable

def process_data(
    read:  Callable[[], None],
    parse: Callable[[], None],
    write: Callable[[], None],
) -> None:
    read()
    parse()
    write()

# CSV processor - plain functions, no subclass needed
def csv_read()  -> None: print("Reading CSV data")
def csv_parse() -> None: print("Parsing CSV")
def csv_write() -> None: print("Writing processed CSV")

# JSON processor
def json_read()  -> None: print("Reading JSON data")
def json_parse() -> None: print("Parsing JSON")
def json_write() -> None: print("Writing processed JSON")

process_data(csv_read,  csv_parse,  csv_write)
process_data(json_read, json_parse, json_write)
