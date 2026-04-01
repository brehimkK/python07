from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical
import random


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)

        self.mana_pool = random.randint(3, 6)
        self.block_power = random.randint(1, 4)

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters battlefield"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.cost,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.block_power, incoming_damage)
        taken = incoming_damage - blocked

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True
        }

    def get_combat_stats(self) -> dict:
        return {
            "block_power": self.block_power
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = min(4, self.mana_pool)

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount

        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_pool": self.mana_pool
        }
