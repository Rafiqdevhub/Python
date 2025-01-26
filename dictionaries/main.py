names={
    "name1":"Sanan",
    "name2":"Khan",
    "name3":"Rafiq",
   
}

print(names)

# print(names.keys()) 

# print(names.values()) 

# print(type(names))

# print(len(names))

# print(names.items())

# print('Khan' in names.values())

# names['name4']='Ali'
# print(names)

# names.update({'name5':'Ahmed'})
# print(names)

# names.pop('name1')
# print(names)

# print(names.popitem())
# print(names)

# del names['name2']
# print(names)

# del names

# new_names=names.copy()
# new_names['name6']='Ahmed'
# print("copies ",new_names)

copies=dict(names)
print('Copies of the dic',copies)


