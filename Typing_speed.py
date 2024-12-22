from time import *
import random as r

def mistakes(para_test,user_test):
    error=0
    for i in range(len(para_test)):
        try:
            if para_test[i] != user_test[i]:
                error+=1
        except:
            error+=1
    return error

def time_spent(time_s,time_e,userdata):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    type_speed=len(userdata)/time_R
    return round(type_speed)
                


test= ["My name is John", "I am 25 years old", "I am a software engineer"
      ,"i Play cricket","I am a fast bowler"]

test1=r.choice(test)
print("***** Type Here *****")
print(test1)
print()

start_t=time()
type_input=input("Enter ")
end_t=time()

print("Speed",time_spent(start_t,end_t,type_input),"W/s")
print("Mistakes",mistakes(test1,type_input))
