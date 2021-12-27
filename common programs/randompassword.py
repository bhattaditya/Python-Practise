import secrets
from random import randint

def random_password():
    password = secrets.token_hex(randint(5,10))
    return password

if __name__ == "__main__":
    print(random_password())