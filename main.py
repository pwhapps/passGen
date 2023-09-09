import random
import string

class RandomPass:
    def text_layout(self): #generates 7 random letters
        text = string.ascii_letters
        random_string = ''.join(random.choice(text) for i in range(7))
        return list(random_string)
    
    def num_pass(self): #generates 6 random numbers
        num = random.sample(range(0,9),6)
        return list(map(str, num))

    def symbol(self): #chooses a random symbol from list
        symbols = ['!','@','#','%','&','*','(',')']
        random_symbol = random.choice(symbols)
        return list(random_symbol)

    def final_password(self):
        li = (self.num_pass()+self.text_layout()+self.symbol())
        random.shuffle(li)
        final_string = ''.join(str(i) for i in li)
        print(final_string)


RandomPass().final_password()