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

challenge = 'Thirty'
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())
challenge = '\u00B2'
print(challenge.isdigit())

num = '10'
print(num.isnumeric())
num = '\u00BD'
print(num.isnumeric())
num = '10.5'
print(num.isnumeric())

challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result)

challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))
challenge = 'thirty days of python'
print(challenge.split())
challenge = 'thiry, days, of, python'
print(challenge.split(','))

challenge = 'thirty days of python'
print(challenge.title())

challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))
challenge = '30 days of python'
print(challenge.startswith('thirty'))