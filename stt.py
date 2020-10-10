import time
import datetime
from random import randint

words = {
1 : "ablity",
2 : "able",
3 : "about",
4 : "above",
5 : "accept",
6 : "according"

}


app = "Typing Test"
appcenter = app.center(100)
correct = 0
fail = 0

def type():
    print("ola")

print("-=-"*30)
print(appcenter)
print("-=-"*30)

def correct():
    correct += 1
    print("-=-"*30)
    randomword  = randint(1, 20)
    print(words[randomword])
    typedword = input("")

def fail():
    fail += 1
    print("-=-"*30)
    randomword  = randint(1, 20)
    print(words[randomword])
    typedword = input("")

start = str(input("Press (S) to Start ")).upper()

while start in "SsNn":
    if start in "Ss":
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        type = print("Start")
        now = time.gmtime(0)
        end = time.gmtime(60)
        while now != end:
            if now != end:
                randomword  = randint(1, 20)
                print(words[randomword])
                typedword = input("")
                if typedword == words:
                    correct()
                else:
                    fail()
            else:
                break
