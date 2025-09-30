initial = int(input("what is the inital number of zombies?"))
rate = int(input("how many people can each zombie infect per day?"))
day = int(input("how many days since the infection began?"))
print((initial+rate)**day)