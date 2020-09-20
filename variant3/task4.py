from typing import Dict


class Thing:
    def __init__(self, kind, armor=0, strength=0, agility=0, intelligence=0):
        self._kind = kind
        self._armor = armor
        self._strength = strength
        self._agility = agility
        self._intelligence = intelligence

    def kind(self):  # возвращает вид вещи
        return self._kind

    def armor(self):  # возвращает броню вещи
        return self._armor

    def strength(self):  # возвращает силу, получаемую от вещи
        return self._strength

    def agility(self):  # возвращает ловкость, получаемую от вещи
        return self._agility

    def intelligence(self):  # возвращает интеллект, получаемую от вещи
        return self._intelligence

    def copy(self):  # возвращает копию объекта.
        return Thing(self._kind, self._armor, self._strength, self._agility, self._intelligence)

    def __eq__(self, other):  # thing1 == thing2
        # возвращает True, если все параметры вещей равны, иначе False
        try:
            return type(other) is Thing and all((
                self._kind == other.kind(),
                self._armor == other.armor(),
                self._strength == other.strength(),
                self._agility == other.agility(),
                self._intelligence == other.intelligence()
            ))
        except Exception:
            return False

    def __sub__(self, other):  # thing - number
        # возвращает копию вещи с броней сниженной на number пунктов, если броня падает до нуля возвращает None
        if self._armor - other <= 0:
            del self
            return
        return Thing(self._kind, self._armor - other, self._strength, self._agility, self._intelligence)

    def __isub__(self, other):  # thing -= number
        # снижает броню вещи на number пунктов, если броня падает до нуля объект вырождается в None
        self._armor -= other
        return None if self._armor <= 0 else self

    def __mul__(self, other):  # thing * number
        # возвращает копию вещи с увеличенными силой, ловкостью и интеллектом в number раз
        return Thing(self._kind,
                     self._armor,
                     self._strength * other,
                     self._agility * other,
                     self._intelligence * other)

    def __str__(self):  # str(thing)
        # возвращает строку описывающую вещь в формате "Kind - Armor: Ar, Strength: S, Agility: Ag, Intelligence: I"
        return "%s - Armor: %s, Strength: %s, Agility: %s, Intelligence: %s" % (
            self._kind,
            self._armor,
            self._strength,
            self._agility,
            self._intelligence
        )


class Player:
    def __init__(self):
        self._things = {}  # type: Dict[str, Thing]

    def armor(self):  # armor() - возвращает суммарную броню героя
        return sum(map(lambda x: x.armor(), self._things.values()))

    def strength(self):  # strength() - возвращает суммарную силу героя
        return sum(map(lambda x: x.strength(), self._things.values()))

    def agility(self):  # agility() - возвращает суммарную ловкость героя
        return sum(map(lambda x: x.agility(), self._things.values()))

    def intelligence(self):  # intelligence() - возвращает суммарный интеллект героя
        return sum(map(lambda x: x.intelligence(), self._things.values()))

    def put_on(self, thing: Thing):  # put_on(thing)
        # надевает на героя заданный предмет. Если на героя уже был надет предмет такого вида, заменяет его
        self._things[thing.kind()] = thing.copy()

    def take_off(self, kind: str):  # take_oﬀ(kind)
        # снимает вещь заданного вида, если она есть, иначе ничего не происходит
        if kind in self._things:
            del self._things[kind]

    def __lshift__(self, thing: Thing):  # player << thing
        # надевает на героя копию заданного предмета. Если на героя уже был надет предмет такого вида, заменяет его
        self.put_on(thing)

    def __rshift__(self, thing: Thing):  # player >> kind
        # снимает вещь заданного вида, если она есть, иначе ничего не происходит
        self.take_off(thing)

    def __isub__(self, number: int):  # player -= number
        # снижает броню всех вещей героя на number пунктов, если броня вещи опускается до нуля, снимает ее
        for thing in list(self._things.values()):
            if thing.armor() - number <= 0:
                self.take_off(thing.kind())
            thing -= number
        return self

    def __getitem__(self, kind):  # player[kind]
        # возвращает вещь заданного вида надетую на игрока, если такой вещи нет возвращает None
        return self._things.get(kind, None)

    def __str__(self):  # str(player)
        # возвращает строковое представление героя
        return """Player - 
    Armor: %s, 
    Strength: %s, 
    Agility: %s, 
    Intelligence: %s""" % (self.armor(), self.strength(), self.agility(), self.intelligence())
