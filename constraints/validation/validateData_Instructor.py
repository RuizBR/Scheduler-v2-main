def validateData_Instructor(sched,name,sb):

    for s in sched:
        if s['instructor']==name:
            if s['day1']==sb['day1'] and s['day1'] != None:

                t1 = sb['timeA1']
                t2 = sb['timeA2']

                ta1 = s['timeA1']
                ta2 = s['timeA2']

                if t1>=ta1 and t1<ta2:                
                    return False
            
                if t2>ta1 and t2<=ta2:                
                    return False
            
            if s['day2']==sb['day2'] and s['day2'] != None:

                t1 = sb['timeB1']
                t2 = sb['timeB2']

                ta1 = s['timeB1']
                ta2 = s['timeB2']

                if t1>=ta1 and t1<ta2:                
                    return False
            
                if t2>ta1 and t2<=ta2:                
                    return False
            
            if s['day3']==sb['day3'] and s['day3'] != None:

                t1 = sb['timeC1']
                t2 = sb['timeC2']

                ta1 = s['timeC1']
                ta2 = s['timeC2']

                if t1>=ta1 and t1<ta2:                
                    return False
            
                if t2>ta1 and t2<=ta2:                
                    return False
    
    return(True)
