#!/usr/bin/env python3

from abc import ABC, abstractmethod
import typing


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = [f'"item_{r}": "{v}"' for r, v in data]
        print("{" + ", ".join(items) + "}")


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values = [v for _, v in data]
        print(",".join(values))


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
            stream[:] = list_processing

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if not self._processor_list:
            print("No processor found, no data")
            return
        for x in self._processor_list:
            container: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    container.append(x.output())
                except Exception:
                    break
            plugin.process_output(container)


def main():
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")

    stream = DataStream()
    csv_plugin = CSVPlugin()
    json_plugin = JSONPlugin()

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh '
          'instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]
    print(f"\nSend first batch of data on stream: {batch1}")
    stream.process_stream(batch1)

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv_plugin)

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE', 'log_message': 'Certificate expires in '
          '10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json_plugin)

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()

"""
CSV/JSON
    classes, contain their own process_output
def process_output(self, data: list[tuple[int, str]]) -> None:
    receive data from output_pipeline
    process the data in the correct format
    print them


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = [f'"item_{r}": "{v}"' for r, v in data]
        print("{" + ", ".join(items) + "}")

class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values = [v for _, v in data]
        print(",".join(values))


def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
    # error if list empty or no processor ****
    for x in self._processor_list():
        container: list[tuple[int, str]] = []
        for _ in range(nb):
            container.append(x._counter - x._storage)
            container.append(x.output())
        # send it to the plugin ****
"""

"""
to add into DataStream:
def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
    call nb elements from all data processors
    send them to "plugin" (CSV or JSON) (the plugin treat and print)

def process_output(self, data: list[tuple[int, str]]) -> None:
    int = number of the processed data

int only for JSON
"""

"""
https://www.w3schools.com/python/python_json.asp
https://docs.python.org/fr/3/library/json.html
https://www.geeksforgeeks.org/python/duck-typing-in-python/
https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
json/csv format
see on gpt
class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = [f'"item_{r}": "{v}"' for r, v in data]
        print("{" + ", ".join(items) + "}")

class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values = [v for _, v in data]
        print(",".join(values))


builtins, standard types, import typing, import abc

######################################

TODO
to add into DataStream:
def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
    call nb elements from all data processors
    send them to "plugin" (CSV or JSON) (the plugin treat and print)

XXX
use code from ex1
use duck typing

class ExportPlugin
inherit from the Protocol class
is a form of type hint

def process_output(self, data: list[tuple[int, str]]) -> None:
    defined in ExportPlugin
    present in CSV and JSON

#

CSV/JSON
    classes, contain their own process_output
def process_output(self, data: list[tuple[int, str]]) -> None:
    receive data from output_pipeline
    process the data in the correct format
    print them

######################################

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

####################################"

Use your code from Exercise 1 and improve it in order to obtain a complete
data pipeline. Your DataStream class already handles input streams correctly.
You need now to handle the output part of the pipeline. This will be achieved
by using a plugin system for export classes, made export-compatible through
duck typing.

Implement the following:
• A new ExportPlugin class that inherits from the special Protocol class.
• This class will define the following method, which will act as a constraint
for each export plugin:
def process_output(self, data: list[tuple[int, str]]) -> None:
The type of the data parameter is a list of tuples that matches the return
value of the output method from the DataProcessor class.
• The DataStream class will now implement the
def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
method, to be used after calling process_stream, that will consume nb elements
from all registered data processors and export them using the provided
compatible plugin.
• Create at least a CSV export plugin and a JSON export plugin. No need to use
a specific import for these plugins, manually create valid CSV and
JSON strings.
"""
