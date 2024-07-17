import random
import string
#encode
def encode(word):
    if len(word)>3:
        word=word[1:]+word[0]
        randomLetter = random.choice(string.ascii_letters)
        word=randomLetter+word+randomLetter
        return word
    else:
        word=word[::-1]
        
#decode
def decode(word):
    if len(word)<3:
        word=word[::-1]
    else:
        list=[]
        for i in word:
            list.append(i)
            del word[0:4]
            del word[-1:-4]
        word=word[1:]+word[-1]
        
x=input("Enter the Number : ")
y=int(input("Enter your choice 1.EC 2.DC"))
match y:
        case 1:
                print(encode(x))
        case 2:
                print(decode(x))        