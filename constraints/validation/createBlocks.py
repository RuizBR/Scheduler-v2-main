def createBlocks(sc, subject):        
    #print('subject: ', subject['code'], ' orig', subject['codeOrig'])

    cc = subject['code']

    i = int(subject['blocks'])
    for j in range(i):
        if j==0:
            subject['code'] = cc + ' (A)'
            subject['blockname']='A'
        if j>=1:
            blk = {
                'currID': subject['currID'],
                'prog': subject['prog'],
                'maj': subject['maj'],
                'myID': subject['myID'],
                'code': subject['code'],
                'description': subject['description'],
                'units': subject['units'],
                'type': subject['type'],
                'codeOrig': subject['codeOrig'],
                'instructor': None,
                'day1': None,
                'day2': None,
                'day3': None,
                'timeA1': 0,
                'timeA2': 0,
                'timeB1': 0,
                'timeB2': 0,
                'timeC1': 0,
                'timeC2': 0,
                'room1': None,
                'room2': None,
                'room3': None,
                'blocks': 0,                
                'blockname': None,
                'isAlreadySch1': False,
                'isAlreadySch2': False,
                'isAlreadySch3': False,
                'isOnline': False,
                'isLabSched': False
            }

            blkname = chr(97 + j).upper()
            blk['blockname'] = str(blkname)
            blk['code'] = cc + f' ({blkname})'  
            sc.append(blk)
