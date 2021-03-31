import string, random

# alphabets=list(string.ascii_letters)

lowercase_alphabet = list(string.ascii_lowercase)

uppercase_alphabet = list(string.ascii_uppercase)

n = 26

random_lowercase = random.sample(lowercase_alphabet, n)
random_uppercase = random.sample(uppercase_alphabet, n)

print(', '.join(random_lowercase[:5]))
print(', '.join(random_lowercase[5:10]))
print(', '.join(random_lowercase[10:15]))
print(', '.join(random_lowercase[15:20]))
print(', '.join(random_lowercase[20:26]))
print("\n")
print(', '.join(random_uppercase[:5]))
print(', '.join(random_uppercase[5:10]))
print(', '.join(random_uppercase[10:15]))
print(', '.join(random_uppercase[15:20]))
print(', '.join(random_uppercase[20:26]))
