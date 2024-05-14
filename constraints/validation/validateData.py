def validateData(sched, sch):

    #print(sch)

    total = len(sched)
    cnt = 0

    for s in sched:
        if s[sch]==True: 
            cnt = cnt + 1
    
    if cnt >= total:
        return True
    else:
        return False