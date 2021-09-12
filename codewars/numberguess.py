import sys,random
while True:
    number = int(input("Guess the number: "))
    r=random.randint(1, 5)
    print(r)
    print("num",number)
    if number == r:
        print("you're Genius!! Well done")
        break
    else:
        continue