language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)
second_last = language[-2]
print(second_last)
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)
final_three = language[-3:]
print(final_three)
end_three = language[3:]
print(end_three)


greeting = 'Hello, World!'
print(greeting[::-1])

pto = language[0:6:2]
print(pto)

challenge = 'thirty days of python'
print(challenge.capitalize())
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))
print(challenge.endswith('on'))
print(challenge.endswith('tion'))
print(challenge.find('y'))
print(challenge.find('th'))
print(challenge.rfind('y'))
print(challenge.rfind('th'))

