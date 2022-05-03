class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self, manufacturer, model, release):
        self._manufacturer = manufacturer
        self._model = model
        self._release = release
        self.data = {}


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, release, is_color, print_format, print_speed):
        super().__init__(manufacturer, model, release)
        self.is_color = is_color
        self.print_format = print_format
        self.print_speed = print_speed
        self.name = (self._manufacturer, self._model, self._release)
        self.param = [self.is_color, self.print_format, self.print_speed]
        self.data[self.name] = self.param

    def __str__(self):
        return f'{self.data}'


class Xerox(OfficeEquipment):
    def __init__(self, manufacturer, model, release, big_scan_format):
        super().__init__(manufacturer, model, release)
        self.big_scan_format = big_scan_format
        self.name = (self._manufacturer, self._model, self._release)
        self.param = [self.big_scan_format]
        self.data[self.name] = self.param

    def __str__(self):
        return f'{self.data}'


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, release, max_scan_resolution, scan_speed):
        super().__init__(manufacturer, model, release)
        self.max_scan_resolution = max_scan_resolution
        self.scan_speed = scan_speed
        self.name = (self._manufacturer, self._model, self._release)
        self.param = [self.max_scan_resolution, self.scan_speed]
        self.data[self.name] = self.param

    def __str__(self):
        return f'{self.data}'


p1 = Printer('HP', 'LaserJet Pro M15w', 2020, 'Color', 'A4', 18)
print(p1)
x1 = Xerox('Canon', 'FC128', 2015, 'No big format')
print(x1)
s1 = Scanner('Brother', 'ADS-2200', 2021, '1200x1200 dpi', 35)
print(s1)

