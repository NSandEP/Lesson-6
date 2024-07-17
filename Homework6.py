my_dict = {'Artemiy': 1234, 'Svetlana': 5678, 'Viktoria': 9090}
print(my_dict)
print(my_dict['Artemiy'])
print(my_dict.get('Georgiy', 'None'))
my_dict['Anton'] = 5479
my_dict['Dilara'] = 4680
A = my_dict.pop('Svetlana')
print(A)
print(my_dict)
my_set = {1, 2, 3, 1, 3, 'Samurai', 56.29, 34.58}
print(my_set)
my_set.add(5)
my_set.discard(34.58)
print(my_set)
