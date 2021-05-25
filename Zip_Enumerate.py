# Zip and Enumerate
# zip and enumerate are useful built-in functions that can come in handy when dealing with loops.

# ZIP
# zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables. For example, printing

list(zip(['a', 'b', 'c'], [1, 2, 3])) 

#>>> [('a', 1), ('b', 2), ('c', 3)]

# Like we did for range() we need to convert it to a list or iterate through it with a loop to see the elements.

# You could unpack each tuple in a for loop like this.

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
print(letters)  # >>> ('a', 'b', 'c')
print(nums)     # >>> (1, 2, 3)

# This would create the same letters and nums tuples we saw earlier.

# ENUMERATE
# enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop.

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

# This code would output:

0 a
1 b
2 c
3 d
4 e



# ---------- Examples

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here

for l,x,y,z in zip(labels,x_coord,y_coord,z_coord):
   # points.append(l+": "+str(x)+', '+str(y)+', '+str(z))
   points.append("{}: {}, {}, {}".format(*point))


for point in points:
    print(point)


# ----- Exec Create Dictionary

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))

print(cast)


# Exec Create Lists from Dictionary

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here

names , heights = zip(*cast)

print(names)
print(heights)


# use Zip to transpose 4x3 Matrix to 3x4
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
col1,col2,col3 = zip(*data)

data_transpose = (col1,col2,col3 )
# replace with your code
print(data_transpose)



#----- Enumerate
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i , character  in enumerate(cast):
    cast[i] = character+" "+str(heights[i])

print(cast)