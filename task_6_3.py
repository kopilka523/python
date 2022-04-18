def length_check(list1, list2):
    while True:
        if len(list1) > len(list2):
            list2.append('None\n')
            return list1, list2
        elif len(list1) < len(list2):
            return 1


def open_users():
    with open('users.csv', 'r', encoding='utf-8') as f:
        full_name_list = f.readlines()
        for i, full_name in enumerate(full_name_list):
            full_name_list[i] = full_name.replace(',', ' ').replace('\n', '')
        return full_name_list


def open_hobby():
    with open('hobby.csv', 'r', encoding='utf-8') as f:
        user_hobby_list = f.readlines()
        for i, user_hobby in enumerate(user_hobby_list):
            user_hobby_list[i] = user_hobby.replace(',', ', ')
            return user_hobby_list


def write_users():
    with open('users_hobby.txt', 'a', encoding='utf-8') as f:
        full_name_list, user_hobby_list = length_check(open_users(), open_hobby())
        users_hobby = dict(zip(full_name_list, user_hobby_list))
        for key, val in users_hobby.items():
            f.write(f'{key}: {val}')


write_users()
