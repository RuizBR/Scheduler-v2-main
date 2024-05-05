def validateData(sched, sc):

    for s in sched:
        if s['code'] != sc['code']:
            if s['room1'] == sc['room1'] and s['room1'] != None:
                if s['day1'] == sc['day1'] and s['day1'] != None:
                
                    t1 = sc['timeA1']
                    t2 = sc['timeA2']

                    ta1 = s['timeA1']
                    ta2 = s['timeA2']

                    if t1>=ta1 and t1<=ta2:
                        return False
                    
                    if t2>=ta1 and t2<=ta2:
                        return False
                       
            if s['room2'] == sc['room2'] and s['room2'] != None:
                if s['day2'] == sc['day2'] and s['day2'] != None:
                
                    t1 = sc['timeB1']
                    t2 = sc['timeB2']

                    tb1 = s['timeB1']
                    tb2 = s['timeB2']
                    
                    if t1>=tb1 and t1<=tb2:
                        return False
                    
                    if t2>=tb1 and t2<=tb2:
                        return False
            
            if s['room3'] == sc['room3'] and s['room3'] != None:
                if s['day3'] == sc['day3'] and s['day3'] != None:
                
                    t1 = sc['timeC1']
                    t2 = sc['timeC2']
                    
                    tc1 = s['timeC1']
                    tc2 = s['timeC2']
                    
                    if t1>=tc1 and t1<=tc2:
                        return False
                    
                    if t2>=tc1 and t2<=tc2:
                        return False
    return True