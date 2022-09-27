# 1
x = [ [5,2,3], [10,8,9] ]
(x[1][0]) = 15
print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
(students[0]['last_name']) = "Byrant"
print(students[0]["last_name"])


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] += 10
sports_directory["soccer"][0] = 'Andres'
print(z)
print(sports_directory)

# 2
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

interate_dictionary = (students)

for element in interate_dictionary:
    for key, value in element.items():
        print(key, value)

# 3
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

interate_dictionary = (students)

for dic in interate_dictionary:
    print (dic['first_name'])

for dic in interate_dictionary:
    print (dic['last_name'])

#4

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print_info = (dojo)

for key, values in print_info.items():
    print(len(key), key)
    if(isinstance(values, list)):
        for value in values:
            print(value)
    else:
        print(value)
