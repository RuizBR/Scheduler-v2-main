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

        setsSubject = [course_code for curriculum in self.curriculum for course_code in curriculum['curriculum']]
        setsPrograms = [program for program in self.program]
        setsTeacher = [teacher for teacher in self.instructor]

        for s in setsSubject:
            for t in setsTeacher:
                for sp in t['specialized']:
                    if sp['code']==s['code']:
                        if s['instructor']==None:
                            s['instructor']=t['fname']+' '+t['sname']

        setsProgramWithBlock = [p for p in setsPrograms if p['block'] != None]
        
        if len(setsProgramWithBlock)>0:
            png = [None]
            pAdd = None
            for pb in setsProgramWithBlock:
                if pAdd==None:
                    pAdd = pb['program']
                    png.append(pb['program'])
                if pAdd != pb['program']:
                    png.append(pb['program'])
                    pAdd = pb['program']
            png.pop(0)

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

        random.shuffle(setsSubject)
        
        for sc in setsSubject:
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

        print(setsSubject)
        # print(rm1)
         
        






        




