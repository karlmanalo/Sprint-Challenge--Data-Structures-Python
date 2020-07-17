import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n")
print (f"runtime for brute force iteration: {end_time - start_time} seconds\n")

# Brute force iteration runtime: 8.430530786514282 seconds
# Runtime complexity is O(n**2)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# Initializing root node of BST with halfway point of sorted names list. Not sure if sorting
# and getting midpoint to optimize BST is faster for this small of a dataset. Will check
# after this.
# Runtime complexity of the built-in sorted method is O(n * log n)

# Finding midpoint of names_1
midpoint = sorted(names_1)[5000]

# Initializing midpoint as root node of BST
BST = BSTNode(midpoint)

# Removing first instance of midpoint from names_1
names_1.remove(midpoint)

# Inserting the rest of the names into BST
for name in names_1: 
    BST.insert(name)

# Searching BST for duplicates with names from names_2
for name_2 in names_2:
    if BST.contains(name_2): 
        duplicates.append(name_2) 

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n")
print (f"runtime for BST sorted: {end_time - start_time} seconds\n")

# BST sorted runtime: 0.11783480644226074 seconds
# Runtime complexity is O(n * log n)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# Initialize root node of BST with index[0] of list to see what's faster

# Initializing root node of BST as first name in list
BST = BSTNode(names_1[0])

# Adding the rest of the names in names_1 to BST
for name in names_1[1:]: 
    BST.insert(name)

# Searching BST for duplicates with names from names_2
for name_2 in names_2:
    if BST.contains(name_2): 
        duplicates.append(name_2) 

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n")
print (f"runtime for BST_0: {end_time - start_time} seconds\n")

# BST_0 runtime: 0.10802698135375977 seconds
# Runtime complexity is O(n * log n)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = list(set(names_1) & set(names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n")
print (f"runtime for built_in python: {end_time - start_time} seconds\n")

# Built-in Python runtime: 0.003955364227294922 seconds