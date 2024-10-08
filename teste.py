import string
import random

def random_generator(size=1):
    return ''.join(random.choice(chars) for _ in range(size))

print(random_generator()) # M4ICUV
print(random_generator()) # 76QUM7