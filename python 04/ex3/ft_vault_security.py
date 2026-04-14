#!/usr/bin/env python3


if __name__ == "_main__":
    main()

"""
open(), read(), write(), print()

This exercise requires the use of the with statement (context manager) to
ensure proper file handling. The with statement automatically closes files
even if errors occur, preventing resource leaks.

Create a function secure_archive() that provides safe access to any file
for reading or writing. It returns a tuple (True|False, str) that indicates
whether the operation succeeded (the boolean) and provides the associated
content (either the file’s contents or an error message). The function takes
the following parameters: a mandatory file name, an optional int or str (your
choice) that indicates the action to perform (read or write), and another
optional string that contains the content to write to the file.

During the defense, the structure of the code will be reviewed to match these
requirements.
"""
