#!/usr/bin/env python3

# check the ****
# utiliser les union et coriger les type accepte par les ingest, PAS DE ANY

from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._counter: int = 0  # total ingested (rank source)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise Exception("No data to output")
        value = self._storage.pop(0)
        rank = self._counter - len(self._storage) - 1
        return (rank, value)


# ---------- NUMERIC ----------

NumericInput = Union[int, float, list[Union[int, float]]]


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: NumericInput) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, list):
            for x in data:
                self._storage.append(str(x))
                self._counter += 1
        else:
            self._storage.append(str(data))
            self._counter += 1


# ---------- TEXT ----------

TextInput = Union[str, list[str]]


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: TextInput) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, list):
            for x in data:
                self._storage.append(x)
                self._counter += 1
        else:
            self._storage.append(data)
            self._counter += 1


# ---------- LOG ----------

LogDict = dict[str, str]
LogInput = Union[LogDict, list[LogDict]]


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_log(d: Any) -> bool:
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            )

        if is_valid_log(data):
            return True
        if isinstance(data, list):
            return all(is_valid_log(x) for x in data)
        return False

    def ingest(self, data: LogInput) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        def format_log(d: LogDict) -> str:
            return f"{d.get('log_level', '')}: {d.get('log_message', '')}"

        if isinstance(data, list):
            for d in data:
                self._storage.append(format_log(d))
                self._counter += 1
        else:
            self._storage.append(format_log(data))
            self._counter += 1


# ---------- TEST ----------

def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    print("\nTesting Numeric Processor...")
    print("Validate 42:", num.validate(42))
    print("Validate 'Hello':", num.validate("Hello"))

    try:
        print("Invalid ingest 'foo'")
        num.ingest("foo")  # type: ignore
    except Exception as e:
        print("Got exception:", e)

    num.ingest([1, 2, 3, 4, 5])
    print("Extract 3 values:")
    for _ in range(3):
        r, v = num.output()
        print(f"Numeric value {r}: {v}")

    print("\nTesting Text Processor...")
    print("Validate 42:", txt.validate(42))
    txt.ingest(["Hello", "Nexus", "World"])
    r, v = txt.output()
    print(f"Text value {r}: {v}")

    print("\nTesting Log Processor...")
    print("Validate 'Hello':", log.validate("Hello"))
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data:{logs}")
    log.ingest(logs)
    for _ in range(2):
        r, v = log.output()
        print(f"Log entry {r}: {v}")


"""
This exercise requires the use of abstract classes using ABC (Abstract Base
Class). We will first create separate classes that share common interfaces.
In the next exercise, they will be unified in the same workflow.

Set up the following architecture:
• An abstract class DataProcessor that inherits from ABC and defines the
common processing interface.

• Three specialized classes NumericProcessor, TextProcessor, and
LogProcessor that inherit from the DataProcessor class and will process
different kinds of data.
• Two abstract methods in DataProcessor: validate, which will check whether
the input data are appropriate for the current data processor, and ingest,
which will process the input data. Each specialized class will need to
override these methods.
• One standard method in DataProcessor: output, which will output ingested
data.

You need to comply with the following constraints:
• The validate method will be defined as validate(self, data: Any) -> bool
in the DataProcessor class. The overriding methods in the specialized classes
will share the same signature, as they cannot know what data will be sent and
must Code Nexus Polymorphic Data Streams in the Digital Matrix accept any type.
This method returns a bool that indicates if the provided data can be ingested
by this data processor.
• The ingest method will be defined as ingest(self, data: Any) -> None in the
DataProcessor class. The overriding methods in the specialized classes will
have their own specific signatures to match the types they expect. In case
the user does not validate the data before calling ingest, and provides
invalid data, an exception must be raised.
• The output method will be defined as output(self) -> tuple[int, str] in the
DataProcessor class. There is no need to override it in the specialized
classes.
• The NumericProcessor ingests int, float, and lists of both types (including
mixed-type lists). It then converts the data into strings and stores it
internally, waiting to be extracted using the output method. The overriding
ingest method signature must reflect the accepted types.
• The TextProcessor ingests str and lists of strings. It stores the data
internally, waiting to be extracted using the output method. The overriding
ingest method signature must reflect the accepted types.
• The LogProcessor ingests a dict of string key-value pairs, and lists of that
type. It then converts the data into strings and stores it internally, waiting
to be extracted using the output method. The overriding ingest method
signature must reflect the accepted types.
• The output method will extract the oldest piece of data stored internally
in the data processor, along with the associated processing rank within the
data processor.
The piece of data is then removed from the data processor.

Finally, test your architecture:
• Create instances for each specialized class.
• Test valid and invalid data for each class through the validate method.
• Test at least one invalid data item with the ingest method without prior
validation, and check that it raises an exception. This will leave you with
a mypy warning, on purpose.
• Ingest various data for each data processor and then extract it using output.

•All code must include comprehensive type annotations.
Check this using mypy .
•Exception handling should protect the data streams from corruption.
•Authorized imports: abc and typing .
•All standard classes and collections are authorized, along with their
methods (int, str, list, dict, etc.).
•All built-in functions are authorized.

During evaluation, you may be asked to explain polymorphic behavior,
demonstrate method overriding, extend your systems with new data
types, or modify processing behavior. Make sure you understand how
inheritance enables code reuse while allowing behavioral specialization.
"""

if __name__ == "__main__":
    main()
