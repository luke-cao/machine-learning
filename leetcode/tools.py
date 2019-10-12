import os


def change_file_name(folder):
    for src in os.listdir(folder):
        if src.startswith('leetcode_'):
            dst = src.replace('leetcode_', '')
            os.rename(src, dst)


if __name__ == '__main__':
    change_file_name('./')