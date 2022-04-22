import re

with open('nginx_logs.txt', 'r+', encoding='utf-8') as f1:
    for _ in f1:
        row_parser = re.compile(r'(\w*[.:\w]*) - - (\[.*\]) "(\w*) (\/\w*\/\w*) HTTP/1.1" (\d*) (\d*)')
        row_parse = row_parser.match(_).groups()
        print(row_parse)
