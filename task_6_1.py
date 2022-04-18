def log_gen():
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        for new_line in f:
            new_line = f.readline().replace('"', '').split()
            yield new_line[0], new_line[5], new_line[6]


print(*list(log_gen())[:50], sep='\n')
