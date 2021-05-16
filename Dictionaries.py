#Dictionaries And Identity Operators
#Dictionaries
#A dictionary is a mutable data type that stores mappings of unique keys to values. Here's a dictionary that stores elements and their atomic numbers.

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
#Dictionaries can have keys of any immutable type, like integers or tuples, not just strings. It's not even necessary for every key to have the same type! We can look up values or insert new values in the dictionary using square brackets that enclose the key.

print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
#We can check whether a value is in a dictionary the same way we check whether a value is in a list or set with the in keyword. Dicts have a related method that's also useful, get. get looks up values in a dictionary, but unlike square brackets, get returns None (or a default value of your choice) if the key isn't found.

print("carbon" in elements)
print(elements.get("dilithium"))
#>>> True
#>>> None

#Carbon is in the dictionary, so True is printed. Dilithium isn’t in our dictionary so None is returned by get and then printed. If you expect lookups to sometimes fail, get might be a better tool than normal square bracket lookups because errors can crash your program.

# Identity Operators
# Keyword	    Operator
# is	        evaluates if both sides have the same identity
# is not	    evaluates if both sides have different identities

#-------------------------


#Data Structure	Ordered	Mutable	    Constructor	        Example
#List	        Yes	    Yes	        [ ] or list()	    [5.7, 4, 'yes', 5.7]
#Tuple	        Yes	    No	        ( ) or tuple()	    (5.7, 4, 'yes', 5.7)
#Set	        No	    Yes	        {}* or set()	    {5.7, 4, 'yes'}
#Dictionary	    No	    No**	    { } or dict()	    {'Jun': 75, 'Jul': 89}
#* You can use curly braces to define a set like this: {1, 2, 3}. However, if you leave the curly braces empty like this: {} Python will instead create an empty dictionary. So to create an empty set, use set().
#** A dictionary itself is mutable, but each of its individual keys must be immutable.


n = elements.get("dilithium")
print(n is None)
print(n is not None)
#>>> True
#>>> False

#------------------ Get x []   - Prioritize Get ( Avoid code to break)


elements['dilithium']
# >>> KeyError: 'dilithium'
elements.get('dilithium')
# >>> None
elements.get('kryptonite', 'There\'s no such element!')
# >>> "There's no such element!" 


#-------- Include info in dictionary
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}


elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True 


#---------- Sort Dictionary Keys
sorted_keys = sorted(list(verse_dict.keys()))       # create a list with the doctionary keys


#---------- Find the element with the highest value in the list of keys
print(max(verse_dict.values())) 

