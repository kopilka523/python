import os
import shutil
from task_7_1 import dir_create


def templates_collecting():
    template_dir = 'my_project/templates'
    os.makedirs(template_dir)
    for root, dirs, files in os.walk('my_project'):
        for f in files:
            if f.rsplit('.', maxsplit=1)[-1] == 'html':
                src = os.path.join(template_dir, root.rsplit('\\')[-1])
                dst = os.path.join(root, f)
                if not os.path.exists(src):
                    os.makedirs(src)
                try:
                    shutil.copy(dst, src)
                except shutil.SameFileError:
                    pass


def create_files(*args):
    dir_create('my_project',
               'settings',
               'mainapp/templates/mainapp',
               'adminapp',
               'authapp/templates/authapp')

    for arg in args:
        with open(arg, 'x', encoding='utf-8') as f:
            pass

    templates_collecting()

    for root, dirs, files in os.walk('my_project'):
        print(f'{root}, папок: {len(dirs)}, файлов: {len(files)}')


if __name__ == '__main__':
    create_files('my_project/settings/__init__.py',
                 'my_project/settings/dev.py',
                 'my_project/settings/prod.py',
                 'my_project/mainapp/__init__.py',
                 'my_project/mainapp/models.py',
                 'my_project/mainapp/views.py',
                 'my_project/mainapp/templates/mainapp/base.html',
                 'my_project/mainapp/templates/mainapp/index.html',
                 'my_project/authapp/__init__.py',
                 'my_project/authapp/models.py',
                 'my_project/authapp/views.py',
                 'my_project/authapp/templates/authapp/base.html',
                 'my_project/authapp/templates/authapp/index.html')
