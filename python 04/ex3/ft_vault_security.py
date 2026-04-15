#!/usr/bin/env python3

def secure_archive(filename: str, r_or_w: str,
                   to_write: str | None) -> tuple[bool, str]:

    returner: tuple = ()

    if r_or_w != "r" and r_or_w != "w":
        returner = (False, "Invalid commant, input r or w")
        return returner
    if r_or_w == "w" and to_write is None:
        returner = (False, "Invalid use of w, input a text to write")
        return returner

    try:
        with open(filename, r_or_w) as f:
            if r_or_w == "r":
                print("Using 'secure_archive' to read from a regular file:")
                returner = (True, f.read())
            else:
                print("Using 'secure_archive' to write previous content to a "
                      "new file:")
                f.write(to_write)
                returner = (True, to_write)
            return returner
    except FileNotFoundError as err:
        print("Using 'secure_archive' to read from a nonexistent file:")
        returner = (False, str(err))
        return returner
    except PermissionError as err:
        print("Using 'secure_archive' to read from an inaccessible file:")
        returner = (False, str(err))
        return returner


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    a: tuple = secure_archive("aa.txt", "w", "success")
    print(a)


if __name__ == "__main__":
    main()

"""
open(), read(), write(), print()

V   1 use with
V   2 create secure_archive()
        2.1 input:
V       -file name
V       -optional int or str indicating if it must read or write
V       -optional str to write in the file
        2.2 try -> with
V           2.2.1 if it fails return error
            2.2.2 if it works check if read or write
                2.2.2.1 if it's read return the text
                2.2.2.1 it it's write then write

V       X it return a tuple (True|False, str) for success / failure of
             operation then the content / the error message
V        X secure against invalid r_or_w

input:
file name
optionnal int or str indicating if it must read or write
optionnal str to write in the file

This exercise requires the use of the with statement (context manager) to
ensure proper file handling. The with statement automatically closes files
even if errors occur, preventing resource leaks.


Create a function secure_archive() that provides safe access to any file
for reading or writing.

It returns a tuple (True|False, str) that indicates whether the operation
succeeded (the boolean) and provides the associated content (either the
file’s contents or an error message).

The function takes the following parameters: a mandatory file name, an optional
int or str (your choice) that indicates the action to perform (read or write),
and another optional string that contains the content to write to the file.

During the defense, the structure of the code will be reviewed to match these
requirements.
"""
