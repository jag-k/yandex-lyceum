class Gem:
    def __init__(self, strength=0, agility=0, intelligence=0):
        self._strength = strength
        self._agility = agility
        self._intelligence = intelligence

    def strength(self):  # strength()
        # возвращает силу, получаемую от кристалла
        return self._strength

    def agility(self):  # agility()
        # возвращает ловкость, получаемую от кристалла
        return self._agility

    def intelligence(self):  # intelligence()
        # возвращает интеллект, получаемый от кристалла
        return self._intelligence

    def copy(self):  # copy()
        # возвращает копию кристалла
        return Gem(self._strength, self._agility, self._intelligence)

    def __add__(self, gem):  # gem1 + gem2
        # создает кристалл, вычисляя целочиселнное среднее арифметическое
        # соответствующих характеристик переданных камней
        return Gem(
            self._ar_mean(self._strength, gem.strength()),
            self._ar_mean(self._agility, gem.agility()),
            self._ar_mean(self._intelligence, gem.intelligence())
        )

    def __iadd__(self, gem):  # gem1 += gem2
        # изменяет характеристики первого кристалла, вычисляя целочиселнное среднее арифметическое
        # соответствующих характеристик переданных камней
        self._strength = self._ar_mean(self._strength, gem.strength())
        self._agility = self._ar_mean(self._agility, gem.agility())
        self._intelligence = self._ar_mean(self._intelligence, gem.intelligence())
        return self

    def __round__(self, n=2):  # round(gem, number)
        # "выравнивает"характеристики камня, путем целочисленного деления их суммы на переданное значение
        self._strength = self._agility = self._intelligence = \
            sum((self._strength, self._agility, self._intelligence)) // n

    def __str__(self):  # str(gem)
        # возвращает строковое представление кристала
        return "Gem(strength: %s, agility: %s, intelligence: %s)" % (
            self._strength,
            self._agility,
            self._intelligence
        )

    @staticmethod
    def _ar_mean(*args):  # Среднее арифметическое
        return sum(args) // len(args) if args else 0


class Thing:
    def __init__(self, name, armor=0, strength=0, agility=0, intelligence=0):
        self.name = name
        self._armor = armor
        self._strength = strength
        self._agility = agility
        self._intelligence = intelligence
        self._gems = []

    def armor(self):  # возвращает броню вещи
        return self._armor

    def strength(self):  # возвращает силу, получаемую от вещи
        return sum(map(lambda x: x.strength(), self._gems)) + self._strength

    def agility(self):  # возвращает ловкость, получаемую от вещи
        return sum(map(lambda x: x.agility(), self._gems)) + self._agility

    def intelligence(self):  # возвращает интеллект, получаемую от вещи
        return sum(map(lambda x: x.intelligence(), self._gems)) + self._intelligence

    def push(self, gem):
        if len(self._gems) == 3:
            del self._gems[0]
        self._gems.append(gem.copy())

    def pop(self, count):
        for i in range(count):
            next(self)

    def __lshift__(self, gem):
        self.push(gem)

    def __next__(self):
        if self._gems:
            del self._gems[-1]

    def __str__(self):
        return "%s( \nArmor: %s, \nStrength: %s, \nAgility: %s, \nIntelligence: %s \n)" % (
            self.name,
            self.armor(),
            self.strength(),
            self.agility(),
            self.intelligence()
        )
