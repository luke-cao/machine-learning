def get_unique_numbers(number):
    unique_number = []
    for digit in str(number):
        if digit not in unique_number:
            unique_number.append(digit)
    return int(''.join(unique_number))


def main():
    numbers = []
    with open('021_numbers.txt', 'r') as f:
        for number in f:
            number = number.strip()
            number = get_unique_numbers(number)
            numbers.append(number)
    print(*sorted(numbers, reverse=True), sep='\n')


if __name__ == '__main__':
    main()
