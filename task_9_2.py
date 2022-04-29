class Road:
    _length = 5000
    _width = 20

    def __init__(self):
        self._weight = 25 / 1000
        self._thickness = 5

    def total_weight(self):
        return round(self._length * self._width * self._weight * self._thickness)


r = Road()
print(f'{r.total_weight()} т')
