import random
import string


def text_layout():  # generates 7 random letters
    text = string.ascii_letters
    random_string = ''.join(random.choice(text) for i in range(7))
    return list(random_string)


def num_pass():  # generates 6 random numbers
    num = random.sample(range(0, 9), 6)
    return list(map(str, num))


def symbol():  # chooses a random symbol from list
    symbols = ['!', '@', '#', '%', '&', '*', '(', ')']
    random_symbol = random.choice(symbols)
    return list(random_symbol)


def final_password():
    li = (num_pass()+text_layout()+symbol())
    random.shuffle(li)
    final_string = ''.join(str(i) for i in li)
    return final_string


final_password()
