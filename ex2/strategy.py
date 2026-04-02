from abc import ABC, abstractmethod
from ex2.exceptions import InvalidStrategyException


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature, opponent) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature, opponent) -> None:
        print(creature.attack())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature, opponent) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )

        print(creature.attack())
        print(creature.heal())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "transform") and hasattr(creature, "revert")

    def act(self, creature, opponent) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
