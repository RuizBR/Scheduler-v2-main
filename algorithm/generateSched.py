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
        setsInstructor = self.instructor

        # for subs in setsSubject:
        #     for sp in setsInstructor:

        #         if subs['code']==ints['code']:
                    
        #             subs['instructor']=ints['fname']+' '+ints['sname']


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
        
        sid=1
        for sc in setsSubjectLab:
                cs = createSched(sc,rndRoomLab,rndRoomLec,1)
                isrand = not validateData(setsSubjectLab, cs)
                cnt = 1
                if isrand == False:
                    while True:
                        cnt = cnt + 1
                        sc = createSched(sc,rndRoomLab,rndRoomLec,cnt)
                        isrand = not validateData(setsSubjectLab, sc)
                        if isrand == True:
                            break

        print(setsSubjectLab)
        # print(rm1)
         
        






        




