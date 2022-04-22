import os
from collections import defaultdict

root_dir = 'some_data'
some_files = defaultdict(int)
labels = [10000, 50000, 100000]
cnt_group_1 = 0
cnt_group_2 = 0
cnt_group_3 = 0

for item in os.scandir(root_dir):
    if item.stat().st_size <= labels[0]:
        cnt_group_1 += 1
    if labels[0] < item.stat().st_size <= labels[1]:
        cnt_group_2 += 1
    if labels[1] < item.stat().st_size <= labels[2]:
        cnt_group_3 += 1

some_files[labels[0]] = cnt_group_1
some_files[labels[1]] = cnt_group_2
some_files[labels[2]] = cnt_group_3
print(some_files)
print('Всего ', len(list(os.scandir(root_dir))))
