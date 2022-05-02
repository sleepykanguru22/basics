students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 

def iterateDictionary2(key,list):
    for item in list:
        print(item[key])
    

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

