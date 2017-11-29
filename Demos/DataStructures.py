#Python list syntax
assorted_list = [True, False, 1, 1.1, 1+2j, 'Learn', b'Python']
first_element = assorted_list[0]
print(first_element)

print(assorted_list)
for item in assorted_list:
    print(type(item))

simpleton = ['Learn', 'Pthon', '2']
print('id(simpleton) ',id(simpleton))
print(simpleton)
print('Id simpleton[2] ', id(simpleton[2]))
simpleton[2] = '3'
print('Id simpleton[2] ', id(simpleton[2]))
print('id(simpleton) ',id(simpleton))
print(simpleton)

#Nesting inside a list
nested = [[1,1,1],[2,2,2],[3,3,3]]
print("Nesting inside a list \n")
for items in nested:
    for item in items:
        print(item, end = ' ')

#Slicing a list
print('Slicing a list')
languages=['C', 'C++', 'Python', 'Java', 'Go', 'Angular']
print('languages = ', languages)
print('languages[0:3] = ', languages[0:3])
print('languages[2:] = ', languages[2:])

## --------------------------------------------------------------

#Define tuple
pure_tuple = ()
print(pure_tuple)

#Nested tuples
first_tuple = (3, 4, 5)
second_tuple = ('learn', 'python 3')
nested_tuple = (first_tuple, second_tuple)
print(nested_tuple)

#Repetition in tuples
sample_tuple = ('Python 3', )*3
print("sample_tuple : ",sample_tuple)


#Dictionaries
sample_dict = {'key' : 'value', 'jan':31, 'feb':'28/29', 'mar':31}
print(type(sample_dict))
print(sample_dict)
#Accessing dictionaries elements with keys
print(sample_dict['jan'])
print(sample_dict['feb'])
#Dictionaries methods to access elements
print("Dictionaries methods to access elements")
print(sample_dict.keys())
print(sample_dict.values())
print(sample_dict.items())
#Modifying a dictionary (Add/update/delete)
print('Modifying a dictionary (Add/update/delete)')
print("sample_dict['feb'] = 29")
sample_dict['feb'] = 29
print('sample_dict : ' , sample_dict)
print("sample_dict.update({'apr' : 30, 'key': 'newValue'})")
sample_dict.update({'apr' : 30, 'key': 'newValue'})
print('sample_dict : ' , sample_dict)
print("del sample_dict['key']")
del sample_dict['key']
print('sample_dict : ' , sample_dict)