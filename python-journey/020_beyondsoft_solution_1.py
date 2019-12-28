from collections import Counter

SURNAMES = ({'张', '李', '欧阳', '赵', '前', '孙'})


def get_surname(name, char_index=1):
    return name[:char_index]


def stats_surname(source_file, dependence):
    with open(source_file, 'r') as f:
        names = f.read().split('\n')
        names.remove('')

        for index, name in enumerate(names):
            # if surname can't be found in SURNAMES constant, maybe the surname is two-charactered
            name = name.strip()
            surname = get_surname(name)
            if surname not in SURNAMES:
                surname = get_surname(name, 2)
            names[index] = surname
    return names


def main():
    surnames = stats_surname('./020_names.txt', SURNAMES)
    for surname, count in Counter(surnames).items():
        print(f'"{surname}"姓出现{count}次')


if __name__ == '__main__':
    main()
