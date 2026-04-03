from ex0.factory import FlameFactory, AquaFactory


def test_factory(factory) -> None:
    print("\nTesting factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(base.attack())


def test_battle(a, b) -> None:
    print("\nTesting battle")
    base_a = a()
    a_c = base_a.create_base()
    print(a_c.describe())
    print("vs.")
    base_b = b()
    b_c = base_b.create_base()
    print(b_c.describe())

    print("  fight!")

    print(a_c.attack())
    print(b_c.attack())


if __name__ == "__main__":
    flam = FlameFactory()
    test_factory(flam)
    aqua = AquaFactory()
    test_factory(aqua)
    test_battle(FlameFactory, AquaFactory)
