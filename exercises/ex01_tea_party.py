"""Program that determines amount of tea bags, treats, and cost for the tea party."""

__author__: str = "730760489"


def main_planner(guests: int) -> None:
    """Calls tea bag and treat function to output amount of supplies needed for party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Given amount of people, returns amount of tea bags needed."""
    return people * 2


def treats(people: int) -> int:
    """Returns amount of treats needed based on tea bags per person."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Returns calculates cost based on amount of tea bags and treats. """
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    """Making the program runnable and asking a user for input when they run """
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
