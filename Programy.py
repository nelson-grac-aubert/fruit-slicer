import random
import time

Inputlist1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Inputlist2 = Inputlist1 + ['0','1','2','3','4','5','6','7','8','9','²']
Inputlist3 = Inputlist2 + ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Inputlist4 = Inputlist3 + ['&','é','"',"'",'(','-','è','_','ç','à',')','=','^','$','ù','*','<','>',',',';',':','!','°','+','¨','£','%','µ','?','.','/','§']
Inputlist5 = Inputlist4 + ['~','#','{','[','|','`','\\','^','@',']','}','¤','€']

def callobjects(currentobject,timer):
    print(currentobject,timer)


def setobject(inputlist):
    timer = 1
    percentbomb = 1000
    percentice = 500
    inuseinput = []
    for loop in range(1000):
        currentobject = []
        objecttype = random.randint(1,10000)
        if objecttype <= percentbomb:
            currentobject += ["Bomb"]
        elif 10000 - percentice < objecttype <+ 10000:
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

setobject(Inputlist4)
