#!/usr/bin/env python3

import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim",
               "release", "use"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
     targets: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    while len(targets) > 0:
        arrow = random.randint(0, len(targets) - 1)
        yield targets.pop(arrow)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    i = 0
    gevent = gen_event()
    while i < 1000:
        name, action = next(gevent)
        print(f"Event {i}: Player {name} did action {action}")
        i += 1

    list_ten = []
    for _ in range(10):
        list_ten.append(next(gevent))
    print(f"Built list of 10 events: {list_ten}")

    for event in consume_event(list_ten):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_ten}")


if __name__ == "__main__":
    main()
