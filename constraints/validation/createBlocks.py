def createBlocks(sc,subject,ch):        

    blk = subject
    
    blk['blockname']=ch
    blk['code'] = subject['codeOrig'] + ' ('+ch+')'                                                            
    blk['blocks']=0

    sc.append(blk)

    return blk