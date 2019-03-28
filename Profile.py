import random


class Property:
    def __init__(self):
        self.tizhi = random.randint(1, 10)
        self.speed = random.randint(1, 10)
        self.wuxing = {'J': random.randint(1, 10), 'M': random.randint(1, 10), 'S': random.randint(1, 10),
                       'H': random.randint(1, 10), 'T': random.randint(1, 10)}
        self.int = random.randint(1, 10)
        self.gengu = random.randint(1, 7)


