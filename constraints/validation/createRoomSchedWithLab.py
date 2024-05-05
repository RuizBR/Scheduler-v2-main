import random
from constraints.validation.validateData import validateData

def createRoomSchedWithLab(room,subject,sc):
    
    days = ['M','T','W','TH','F','Sat']

    maxhours_perday = 12

    totalLabRoom = len(room)
    totalHours = len(room) * len(days) * maxhours_perday
    totalH = 0
    totalSubject = len(subject)
    counter = 0

    tm1 = 0
    tm2 = 0
    tm3 = 0

    ttime = 0
    tstart = 7
        
    rm_no = ''

    random.shuffle(subject)

    cnt = 0

    for rm in room:
        ttime = 0
        tstart = 7

        if counter>totalSubject:
                break

        for day in days:

            if counter>totalSubject:
                break                            

            while True:                                

                rndSlot = random.choice(subject)                
                    
                if rndSlot['isLabSched']==False:                                                            

                    if rndSlot['units']=='5':
                        tm1 = 2
                        tm2 = 2
                        tm3 = 1 
                
                    if rndSlot['units']=='3':
                        tm1 = 2
                        tm2 = 1
                        tm3 = 0                        

                    if rndSlot['day1']==None and rndSlot['isAlreadySch1']==False:
                        rndSlot['day1']=day
                        rndSlot['timeA1']=tstart
                        rndSlot['timeA2']=tstart+tm1
                        rm_no = 'room1'
                    else:
                        if rndSlot['day2']==None and rndSlot['day1']!=None and tm2>0 and rndSlot['isAlreadySch2']==False:
                            rndSlot['day2']=day
                            rndSlot['timeB1']=tstart
                            rndSlot['timeB2']=tstart+tm2
                            rm_no = 'room2'
                        else:
                            if rndSlot['day3']==None and rndSlot['day2']!=None and tm3>0 and rndSlot['isAlreadySch3']==False:
                                rndSlot['day3']=day
                                rndSlot['timeC1']=tstart
                                rndSlot['timeC2']=tstart+tm3
                                rm_no = 'room3'

                    if validateData(sc, rndSlot) == True:
                        
                        rndSlot['isLabSched']=True

                        rndSlot[rm_no] = rm
                    
                        if rm_no == 'room1':
                            tstart = tstart + tm1
                            ttime = ttime + tm1
                            rndSlot['isAlreadySch1'] = True                            
                            totalH = totalH + ttime
                            counter = counter + 1

                        if rm_no == 'room2':
                            tstart = tstart + tm2
                            ttime = ttime + tm2
                            rndSlot['isAlreadySch2'] = True                            
                            totalH = totalH + ttime
                            counter = counter + 1

                        if rm_no == 'room3':
                            tstart = tstart + tm3
                            ttime = ttime + tm3
                            rndSlot['isAlreadySch3'] = True                            
                            totalH = totalH + ttime
                            counter = counter + 1

                        break
                    
                    if ttime>maxhours_perday:                        
                        break
                    
                    if counter>totalSubject:
                        break

    print('===================================')
    print('TOTAL LAB Room = ',totalLabRoom)
    print('TOTAL LAB Hours to be consumed (',totalLabRoom,'room x ',maxhours_perday,'hrs x ',len(days),' days) = ',totalHours,' hrs')
    print('TOTAL LAB Subject = ',totalSubject)
    print('TOTAL Max SLOTS Can Produce is (Total Lab Hours / (',maxhours_perday,')Per daily hours ) = ',totalHours / maxhours_perday)
    print('TOTAL SLOTS Sched. Subject Given = ',counter)
    print('===================================')

    return (True)