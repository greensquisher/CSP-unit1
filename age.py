import time
import random
years = input("what is your age")
years = int(years)
print("your are",(int(years)*365),"days old")
print("you are",(int(years)/10),"decades old")
print("you are",(int(years)*52),"weeks old")
print("you are",(int(years)*525600),"minutes old")
time.sleep(2)
print("contributions to society:",(int((random.randint(0,100)/10))))