import random
import string
#encode
def encode(word):
    if len(word)>=3:
        word=word[1:]+word[0]
        randomLetter = random.choice(string.ascii_letters)
        word=randomLetter+word+randomLetter
        return word
    else:
        word=word[::-1]
        return word

#decode
def decode(word,temp):
    if len(temp)<3:
        word=temp[::-1]
    else:
        list1=[]
        for i in word:
            list1.append(i)
        del list1[0]
        del list1[-1]
        list1.insert(0,list1[-1])
        list1.pop()
        word=""
        for i in list1:
             word+=i
    return word
        
word=input("Enter the string : ")
temp=word
while True:
    y=int(input("Enter your choice 1.EC 2.DC: "))
    if y==1:
            word=encode(word)
            print(word)
    if y==2:
            print(decode(word,temp))        
    if y==3:
            exit(0)