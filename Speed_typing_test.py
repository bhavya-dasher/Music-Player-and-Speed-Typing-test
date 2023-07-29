from time import *
import random as ran

#this will show the number of seconds from 1971 till now
print(time())


def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except :
            error = error + 1
    return error

def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_round = round(time_delay,2)
    speed = len(userinput)/ time_round
    return round(speed)
    
if __name__ == "__main__":
    while True:
        check = input(" ready to test : yes / no : ")
        if check == "yes":
        
            test = ["Helo! welcome to speed typing test",
                "Currently you are typing to check your speed Am I right but this will only test your one line typing speed and for improvement you have to practice it everyday."]

            test1 = ran.choice(test)
            print("                                                                        ******* typing speed test *******      ")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Enter : ")
            time_2 = time()

            print("Speed : ", speed_time(time_1, time_2, testinput), "word/sec")
            print("error : ", mistake(test1, testinput))
              
        elif check == "no":
            print("thank you")
            break
        else:
            print("Invalid input")
