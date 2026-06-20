first_name = 'Flynn'
last_name = 'Wensley'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'. format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'. format(a, b, a + b))
print('{} - {} = {}'. format(a, b, a - b))
print('{} * {} = {}'. format(a, b, a * b))
print('{} / {} = {:.2f}'. format(a, b, a / b))
print('{} % {} = {}'. format(a, b, a % b))
print('{} // {} = {}'. format(a, b, a // b))
print('{} ** {} = {}'. format(a, b, a ** b))

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with radius {} is {:.2f}.'. format(radius, area)
print(formated_string)

print(f' {a} + {b} = {a + b}')
print(f' {a} - {b} = {a - b}')
print(f' {a} * {b} = {a * b}')
print(f' {a} / {b} = {a / b:.2f}')
print(f' {a} % {b} = {a % b}')
print(f' {a} // {b} = {a // b}')
print(f' {a} ** {b} = {a ** b}')