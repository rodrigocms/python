#Useful Functions for Lists I
#len() #returns how many elements are in a list.
#max() #returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number. The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically. This works because the the max function is defined in terms of the greater than comparison operator. The max function is undefined for lists that contain elements from different, incomparable types.
#min() #returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.
#sorted() #returns a copy of a list in order from smallest to largest, leaving the list unchanged.
#sorted() #returns a copy of a list in order from smallest to largest, leaving the list unchanged.
#print(sorted(sizes, reverse=True))   # decrecente

#--- Join
new_str = "\n".join(["fore", "aft", "starboard", "port"])   # print each item in a new line 
#print(new_str)

new_str2 = "-".join(["fore", "aft", "starboard", "port"])   # insert '-' to join itens
#print(new_str2)

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))                            # Join and Sorting ***

#---- Append
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

