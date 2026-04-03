from ex1.creatures import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory) -> None:
    print("Testing Creature with healing capability")

    print(" base:")
    base_a = factory.create_base()
    print(base_a.describe())
    print(base_a.attack())
    print(base_a.heal())

    print(" evolved:")
    base_ev = factory.create_evolved()
    print(base_ev.describe())
    print(base_ev.attack())
    print(base_ev.heal())


def transform_test(factory) -> None:
    print("\nTesting Creature with transform capability")

    print(" base:")
    base_sh = factory.create_base()
    print(base_sh.describe())
    print(base_sh.attack())
    print(base_sh.transform())
    print(base_sh.attack())
    print(base_sh.revert())

    print(" evolved:")
    base_ev = factory.create_evolved()
    print(base_ev.describe())
    print(base_ev.attack())
    print(base_ev.transform())
    print(base_ev.attack())
    print(base_ev.revert())


if __name__ == "__main__":
    h = HealingCreatureFactory()
    test_healing(h)
    sh = TransformCreatureFactory()
    transform_test(sh)
