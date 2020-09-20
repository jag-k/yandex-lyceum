from typing import List

STRENGTH_COEF = 3
AGILITY_COEF = 2
INTELLIGENCE_COEF = 1


class Weapon:
    def __init__(self, one_handed=False, strength=0, agility=0, intelligence=0):
        self._one_handed = one_handed
        self._strength = strength
        self._agility = agility
        self._intelligence = intelligence

    def is_one_handed(self):
        return self._one_handed

    def strength(self):
        return self._strength

    def agility(self):
        return self._agility

    def intelligence(self):
        return self._intelligence

    def speed(self):
        return sum((
            self.strength() * STRENGTH_COEF,
            self.agility() * AGILITY_COEF,
            self.intelligence() * INTELLIGENCE_COEF
        ))

    def __add__(self, other: int):
        one_hand = not other % 2
        return Weapon(one_hand,
                      self.strength() + STRENGTH_COEF * other,
                      self.agility() + AGILITY_COEF * other,
                      self.intelligence() + INTELLIGENCE_COEF * other,
                      )

    def __iadd__(self, other: int):
        self._one_handed = bool(other % 2)
        self._strength += STRENGTH_COEF * other
        self._agility += AGILITY_COEF * other
        self._intelligence += INTELLIGENCE_COEF * other
        return self

    def __round__(self, n=2):
        return Weapon(self._one_handed,
                      self.strength() - self.strength() % n,
                      self.agility() - self.agility() % n,
                      self.intelligence() - self.intelligence() % n,
                      )

    def copy(self):
        return Weapon(**dict(map(lambda x: (x[0][1:], x[1]), self.__dict__.items())))

    def __str__(self):
        return "Weapon[%d](strength: %s, agility: %s, intelligecne: %s, speed: %s)" % (
            2 - int(self.is_one_handed()),
            self.strength(),
            self.agility(),
            self.intelligence(),
            self.speed()
        )


class Player:
    def __init__(self):
        self._weapon = []  # type: List[Weapon]

    def strength(self):  # strength() - возвращает суммарную силу героя
        return sum(map(lambda x: x.strength(), self._weapon))

    def agility(self):  # agility() - возвращает суммарную ловкость героя
        return sum(map(lambda x: x.agility(), self._weapon))

    def intelligence(self):  # intelligence() - возвращает суммарный интеллект героя
        return sum(map(lambda x: x.intelligence(), self._weapon))

    def speed(self):
        return sum(map(lambda x: x.speed(), self._weapon))

    def take_up_weapon(self, weapon):
        w = weapon.copy()
        if self._weapon and (len(self._weapon) == 2 or not self._weapon[0].is_one_handed()):
            self.throw_a_weapon()
        self._weapon.append(w)

    def throw_a_weapon(self):
        del self._weapon[0]

    def __next__(self):
        self.throw_a_weapon()

    def __and__(self, other):
        self.take_up_weapon(other)

    def __str__(self):  # str(player)
        # возвращает строковое представление героя
        return """Player[%s]( 
Strength: %s, 
Agility: %s, 
Intelligence: %s, 
Speed: %s 
)""" % (len(self._weapon), self.strength(), self.agility(), self.intelligence(), self.speed())
