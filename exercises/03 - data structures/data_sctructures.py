def is_palindrom(s):
    if s == s[::-1]:
        return True
    else:
        return False
print(is_palindrom("anne"))

my_dict = {'key1': 1, 'key2': 2}
def invert(dict):
    new_dict = {}
    list_of_dict = dict.items()
    for list_dict in list_of_dict:
        print(list_dict[::-1])

print(invert(my_dict))

