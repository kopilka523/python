import os


def dir_create(d_path, *args):
    try:
        os.mkdir(d_path)
        for arg in args:
            os.makedirs(os.path.join(d_path, arg))
    except FileExistsError:
        if os.path.exists('my_project'):
            os.rename('my_project', 'old_my_project')
            print('Переименована существующая root-папка')
            return dir_create(d_path, *args)


if __name__ == '__main__':
    dir_create('my_project',
               'settings',
               'mainapp/templates/mainapp',
               'adminapp',
               'authapp/templates/authapp')
