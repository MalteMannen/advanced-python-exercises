number = 10
numbers = []
my_dict = {}
def a(number):
    while number != 1:
        if number % 2 == 0:
            #even
            number = number // 2
            numbers.append(number)
        else:
            #odd
            number = 3 * number + 1
            numbers.append(number)
    return number
print(a(number))
print(len(numbers))
print(numbers)