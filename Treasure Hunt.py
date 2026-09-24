import random
grid=[]
def initialisegrid():
    for i in range(5):
        row=[]
        for i in range(5):
            row.append("_")
        grid.append(row)
    for i in grid:
        print(i)
initialisegrid()
treasurerow=0
treasurecolumn=0
def placetreasure():
    global treasurerow,treasurecolumn
    treasurerow=random.randint(0,4)
    treasurecolumn=random.randint(0,4)
placetreasure()
attempts=0
for i in range(5):
    attempts=attempts+1
    guessrow=int(input("Guess the row number from 0,4"))
    guesscolumn=int(input("Guess the column number from 0,4"))
    if treasurerow > guessrow:
        print("Move Down")
    elif treasurerow < guessrow:
        print("Move Up")
    else:
        if treasurecolumn > guesscolumn:
            print("Move Right")
        elif treasurecolumn < guesscolumn:
            print("Move Left")
        else:
            print("You have found the Treasure in {} attempts!".format(attempts))
            break
         
        
    
