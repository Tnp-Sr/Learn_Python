'''
[Problem]
rock_paper_scissors game -> user vs com(random) and show score.
'''

import random
### function

def game(user):
    #random com
    result = ""
    d = {"r":"rock","p":"paper","s":"scissors"}
    com = random.choice(list(d.keys()))
    #user vs com
    if user == com:
        result = "tie"
    elif user == "r" and com == "s":
        result = "win"
    elif user == "p" and com == "r":
        result = "win"
    elif user == "s" and com == "p":
        result = "win"
    else:
        result = "lose"
    print("You : {} vs Computer : {} --> You {}".format(d[user],d[com],result))
    #return score
    score = [0,0] #score[user,com]
    if result == "win":
        score = [1,0]
    elif result == "lose":
        score = [0,1]
    else:
        score =[0,0]
    return score


### main
com_score = 0
user_score = 0
while True:
    score = [] #score[user,com]
    user = input("[r]ock, [p]aper, [s]cissors, e[x]it : ").lower()
    if user == "x":
        break
    elif user == "p" or user == "r" or user == "s":
        score = game(user)
        user_score += score[0]
        com_score += score[1]
        print("Score => You {} | Com {}".format(user_score,com_score))
    else : 
        print("---Wrong Answer---")
    print("")