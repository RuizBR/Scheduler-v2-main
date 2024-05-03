import random
from constraints.validation.validateData import validateData
from constraints.validation.createSched import createSched
class generateSched: 
    def __init__(self,program,course,instructor,room,curriculum,sem):
        self.instructor = instructor
        self.curriculum = curriculum
        self.program = program
        self.course = course
        self.room = room
        self.sem = sem

        setsCurriculum = [c for c in self.curriculum]
        print('curriculum ',len(setsCurriculum))

        setsCurriculumAndBlock =[(p['block'], c) for c in self.curriculum for p in self.program if p['program']==c['program'] and p['major']==c['major'] and p['year']==c['year']]

        print('with blocks ',len(setsCurriculumAndBlock))

        cnt = 0

        for cb in setsCurriculumAndBlock:
            bl = cb[0]

            curr = cb[1]['curriculum']
            cnt = cnt + len(curr)
            for cc in curr:
                cc['blocks']=bl

        print('total curriculum = ',cnt)

        setsSubject = [course_code for curriculum in self.curriculum for course_code in curriculum['curriculum']]

        print('total subject = ', len(setsSubject))

        setsSched = setsSubject

        #/sets blocks
        for s in setsSched:
            if int(s['blocks'])>=1:
                cnt = int(s['blocks'])

                if cnt>=1:
                    new = [self.curriculum] * 1
                    new = s
                    new['blocks']=0                    
                    new['blockname']='A'
                    new['code'] = s['codeOrig'] + ' (A)'
                    setsSubject.append(new)
                
                if cnt>=2:
                    new = [self.curriculum] * 1
                    new = s
                    new['blocks']=0                    
                    new['blockname']='B'
                    new['code'] = s['codeOrig'] + ' (B)'
                    setsSubject.append(new)
                
                if cnt>=3:
                    new = [self.curriculum] * 1
                    new = s
                    new['blocks']=0                    
                    new['blockname']='C'
                    new['code'] = s['codeOrig'] + ' (C)'
                    setsSubject.append(new)

                if cnt>=4:
                    new = [self.curriculum] * 1
                    new = s
                    new['blocks']=0                    
                    new['blockname']='D'
                    new['code'] = s['codeOrig'] + ' (D)'
                    setsSubject.append(new)                
                
                if cnt>=5:
                    new = [self.curriculum] * 1
                    new = s
                    new['blocks']=0                    
                    new['blockname']='E'
                    new['code'] = s['codeOrig'] + ' (E)'
                    setsSubject.append(new)

        #/sets blocks

        setsSched = setsSubject

        print('No. of slots = ',len(setsSched))

        #/ Total Hours
        hrs = 0
        for sc in setsSched:
            hrs = hrs + int(sc['units'])

        print('total hours = ',hrs)

        setsPrograms = [program for program in self.program]
        print('Programs = ',len(setsPrograms))
        setsTeacher = [teacher for teacher in self.instructor]
        print('Teacher = ',len(setsTeacher))

        for s in setsSched:
            for t in setsTeacher:
                for sp in t['specialized']:
                    if sp['code']==s['codeOrig']:
                        if s['instructor']==None:
                            s['instructor']=t['fname']+' '+t['sname']                

        setsProgramWithBlock = [c for c in self.curriculum for p in self.program if p['program']==c['program'] and p['major']==c['major']]
        setsProgramWithBlock = [p for p in setsPrograms if p['block'] != None]

        # print(setsCurriculumAndBlock)
        # print(len(setsCurriculumAndBlock))        

        setsSubjectLab = [Subject for Subject in setsSubject if Subject['type']=='Laboratory'] 
        setsSubjectLec = [Subject for Subject in setsSubject if Subject['type']=='Lecture']
        setsRoomLab = [room for room in self.room if room['type']=='Laboratory'] 
        setsRoomLec = [room for room in self.room if room['type']=='Lecture'] 
        

        rndRoomLab = [None] * len(setsRoomLab)
        i=0
        for r in setsRoomLab:
            rndRoomLab[i] = r['name']
            i=i+1

        rndRoomLec = [None] * len(setsRoomLec)
        i=0
        for r in setsRoomLec:
            rndRoomLec[i] = r['name']
            i=i+1

        print('Subject: Lab =',len(setsSubjectLab),'Subject: Lec =',len(setsSubjectLec))
        print('Room: Lab =',len(setsRoomLab),'Room: Lec =',len(setsRoomLec))

        random.shuffle(setsSched)
        
        for sc in setsSched:
                cs = createSched(sc,rndRoomLab,rndRoomLec,1)
                isrand = validateData(setsSubject, cs)
                cnt = 1
                if isrand == False:
                    while True:
                        cnt = cnt + 1
                        sc = createSched(sc,rndRoomLab,rndRoomLec,cnt)
                        isrand = validateData(setsSubjectLab, sc)
                        if isrand == True:
                            break

        # for sc in setsSched:
        #     if sc['blockname']=='B':
        #         print(sc)

        # print(setsSubject)
         
        






        




