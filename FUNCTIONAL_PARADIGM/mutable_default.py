# In Python there are two muttable sequences, these are lists and dictionaries.
# In functions exists the exceptions for default's values of muttable objects. 

def add_to_list(item, list=None):
    if list is None:
        list = []
    list.append(item)
    print(list)

add_to_list(5)
add_to_list(6)
add_to_list(7)
add_to_list(8)

def add_to_dict(key, value, dict=None):
    if dict is None:
        dict = {}
    dict[key] = value
    print(dict)

add_to_dict('name','Alex')
add_to_dict('age', 23)
add_to_dict('address', 'Kyiv')
add_to_dict('telephone', + 123344556)
add_to_dict('PSC', 108939)