def validateData(sched, sc):

    # if (len(sched)>0):
    #     # if s['code'] != sc['code']
    #     a = len(sched)
    #     print(a)
    # else:
        return True
    x = sched['code'] != sc['code']
    print(x)
    # for s in sched:
    #     if s['code'] != curr['code']:
    #         if s['room1'] == curr['room1'] and s['room1'] != None:
    #             if s['day1'] == curr['day1'] and s['day1'] != None:
                
    #                 c1 = curr['timeA1']
    #                 ta1 = s['timeA1']
    #                 ta2 = s['timeA2']

    #                 if c1>=ta1 and c1<=ta2: 
    #                     return False
                       
    #             if s['room2'] == curr['room2'] and s['room2'] != None:
    #                 if s['day2'] == curr['day2'] and s['day2'] != None:
                
    #                     c2 = curr['timeB1']
    #                     tb1 = s['timeB1']
    #                     tb2 = s['timeB2']

    #                     if c2>=tb1 and c2<=tb2 :
    #                         return False
    # return True