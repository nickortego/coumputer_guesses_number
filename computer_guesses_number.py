yes = input('Think of a whole number between 0 and 10 and I will guess it. When you are ready, enter "yes": ')
if yes == 'yes':
	import random
for x in range(1):
    guess = random.randint(0,10)
    print(guess)
    print('Is that correct?')
    print('Too high?')
    y = input('Or too low? ')
if y == 'correct':
    print("Am I great or what?")
    import sys
    sys.exit()


if y == 'too low':
    low = guess
    high = 10
    guess = random.randint(low, high)
if y == 'too high':
    high = guess
    low = 0
    guess = random. randint(low, high)
print(guess)
print('Is that correct?')
print('Too high?')
y = input('Or too low? ')
    
if y == 'correct':
    print("Am I great or what?")
    import sys
    sys.exit() 
	
while y != 'correct':
    if y == 'too low':
        low = guess
        if low != 0 and high != 10:
            guess = random.randint(low + 1, high - 1)
        elif low == 0:
            guess = random.randint(low, high -1)
        elif high == 10:
            guess = random.randint(low + 1, high)
    if y == 'too high':
        high = guess
        if low != 0 and high != 10:
            guess = random.randint(low + 1, high - 1)
        elif low == 0:
            guess = random.randint(low, high -1)
        elif high == 10:
            guess = random.randint(low + 1, high)
        guess = random.randint(low + 1, high - 1)
    print(guess)
    print('Is that correct?')
    print('Too high?')
    y = input('Or too low? ')
    
if y == 'correct':
    print("Am I great or what?")
    import sys
    sys.exit() 
