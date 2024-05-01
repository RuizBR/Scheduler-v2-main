def validateData(sched, sc):

    for s in sched:
        if s['code'] != sc['code']:
            if s['room1'] == sc['room1'] and s['room1'] != None:
                if s['day1'] == sc['day1'] and s['day1'] != None:
                
                    c1 = sc['timeA1']
                    ta1 = s['timeA1']
                    ta2 = s['timeA2']

                    if c1>=ta1 and c1<=ta2:
                        return False
                       
            if s['room2'] == sc['room2'] and s['room2'] != None:
                if s['day2'] == sc['day2'] and s['day2'] != None:
                
                    c2 = sc['timeB1']
                    tb1 = s['timeB1']
                    tb2 = s['timeB2']

                    if c2>=tb1 and c2<=tb2 :
                        return False
    return True