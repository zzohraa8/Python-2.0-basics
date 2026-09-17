import random
birds=["woodpecker","pigeon","toucan","parrot","cardinal","sparrow","pelican","penguin","swan","crow","flamingo","eagle","peacock","hummingbird","robin","mockingbird","albatross","ostrich","turkey","chicken"]
score=0
rounds=1
for i in range(5):
    
    word=random.choice(birds)
    wordlist=list(word)
    random.shuffle(wordlist)
    
    print(" "+str(rounds)+". This is the shuffled word, "+"".join(wordlist))
    hint=input("Do you want a hint? Type yes/no")
    if hint=="yes":
        score=score-0.5
        print ("The first letter of the word is "+word[0])
    answer=input("Enter the original word, ")
    if answer==word:
        print("Your answer is correct")
        score=score+1
    else:
        print("Your answer is incorrect. The correct answer was "+word)
    print("\n")
    rounds=rounds+1
    
    
print("Your score out of 5 is "+str(score))
