import time
from random import randint

words = {
1 : "ablity",
2 : "able",
3 : "about",
4 : "above",
5 : "accept",
6 : "according",
7 : "account",
8 : "alone",
9 : "agency",
10 : "arm",
11 : "animal",
12 : "air",
13 : "after",
14 : "anyone",
15 : "another",
16 : "apply",
17 : "answer",
18 : "attention",
19 : "around",
20 : "area",
21 : "article",
22 : "available",
23 : "baby",
24 : "back",
25 : "bad",
26 : "bag",
27 : "ball",
28 : "bank",
29 : "bar",
30 : "base",
31 : "beat",
32 : "beautiful",
33 : "become",
34 : "bed",
35 : "before",
36 : "begin",
37 : "between",
38 : "blood",
39 : "bilion",
40 : "buy",
41 : "box",
42 : "build",
43 : "bug",
44 : "call",
45 : "camera",
46 : "campaign",
47 : "cancer",
48 : "capital",
49 : "card",
50 : "car",
51 : "carrer",
52 : "chair",
53 : "center",
54 : "catch",
55 : "close",
56 : "city",
57 : "class",
58 : "company",
59 : "cup",
60 : "control",
61 : "dark",
62 : "day",
63 : "decide",
64 : "death",
65 : "develop",
66 : "detail",
}


app = "Typing Test"
appcenter = app.center(100)


# Globais

actual_word = ""
corrects = 0
fails = 0



def checkWord(word, typed_word):

    if word.strip().lower() == typed_word.strip().lower():
        print("-=-" * 30)
        correct()
    else:
        print("-=-" * 30)
        fail()


def correct():
    global corrects
    corrects += 1

def fail():
    global fails
    fails += 1


def genNewWord():
    randomword = randint(1, 66)
    return words[randomword]

    # typedword = input("")

print("-=-"*30)
print(appcenter)
print("-=-"*30)

print("[A] 30 Seconds ")
print("[B] 1 Minute ")
print("[C] 3 Minute ")


timer = str(input("")).strip().upper()
start = str(input("Press (S) to Start ")).upper()


if start in "Ss":
    if timer in "A":
        typing_time = 30

        print("3")
        time.sleep(1)

        print("2")
        time.sleep(1)

        print("1")
        time.sleep(1)
        print("Start")


        end_time = time.time() + typing_time

        while time.time() < end_time:


            actual_word = genNewWord()
            print(actual_word)
            typed_word = input()


            checkWord(actual_word, typed_word)


        print("Done")
        print(f"{corrects} Words in 30 Seconds")
        print(f"Failed {fails} words ")

    elif timer in "B":

        typing_time = 60

        print("3")
        time.sleep(1)

        print("2")
        time.sleep(1)

        print("1")
        time.sleep(1)
        print("Start")


        end_time = time.time() + typing_time

        while time.time() < end_time:


            actual_word = genNewWord()
            print(actual_word)
            typed_word = input()


            checkWord(actual_word, typed_word)


        print("Done")
        print(f"{corrects} Words in 1 Minute")
        print(f"Failed {fails} words ")

    elif timer in "C":

        typing_time = 180

        print("3")
        time.sleep(1)

        print("2")
        time.sleep(1)

        print("1")
        time.sleep(1)
        print("Start")


        end_time = time.time() + typing_time

        while time.time() < end_time:


            actual_word = genNewWord()
            print(actual_word)
            typed_word = input()


            checkWord(actual_word, typed_word)


        print("Done")
        print(f"{corrects} Words in 30 Seconds")
        print(f"Failed {fails} words ")



else:
    print("Quiting...")
