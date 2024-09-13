"""Challenge question number 1"""

__author__ = "730760489"


def mimic(message: str) -> str:
    """A function that returns your message to yourself"""
    return message


def main() -> None:
    """Print the result of calling mimic"""
    print(mimic(message=input("What is your name?")))


if __name__ == "__main__":
    main()
