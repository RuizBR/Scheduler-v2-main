import random
def createSched(sc, rndRoomLab, rndRoomLec):

    tm = [7,8,9,10,11,12,13,14,15,16]
    t1 = random.choice(tm)
    sc['timeA1']=t1
    sc['timeA2']=t1 + 3
    sc['timeB1']=t1
    sc['timeB2']=t1 + 2

    dy = ['M','T','W','TH','F']
    dn = [0,1,2,3,4]
    d1 = random.choice(dn)

    rm1 = random.choice(rndRoomLab)
    sc['room1'] = rm1

    cnt = 0
    rm2 = random.choice(rndRoomLec)
    sc['room2'] = rm2
            
    sc['day1']=dy[d1]
    d2 = d1 + 2
    if d2 >4: 
        d2 = 0
    sc['day2'] = dy[d2]

    return sc