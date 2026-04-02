from ex0.factories import FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    InvalidStrategyException,
)


def create_creature(factory):
    return factory.create_base()


def fight(opponent1, opponent2):
    factory1, strategy1 = opponent1
    factory2, strategy2 = opponent2

    c1 = create_creature(factory1)
    c2 = create_creature(factory2)

    print(f"{c1.describe()}")
    print("vs.")
    print(f"{c2.describe()}")
    print("now fight!")

    try:
        strategy1.act(c1, c2)
        strategy2.act(c2, c1)
    except InvalidStrategyException as e:
        raise e


def tournament(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            print("* Battle *")

            try:
                fight(opponents[i], opponents[j])
            except InvalidStrategyException as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":

    flame = FlameFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    aqua = AquaFactory()

    print("Tournament 0 (basic)")
    tournament([
        (flame, NormalStrategy()),
        (healing, DefensiveStrategy()),
    ])

    print("\nTournament 1 (error)")
    tournament([
        (flame, AggressiveStrategy()),
        (healing, DefensiveStrategy()),
    ])

    print("\nTournament 2 (multiple)")
    tournament([
        (aqua, NormalStrategy()),
        (healing, DefensiveStrategy()),
        (transform, AggressiveStrategy()),
    ])
