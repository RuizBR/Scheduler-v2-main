import random
def createSched(sc, rndRoomLab, rndRoomLec, cnt):

    if sc['type']=='Laboratory':
        tstart=3
        tend=2
    if sc['type']=='Lecture':
        tstart=2
        tend=1

    tm = [7,8,9,10,11,12,13,14,15,16]
    t1 = random.choice(tm)
    sc['timeA1']=t1
    sc['timeA2']=t1 + tstart
    sc['timeB1']=t1
    sc['timeB2']=t1 + tend

    dy = ['M','T','W','TH','F']
    dn = [0,1,2,3,4]
    d1 = random.choice(dn)

    sc['day1']=dy[d1]
    d2 = d1 + 2
    if d2 >4: 
        d2 = 0
    sc['day2'] = dy[d2]

    if sc['type']=='Laboratory':
        rm1 = random.choice(rndRoomLab)
        sc['room1'] = rm1
    else:
        rm1 = random.choice(rndRoomLec)
        sc['room1'] = rm1

    rm2 = random.choice(rndRoomLec)
    if (cnt<3):
        sc['room2'] = rm2
    else:
        if sc['type']=='Laboratory':
            rm2 = random.choice(rndRoomLab)
            sc['room2'] = rm2
        else:
            rm2 = random.choice(rndRoomLec)
            sc['room2'] = rm2

    return sc