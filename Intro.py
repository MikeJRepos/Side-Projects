#Basic program for beginners

print("\t Welcome! Whats your name?: ")

while True:
    name = input()
    if  len(name.strip()) == 0:
        print("\tYou have to enter your name!")
    else:
        break

print("\tHello " + name + "!")
print("\tAre you ready to learn?")

while True:
    answer = input().lower()
    if answer == "y" or answer == "yes":
        print("\tGreat! Lets get started")
        break
    elif answer == "n" or answer == "no":
        print("\tWell thats just a shame...")
        break
    else:
        print("\tYou have to answer yes or no!")
        
