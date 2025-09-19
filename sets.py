from collections.abc import Iterable
from time import sleep as tsleep

class CharacterSet:
    def __init__(self, chars: Iterable, delay: float | int) -> None:
        self.characters = iter(chars)
        self.delay = delay

    def yield_delay(self):
        for character in self.characters:
            yield character
            tsleep(self.delay)

    def __iter__(self):
        yield from self.yield_delay()


class Line:
    def __init__(self, sets: list[CharacterSet]) -> None:
        self.sets = sets

    def print_delay(self):
        for st in self.sets:
            for i in st:
                print(i, end='', flush=True)

def main() -> None:
    a = Line([CharacterSet("Hello ", 0.2), CharacterSet("World", 0.5)])

    a.print_delay()

if __name__ == '__main__':
    main()