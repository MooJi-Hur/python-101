import os

# 절대 경로와 상대 경로

path = ".."

for dir_name, sub_dir_list, file_list in os.walk(path):
    print(dir_name)
    for sub_dir_name in sub_dir_list:
        print(f"\t [d] {sub_dir_name}")
    for file_name in file_list:
        print(f"\t [f] {file_name}")