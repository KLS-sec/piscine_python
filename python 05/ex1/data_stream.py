#!/usr/bin/env python3

from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise Exception("No data to output")
        rank = self._counter - len(self._storage)
        value = self._storage.pop(0)
        return (rank, value)

###########################################


NumInput = typing.Union[int, float, list[typing.Union[int, float]]]


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: NumInput) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, list):
            for x in data:
                self._storage.append(str(x))
                self._counter += 1
            return
        self._storage.append(str(data))
        self._counter += 1


TxtInput = str | list[str]
# modern version for union


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: TxtInput) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, list):
            for x in data:
                self._storage.append(str(x))
                self._counter += 1
            return
        self._storage.append(str(data))
        self._counter += 1


LogInput = typing.Union[dict[str, str], list[dict[str, str]]]


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(a, str) and isinstance(b, str)
                       for a, b in data.items())
        if isinstance(data, list):
            return all(isinstance(x, dict) and
                       all(isinstance(a, str) and isinstance(b, str)
                       for a, b in x.items()) for x in data)
        return False

    def ingest(self, data: LogInput) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        def auto_extract(data: dict[str, str]) -> str:
            return (f"{data.get('log_level', '')}:"
                    f" {data.get('log_message', '')}")

        if isinstance(data, list):
            for x in data:
                self._storage.append(auto_extract(x))
                self._counter += 1
            return
        # two different versions to test things
        self._storage.append(f"{data.get('log_level', '')}: "
                             f"{data.get('log_message', '')}")
        self._counter += 1


class DataStream():
    def __init__(self) -> None:
        self._processor_list: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise TypeError("Error, invalid type, "
                            "please input a DataProcessor")
            return
        self._processor_list.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        if not len(self._processor_list):
            print("No processor found, no data")
            return
        if not isinstance(stream, list):
            raise TypeError("Error, invalid type, please input a list")
        if not stream:
            print("Error, empty list.")
            return
        for processor in self._processor_list:
            list_processing: list[typing.Any] = []
            for data in stream:
                if processor.validate(data):
                    processor.ingest(data)
                else:
                    list_processing.append(data)
            stream[:] = list_processing  # [:] for data replacement

        for x in stream:
            print(f"DataStream error - Can't process element "
                  f"in stream: {x}")

    def print_processors_stats(self) -> None:
        if not len(self._processor_list):
            print("No processor found, no data")
            return
        for x in self._processor_list:
            name = x.__class__.__name__.removesuffix('Processor')
            print(f"{name} Processor: total {x._counter} items processed,"
                  f" remaining {len(x._storage)} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    print("== DataStream statistics ==")

    stream = DataStream()
    stream.print_processors_stats()

    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    print("\nRegistering Numeric Processor\n")
    stream.register_processor(num)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! Use ssh"
             " instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch.copy())

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(txt)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(batch.copy())

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: Numeric 3, "
          "Text 2, Log 1")

    for _ in range(3):
        try:
            num.output()
        except Exception:
            break

    for _ in range(2):
        try:
            txt.output()
        except Exception:
            break

    for _ in range(1):
        try:
            log.output()
        except Exception:
            break

    print("== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()


"""
https://www.w3schools.com/python/python_polymorphism.asp
https://www.geeksforgeeks.org/python/polymorphism-in-python/
https://realpython.com/ref/glossary/polymorphism/#:~:text=Polymorphism%20enables%20you%20to%20use,through%20inheritance%20and%20method%20overriding.

builtins, standard types, import typing, import abc

TODO
DataStram class:
-receive stream of data of multiple types
-send it to the corect processor
-use polymorphic behavior

WILL CONTAIN:
#####################################################"

def print_processors_stats(self) -> None:
print stream statistics
data of every class

create a test scenario:
corect uses of processors
display stats
use output method to consume elements
display stat again

to know:
polymorphic behavior
extending the system with new data type
modify process behavior

# **** securise log.validate(), for if the key does not look
# like "log_level"and "log_message"

# for the main
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())

TODO: DONE
in DataStream:
def register_processor(self, proc: DataProcessor) -> None:
register a new data processor to process the stream

def process_stream(self, stream: list[typing.Any]) -> None:
analyze each elements of the list received as parameter
sent it to the apropriate registered data processor
Error message if no processor can handle an element

###############################################

possible solution au pb de

        list_rest: list[typing.Any] =
        for data in stream:
            handled = False
            for processor in self._processor_list:
                if processor.validate(data):
                    processor.ingest(data)
                    handled = True
                    break   # stops here → guarantees single processor
            if not handled:
                print error

################################################################"

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

##########################################################
Use your code from Exercise 0 and improve it:
• Create a DataStream class that will receive a stream of data containing
different types and then will route each element to the appropriate data
processor using polymorphic behavior.
• This class will implement the
def register_processor(self, proc: DataProcessor) -> None:
method that allows you to register a new data processor to process
the data stream.
• This class will implement the
def process_stream(self, stream: list[typing.Any]) -> None:
method that will analyze each element of the list received as a parameter
and send it to the appropriate registered data processor. Error messages
will be printed if no data processor can handle an element.
• Finally, the class will implement the
def print_processors_stats(self) -> None:
method in order to print stream statistics.
• Create a test scenario that demonstrates the correct processing of a
data stream. Display statistics on registered data processors, consume
elements using the output method of each data processor and show updated
statistics.
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
