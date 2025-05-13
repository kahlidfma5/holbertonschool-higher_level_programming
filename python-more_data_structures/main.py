#!/usr/bin/python3
search_replace = __import__('0-search_replace').search_replace

my_list = [1, 2, 3, 2, 4]
new_list = search_replace(my_list, 2, 99)

print("Original list:", my_list)
print("New list:", new_list)
