import random
import string

def generate_password(m):
    allowed_chars = [char for char in string.ascii_letters + string.digits if char not in "lI1oO0"]
    return ''.join(random.choice(allowed_chars) for _ in range(m))

def main(n, m):
    return [generate_password(m) for _ in range(n)]

print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")