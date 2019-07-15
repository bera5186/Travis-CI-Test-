import random
from utility import generate_password


lengths = [8,8,100]
list_of_passwords = generate_password(lengths)
print(list_of_passwords)