import random
import time

Inputlist1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Inputlist2 = Inputlist1 + ['0','1','2','3','4','5','6','7','8','9','²']
Inputlist3 = Inputlist2 + ['&','é','"',"'",'(','-','è','_','ç','à',')','=','^','$','ù','*','<',',',';',':','!']

Easysetting = (Inputlist1,5,10,(1,3),(8,14))
Normalsetting = (Inputlist2,10,5,(3,5),(12,18))
Hardsetting = (Inputlist3,25,1,(5,7),(16,22))

def callobjects(currentobject,timer):
    print(currentobject,timer)


def setobject(Difficulty):
    timer = 1
    inputlist = Difficulty[0]
    percentbomb = Difficulty[1]
    percentice = Difficulty[2]
    inuseinput = []
    for loop in range(1000):
        currentobject = []
        objecttype = random.randint(1,100)
        if objecttype <= percentbomb:
            currentobject += ["Bomb"]
        elif 100 - percentice < objecttype <= 100:
            currentobject += ["Ice"]
        else:
            currentobject += ["Fruit"]
#        while True:
        objectletter = random.choice(inputlist)
#            if not objectletter in inuseinput:
        currentobject += [objectletter]
#                inuseinput += [objectletter]
#                break
        callobjects(currentobject,timer)
        time.sleep(timer)
        if not timer <= 0.2:
            timer -= 0.005

setobject(Easysetting)
