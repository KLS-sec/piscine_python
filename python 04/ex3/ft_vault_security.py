#!/usr/bin/env python3

def secure_archive(filename: str, r_or_w: str = "r",
                   to_write: str = "") -> tuple[bool, str]:

    if r_or_w != "r" and r_or_w != "w":
        return (False, "Invalid command, input r or w")
    if r_or_w == "w" and to_write == "":
        return (False, "Invalid use of w, input a text to write")

    try:
        with open(filename, r_or_w) as f:
            if r_or_w == "r":
                print("Using 'secure_archive' to read from a regular file:")
                return (True, f.read())
            else:
                print("Using 'secure_archive' to write previous content to a "
                      "new file:")
                f.write(to_write)
                return (True, "Content successfully written to file")
    except FileNotFoundError as err:
        print("Using 'secure_archive' to read from a nonexistent file:")
        return (False, str(err))
    except PermissionError as err:
        print("Using 'secure_archive' to read from an inaccessible file:")
        return (False, str(err))
    except Exception as err:
        print("Using 'secure_archive' incorectly:")
        return (False, str(err))


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    a = secure_archive("aaa.txt", "r", "")
    print(a)  # strange print is asked by the exercise


if __name__ == "__main__":
    main()
