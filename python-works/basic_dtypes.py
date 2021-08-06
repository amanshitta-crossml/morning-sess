#!/usr/bin/python3

"""
Description:
	Basic Python Data Types Lists, Tuples and Dict

Usage: python3 <filename.py> 
"""

name_list = ["aman","rahul","Pinkal","yakul","Sourav","pooja","Achin"]

# Iterating through list
print("[+] List\n")
for i in range(len(name_list)):
	print(f"name {i+1} => ",name_list[i])

# List comprehension 

new_names = [name for name in name_list]
print("new_names => ",new_names)

# TODO: list operations
print("\n[-] End List\n")

# Tuple
print("[+] Tuple\n")
graph_initial_point = (1,2)
print("graph_initial_point => ",graph_initial_point)
# TODO : tuple Operations
print("\n[-] End Tuple\n")

print("[+] Dictionary")
# TODO
print("\n[-] End Dictionary\n")
