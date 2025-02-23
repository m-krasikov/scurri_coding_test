def sequence_print(start=1, end=101):
    sequence = list(i if i % 3 != 0 and i % 5 != 0 else "Three" * (i % 3 == 0) + "Fine" * (i % 5 == 0) for i in range(start, end))
    for item in sequence:
        print(item)

if __name__ == '__main__':
    sequence_print()
