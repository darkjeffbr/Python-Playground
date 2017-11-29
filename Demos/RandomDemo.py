import random

def separator():
    print("".center(40, '#'))

print("random.randrange(5)")
print(random.randrange(5))

print("random.randrange(4, 11)")
print(random.randrange(4, 11))

print("random.randrange(4, 11, 3)")
print(random.randrange(4, 11, 3))

print("Get random number in range 0 through 9")
iter = 0
while iter < 10:
    r = random.randint(0, 9)
    print('Iteration %d : %d' % (iter, r))
    iter += 1

separator()

print("Generate a random string from the list of strings")
print(random.choice(['Python', 'C++', 'Java']))

print("Generate a random number from the list of [-1, 1, 3.5, 7, 15]")
print(random.choice([-1, 1, 3.5, 7, 15]))

print("Generate a random number from a uniformly distributed tuple")
print(random.choice(((1.1, -5, 6, 4, 7))))

print("Generate a random char from a string")
print(random.choice("Learn Python Programming"))

separator()

print('Select any three chars from a string')
print(random.sample('Python', 3))

print('Randomly select a tuple of three elements from a base tuple')
print(random.sample((21, 12, -31, 24, 65, 16.3), 3))

print('Randomly select a list of three elements from a base list')
print(random.sample((21, 12, -31, 24, 65, 16.3), 3))

print('Randomly select a subset of size three elements from a given set of numbers')
print(random.sample({21, 12, -31, 24, 65, 16.3}, 3))

print('Randomly select a subset of size three elements from a given set of strings')
print(random.sample({'Python', 'C++', 'Java', 'Go'}, 3))

separator()

print('Generate a floating-point pseudo-random number between 0 and 1')
print(random.random())

print('Generate random number in a range')
print(random.uniform(5, 10))