challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

first_name = 'Flynn'
last_name = 'Wensley'
age = 400
job = 'Something'
country = 'Canada'
sentence = f'I am {first_name} {last_name}. I am {age} years old. I work in {job}. I live in {country}.'
print(sentence)

radius = 10
pi = 3.14
area = pi * radius ** 2
result = f'The area of a circle with radius {radius!s} is {area!s}.'
print(result)

challenge = 'thirty days of python'
print(challenge.rindex('on', 8))

challenge = 'ThirtyDaysPython'
print(challenge.isalnum())

challenge = '30DaysPython'
print(challenge.isalnum())

challenge = 'thirty days of python'
print(challenge.isalnum())

challenge = 'thirty days of python 2019'
print(challenge.isalnum())

challenge = 'thirty days of python'
print(challenge.isalpha())
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())
num = '123'
print(num.isalpha())
print(challenge.isdigit())
challenge = '\u00B2'
print(challenge.isdigit())
