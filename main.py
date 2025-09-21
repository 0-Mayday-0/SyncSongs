from time import sleep as tsleep
from sets import Line, CharacterSet
from playsound import playsound
import threading


class Song:
    def __init__(self):
        self.intro_line: Line = Line([
                    CharacterSet("The sun ", 0.05),
                    CharacterSet("says leave.\n", 0.05),
                    CharacterSet("The clock ", 0.05),
                    CharacterSet("agrees.\n", 0.07),
                    CharacterSet("My dreams ", 0.05),
                    CharacterSet("have left ", 0.05),
                    CharacterSet("ahead ", 0.1),
                    CharacterSet("of me.\n", 0.06),
                    CharacterSet("The mo", 0.07),
                    CharacterSet("ment flew.\n", 0.07),
                    CharacterSet("They al", 0.07),
                    CharacterSet("ways do.\n", 0.07),
                    CharacterSet("Seems one ", 0.05),
                    CharacterSet("is some", 0.07),
                    CharacterSet("times more ", 0.07),
                    CharacterSet("than two.\n", 0.07)
                    ],
            2)

        self.chorus_lines: dict[str, Line] = {
            'made up':
                Line([
                    CharacterSet("\nEverything is made up.\n", 0.1),
                    CharacterSet("Everything is made up.\n", 0.1),
                    CharacterSet("Everything belongs to someone else.\n", 0.07)
                ], 2.7),
            'universe':
                Line([
                    CharacterSet("And everyone's a world inside themselves.\n", 0.07),
                    CharacterSet("The universe and I both understand...\n", 0.1),
                    CharacterSet("...that nothing's more amusing than a plan.\n", 0.7),
                ], 1.7)
        }

    @staticmethod
    def async_sound(path):
        threading.Thread(target=playsound, args=(path,), daemon=True).start()

    def intro(self):

        tsleep(20.6)

        self.intro_line.print_delay()

    def chorus(self):
        tsleep(0.45)

        for key, line in self.chorus_lines.items():
            line.print_delay()


def main():
    song = Song()
    song.async_sound("./music/exit-enter.mp3")

    song.intro()
    song.chorus()

if __name__ == '__main__':
    main()