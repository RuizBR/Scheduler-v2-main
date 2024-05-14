import random
from constraints.validation.validateData import validateData
from constraints.validation.validateData_ver2 import validateData_ver2

def createDataSched(room,subject,sc,sctime):

    #print(sctime)

    days = ['M','W','F','T','TH']

    orig_timestart = 7
    maxhours_perday = 12

    totalLabRoom = len(room)
    totalHours = len(room) * maxhours_perday
    totalH = 0
    totalSubject = len(subject)

    ideal_subjectperday = round(totalSubject / len(days))
    cntperday = 0

    counter = 0

    tm1 = 0
    tm2 = 0
    tm3 = 0

    ttime = 0
        
    rm_no = ''
    rmname = ''
    curr_day = ''
    codename = ''

    random.shuffle(subject)

    cnt = 0
    tEnd = 0

    for rm in room:
        ttime = 0
        tStart = orig_timestart
        cntperday = 0     

        for day in days:                        

            for sb in subject:

                if ttime > maxhours_perday:
                    break

                if counter > len(subject):
                    break
            
                if cntperday >= ideal_subjectperday:                                           
                    break                                    
                
                if sb[sctime]==False:                                                        

                    if sb['units']=='5':
                        tm1 = 2
                        tm2 = 2
                        tm3 = 1 
                
                    if sb['units']=='3':
                        tm1 = 2
                        tm2 = 1
                        tm3 = 0                        

                    if sb['day1']==None and sb['isAlreadySch1']==False and tm1>0:                            
                        tEnd = tStart+tm1
                        rm_no = 'room1'                            
                    else:
                        if sb['day2']==None and sb['day1']!=None and tm2>0 and sb['isAlreadySch2']==False:                                
                            tEnd = tStart+tm2
                            rm_no = 'room2'
                        else:
                            if sb['day3']==None and sb['day2']!=None and tm3>0 and sb['isAlreadySch3']==False:                                    
                                tEnd = tStart+tm3
                                rm_no = 'room3'
                    
                    rmname = rm['name']
                    codename = sb['code']

                    checking = validateData_ver2(sc,rmname,day,codename,tStart,tEnd)

                    if checking == True:                            

                        sb[sctime]=True
                        counter = counter + 1
                        cntperday = cntperday + 1                            
                    
                        if rm_no == 'room1':                                                         
                            sb['day1']=day
                            sb['timeA1']=tStart
                            sb['timeA2']=tEnd
                            sb['isAlreadySch1'] = True
                            sb['room1']=rmname
                            tStart = tStart + tm1
                            ttime = ttime + tm1
                            
                            

                        if rm_no == 'room2':                                                        
                            sb['day2']=day
                            sb['timeB1']=tStart
                            sb['timeB2']=tEnd
                            sb['isAlreadySch2'] = True                                                        
                            sb['room2']=rmname                            
                            tStart = tStart + tm2
                            ttime = ttime + tm2

                        if rm_no == 'room3':                            
                            sb['day3']=day
                            sb['timeC1']=tStart
                            sb['timeC2']=tEnd
                            sb['isAlreadySch3'] = True
                            sb['room3']=rmname
                            tStart = tStart + tm3
                            ttime = ttime + tm3
                        
                        totalH = totalH + ttime                            
                        

                    # print('Day ',day,' total time per day: ',ttime, ' ideal subject: ',cntperday)
                    

    # print('===================================')
    # print('TOTAL Room = ',totalLabRoom)
    # print('TOTAL Hours to be consumed (',totalLabRoom,'room x ',maxhours_perday,'hrs x = ',totalHours,' hrs')
    # print('TOTAL Subject = ',totalSubject)
    # print('TOTAL SLOTS Sched. Subject Given = ',counter)
    # print('===================================')

    return (counter)