class Stationary:
    title = 'ручка', 'карандаш', 'маркер'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print(Stationary.title[0])


class Pencil(Stationary):
    def draw(self):
        print(Stationary.title[1])


class Handle(Stationary):
    def draw(self):
        print(Stationary.title[2])


st_obj = Stationary()
st_obj.draw()
pen_obj = Pen()
pen_obj.draw()
pencil_obj = Pencil()
pencil_obj.draw()
handle_obj = Handle()
handle_obj.draw()
