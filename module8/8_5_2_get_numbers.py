size = 6


def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)  # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers


def print_all_numbers(numbers):
    numsAsString = ' '.join(str(i) for i in numbers)
    print('Numbers: {}'.format(numsAsString))


def print_odd_numbers(numbers):
    # Print all odd numbers
    oddNums = []
    for i in numbers:
        if i % 2 != 0:
            oddNums.append(i)
    oddAsString = ' '.join(str(j) for j in oddNums)
    print('Odd numbers: {}'.format(oddAsString))


def print_negative_numbers(numbers):
    negNums = []
    for i in numbers:
        if i < 0:
            negNums.append(i)
    negAsString = ' '.join(str(i) for i in negNums)
    print('Negative numbers: {}'.format(negAsString))


nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
