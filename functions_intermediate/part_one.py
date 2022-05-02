# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 

def order(x):
    temp =x[1][0] + 5
    x[1][0] = temp
    print(x)

order(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def change_last_name(students):
    students[0]['last_name'] = 'Bryant'
    print(students)

change_last_name(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

def change_player(sports_directory):
    sports_directory['soccer'][0] = 'Andres'
    print(sports_directory)

change_player(sports_directory)

# Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
def change_value(z):
    z[0]['y']=30
    print(z)
    
change_value(z)




