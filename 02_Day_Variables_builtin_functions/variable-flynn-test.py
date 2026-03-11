print('Hello, World!')
len('Hello, World!')
type('Hello, World and all')
str(10)
float(10)
input('What is your name?')

#practice of what variables are available.
min(20, 30, 40, 50)
max(20, 30, 40, 50)
min([20, 30,40,50])
max([20, 30,40,50])
sum([20, 30,40,50])


#new section to provide data for variables
first_name = 'Flynn'
last_name = 'Wensley'
country = 'Canada'
age = 30
is_married = True
skills = ['Python', 'HTML']
person_info = {
    'firstname': 'Flynn',
    'lastname': 'Wensley',
    'country': 'Canada',
    'age': 30
}

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#multiple variables in one line
first_name, last_name, country, age, is_married = 'Flynn', 'Wensley', 'Canada', 30, True
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

print(type('Flynn'))
print(type(first_name))
print(type(30))
print(type(3.14))
print(type(1 + 1j))

#int to float
num_int = 10
print('num_int:', num_int) #10
num_float = float(num_int)
print('num_float:', num_float) #10.0

#float to int
gravity = 9.81
print(int(gravity)) #9

# int to str
num_int = 10
print(num_int) #10
num_str = str(num_int)
print(num_str) #'10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
num_int = int(num_str) #Convert the string to a float first)
num_int = int(num_float) #Then convert the float to an integer
print('num_int', int(num_str)) #10
print('num_float', float(num_str)) #10.6
num_int = int(num_float)
print('num_int', int(num_int)) #10

#str to list
first_name = 'Flynn'
print(first_name) #Flynn
first_name_to_list = list(first_name)
print(first_name_to_list) #['F', 'l', 'y', 'n', 'n']
