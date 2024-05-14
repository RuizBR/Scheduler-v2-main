def validateData_ver2(sched,room,day,code,time1,time2):
        
    #print('Room: ',room, ' day: ',day,' Subject: ',code,' time1: ',time1,' time2: ', time2)

    for s in sched:
        if s['code'] == code:
            #print('code ',code,' vs ',s['code'], ' day: ',day,' vs ',s['day1'],' vs ',s['day2'])
            
            if s['day1']==day and s['day1'] != None:
                #print('Day Conflict 1')
                return False

            if s['day2']==day and s['day2'] != None:
                #print('Day Conflict 2')              
                return False


        if s['code'] != code:            

            if s['room1'] == room and s['room1'] != None:
                if s['day1'] == day and s['day1'] != None:
                
                    t1 = time1
                    t2 = time2

                    ta1 = s['timeA1']
                    ta2 = s['timeA2']

                    if t1>=ta1 and t1<ta2:

                        #print('No Available Room 1')
                        return False
                    
                    if t2>ta1 and t2<=ta2:
                        #print('No Available Room 2')
                        return False
                            
            if s['room2'] == room and s['room2'] != None:
                if s['day2'] == day and s['day2'] != None:
                
                    t1 = time1
                    t2 = time2

                    tb1 = s['timeB1']
                    tb2 = s['timeB2']
                    
                    if t1>=tb1 and t1<tb2:
                        #print('No Available Room 3')
                        return False
                    
                    if t2>tb1 and t2<=tb2:
                        #print('No Available Room 4')
                        return False
                    
            if s['room3'] == room and s['room3'] != None:
                if s['day3'] == day and s['day3'] != None:
                
                    t1 = time1
                    t2 = time2
                    
                    tc1 = s['timeC1']
                    tc2 = s['timeC2']
                    
                    if t1>=tc1 and t1<tc2:
                        #print('No Available Room 5')
                        return False
                    
                    if t2>tc1 and t2<=tc2:
                        #print('No Available Room 6')
                        return False
        
    return True