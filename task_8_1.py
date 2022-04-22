import re


def email_parse(*args):
    for arg in args:
        my_parser = re.compile(r'(?P<username>[\w._-]+)@(?P<domain>\w+\.\w+)')
        user_email_parse = my_parser.match(arg)
        if user_email_parse:
            print(user_email_parse.groupdict(arg))
        else:
            msg = f'wrong email: {arg}'
            raise ValueError(msg)


email_parse('tomilov.alex@gmail.com',
            'A.Tomilov@tatar.ru')
