import random
from constraints.validation.validateData import validateData
from constraints.validation.createSched import createSched
from constraints.validation.createBlocks import createBlocks
from constraints.validation.createRoomSchedWithLab import createRoomSchedWithLab
from constraints.validation.createLectureSched import createLectureSched

class generateSched: 
    def __init__(self,program,course,instructor,room,curriculum,sem):
        self.instructor = instructor
        self.curriculum = curriculum
        self.program = program
        self.course = course
        self.room = room
        self.sem = sem

        setsCourse = [c for c in self.course]
        setsCurriculum = [c for c in self.curriculum]

        print('course = ',len(setsCourse))                
        print('curriculum = ',len(setsCurriculum))    

        setsCurriculumAndBlock =[(p['block'], c) for c in self.curriculum for p in self.program if p['program']==c['program'] and p['major']==c['major'] and p['year']==c['year']]        

        print('with blocks = ',len(setsCurriculumAndBlock))

        cnt = 0
        
        for cb in setsCurriculumAndBlock:
            bl = cb[0]

            curr = cb[1]['curriculum']
            cnt = cnt + len(curr)
            for cc in curr:
                cc['blocks']=bl

        print('total curriculum = ',cnt)
        
        setsSubject = [course_code for curriculum in self.curriculum for course_code in curriculum['curriculum']]
        setsTemp = [course_code for curriculum in self.curriculum for course_code in curriculum['curriculum']]
        new = [course_code for curriculum in self.curriculum for course_code in curriculum['curriculum']]
        new.clear()
        setsTemp.clear()
        
        print('total subject (possible with duplicate)= ', len(setsSubject))
        #// Sort by code
        setsSubject.sort(key=lambda x: x['code'])

        #// Removing duplicate entry
        i=0
        del_index=0
        
        sb = [curriculum] * 1
        cnt_dup = 0        
        ch = ''
        for s in setsSubject:
            i = i + 1                                 
            # print(i,' ',s['code'],' id ',s['myID'])
            if ch != s['code']:            
                ch = s['code']                
                setsTemp.append(s)
            
        #// Removing duplicate entry
        
        setsTemp.sort(key=lambda x: x['code'])           
        i = 0        
        for s in setsTemp:
            i = i + 1
            # print(i,' ',s['code'],' id ',s['myID'])    
        
        print('total subject (without duplicate) = ', len(setsTemp))

        setsSched = setsTemp
        setsSubject.clear()

        # print(setsSched)

        #/sets blocks
                
        # setsSched.sort(key=lambda x: x['blocks'])

        # getBlockA = [sc for sc in setsSched if sc['blocks']=='1']
        # if len(getBlockA)>0:
        #     for a in getBlockA:
        #         createBlocks(setsSched,a,'A')
        
                
        # getBlockB = [sc for sc in setsSched if sc['blocks']=='2']
        # if len(getBlockB)>0:            
        #     for a in getBlockB:
        #         if a['blockname']==None:
        #             a['blockname']='A'
        #             a['code'] = a['codeOrig'] + ' (A)'
        #             setsSched.append(a)

        #     for b in getBlockB:
        #         if b['blockname']==None:
        #             b['blockname']='B'
        #             b['code'] = b['codeOrig'] + ' (B)'
        #             setsSched.append(b)
        
        # getBlockD = [sc for sc in setsSched if sc['blocks']=='3']
        # if len(getBlockD)>0:            
        #     for a in getBlockD:                
        #             a['blockname']='A'
        #             a['code'] = a['codeOrig'] + ' (A)'                                                            
        #             a['blocks']=0
        #             setsSched.append(a)                    

        #     for b in getBlockD:                
        #             b['blockname']='B'
        #             b['code'] = b['codeOrig'] + ' (B)'
        #             b['blocks']=0                                                   
        #             setsSched.append(b)                    
            
        #     for c in getBlockD:                
        #             c['blockname']='C'
        #             c['code'] = b['codeOrig'] + ' (C)'                                                            
        #             c['blocks']=0
        #             setsSched.append(c)                                    
        
        # getBlockD = [sc for sc in setsSched if sc['blocks']=='4']
        # if len(getBlockD)>0:            
        #     for a in getBlockD:
        #         a=createBlocks(setsSched,a,'A')
            
        #     for b in getBlockD:
        #         b=createBlocks(setsSched,b,'B')
                        
        #     for c in getBlockD:
        #         c=createBlocks(setsSched,c,'C')
            
        #     for d in getBlockD:
        #         d=createBlocks(setsSched,d,'D')                               
        
        # print('blocks A = ', setsSched.count(''))
        # print('blocks B = ',len(getBlockA))
        # print('blocks D = ',len(getBlockA))
        # print('blocks D = ',len(getBlockD))
        
        t = 0
        
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

        setsSubjectLab = [Subject for Subject in setsSched if Subject['type']=='Laboratory'] 
        setsSubjectLec = [Subject for Subject in setsSched if Subject['type']=='Lecture']

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
            
        print('==================================')
        print('Subject Lecture Only =',len(setsSubjectLec))
        print('Subject with Laboratory (5 units) =',len(setsSubjectLab))        
        print('Total Lab Room =',len(setsRoomLab))
        print('Total Lec Room =',len(setsRoomLec))
        print('==================================')

        random.shuffle(setsSched)
        
        #// 1 Sched for Laboratory
        createRoomSchedWithLab(setsRoomLab,setsSubjectLab,setsSched)

        #// 2 Sched for Lecture
        createLectureSched(setsRoomLec,setsSubjectLec,setsSched)
        createLectureSched(setsRoomLec,setsSubjectLec,setsSched)
        createLectureSched(setsRoomLec,setsSubjectLec,setsSched)

        # #// 3 Sched Lab/Lec
        createLectureSched(setsRoomLec,setsSubjectLab,setsSched)
        createLectureSched(setsRoomLec,setsSubjectLab,setsSched)        

        #// ===========================================
        setsSched.sort(key=lambda x: x['code'])                
        i = 0
        for sc in setsSched:            
            #if sc['type']=='Laboratory' and sc['isLabSched']==True:            
            #if sc['type']=='Laboratory' and sc['isLabSched']==False:
            #if sc['type']=='Lecture':
            if sc['type']=='Laboratory':
                print(sc)
                i=i+1
        print('Total Output = ',i)
        #// ===========================================