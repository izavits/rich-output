from rich import print, pretty, inspect

pretty.install()

my_dict = {
    'list1': [1, 2, 3],
    'list2': [4, 5, 6]
}

# Pretty print my_dict and other variables
print(my_dict)
print([1, 2, 3, 4, 5])
print(False, True)

print('')
print('Inspecting my_dict:')
# Inspect my_dict
inspect(my_dict)