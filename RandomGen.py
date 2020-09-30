import random
minValue=1
maxValue=6

while True:
    x=random.randint(minValue, maxValue)
    print(f"Your Random Number between 1 and 6 is:---\n{x}")
    
    roll_again=input("Do you want to generate the random number again:---(y/n)\n")
    if roll_again.lower()=="y":
        continue
    else:
        print("Thanks for using 'The Random Number Generator', See You Again :))")
        break
