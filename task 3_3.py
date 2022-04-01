def thesaurus(*names):
    our_dict = {}
    for n in names:
        our_dict.setdefault(n[0], [])
        our_dict[n[0]].append(n)
        #our_dict_1.setdefault(n[8], [])
        #our_dict_1[n[8]].append(n)
    return our_dict
print(thesaurus("Иван", "Мария", "Петр", "Илья"))