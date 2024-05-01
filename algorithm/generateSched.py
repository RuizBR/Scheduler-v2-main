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
                sc['scID'] = sid
                sc = createSched(sc,rndRoomLab,rndRoomLec)
                isrand = not validateData(setsSubjectLab, sc)
                if isrand == False:
                    print(sc['code'])
                #     while True:
                #         sc = createSched(sc,rndRoomLab,rndRoomLec)
                #         isrand = not validateData(setsSubjectLab, sc)
                #         if isrand == True:
                #             break
                # if isrand:
                sid=sid+1

        print(setsSubjectLab)
        # print(rm1)
         
        






        




