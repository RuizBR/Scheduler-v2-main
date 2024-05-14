import random
import uuid
import base64
from constraints.validation.validateData import validateData
from constraints.validation.validateData_ver2 import validateData_ver2
from constraints.validation.createSched import createSched
from constraints.validation.createBlocks import createBlocks
from constraints.validation.createDataSched import createDataSched
from constraints.validation.createInstructor import createInstructor

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

        print('no. course = ',len(setsCourse))                
        print('no. curriculum = ',len(setsCurriculum))    

        # and p['semester']==c['semester']

        setsCurriculumAndBlock =[(p['block'], c) for c in self.curriculum for p in self.program if p['program']==c['program'] and p['major']==c['major'] and p['year']==c['year'] and p['semester']==c['semester']]                

        print('no. programs = ',len(setsCurriculumAndBlock))                

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
        setsTemp.clear()
        # setsSched = [course_code for curriculum in self.curriculum for course_code in curriculum['curriculum']]        
        # setsSched.clear()        
        
        print('total subject (1st screening)= ', len(setsSubject))
        #// Sort by code
        setsSubject.sort(key=lambda x: x['code'])

        #// Removing duplicate entry
        i=0
        del_index=0
        
        sb = [curriculum] * 1
        cnt_dup = 0        
        ch = ''
        currID = ''
        prog = ''
        maj = ''
        for s in setsSubject:
            i = i + 1                                 
            #print(i,' ',s['code'],' id ',s['myID'], ' currID ', s['currID'],' prog ',s['prog'],' maj ',s['maj'], ' codeOrig ',s['codeOrig'])
            if ch != s['code']:            
                ch = s['code']
                currID = s['currID']
                prog = s['prog']
                maj = s['maj']
                setsTemp.append(s)                

            if ch == s['code']:
                if currID != s['currID'] or prog != s['prog'] or maj != s['maj']:
                    cc = str(uuid.uuid4())
                    s['myID']=cc
                    s['code']=s['codeOrig'] +'-'+ cc[:8]
                    #print(s['code'])
                    setsTemp.append(s)            

        print('total subject (finale screening) = ', len(setsTemp))

        #// Removing duplicate entry                                

        #// Create Blocks ===============================
        
        setsTemp.sort(key=lambda x: x['code'])
        for b in setsTemp:
            no_blk = int(b['blocks'])
            if no_blk>1:
                #print('blocks ',b['code'],' = ',no_blk)
                createBlocks(setsTemp,b)
        #// Create Blocks ===============================

        # for t in setsTemp:
        #     print(t['code'],' blocks = ',t['blockname'])

        setsSched = setsTemp
        setsSubject.clear()
                
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

        #/================================================
        #/ Teacher Assignment
        # for s in setsSched:
        #     for t in setsTeacher:                
        #         for sp in t['specialized']:
        #             if sp['code']==s['codeOrig']:                        
        #                 if s['instructor']==None:
        #                     s['instructor']=t['fname']+' '+t['sname']                        
        #/================================================       

        setsSubjectLab = [Subject for Subject in setsSched if Subject['type']=='Laboratory'] 
        setsSubjectLec = [Subject for Subject in setsSched if Subject['type']=='Lecture']

        setsRoomLab = [room for room in self.room if room['type']=='Laboratory'] 
        setsRoomLec = [room for room in self.room if room['type']=='Lecture']
        setsRoomAll = [room for foom in self.room]
        

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
        
        # // 1 Sched for Laboratory Once
        sch='isAlreadySch1'
        while validateData(setsSubjectLab,sch)==False:
            cnt = createDataSched(setsRoomLab,setsSubjectLab,setsSched,sch)
            if cnt <=0:                
                break
        
        sch='isAlreadySch2'
        while validateData(setsSubjectLab,sch)==False:
            cnt = createDataSched(setsRoomLab,setsSubjectLab,setsSched,sch)
            if cnt <=0:                
                break
        
        sch='isAlreadySch3'
        while validateData(setsSubjectLab,sch)==False:
            cnt = createDataSched(setsRoomLab,setsSubjectLab,setsSched,sch)
            if cnt <=0:                
                break

        # # # # #// 2 Sched for Lecture
        sch='isAlreadySch1'
        while validateData(setsSubjectLab,sch)==False:
            cnt = createDataSched(setsRoomLec,setsSubjectLec,setsSched,sch)
            if cnt <=0:                
                break
        
        sch='isAlreadySch2'
        while validateData(setsSubjectLab,sch)==False:
            cnt = createDataSched(setsRoomLec,setsSubjectLec,setsSched,sch)
            if cnt <=0:                
                break
        
        sch='isAlreadySch3'
        while validateData(setsSubjectLab,sch)==False:
            cnt = createDataSched(setsRoomLec,setsSubjectLec,setsSched,sch)
            if cnt <=0:                
                break

        #// ===========================================
        createInstructor(setsSched,setsTeacher)
        #// ===========================================

        # days = ['M','T','W','TH','F']

        # for rm in setsRoomLab:
        #     print('Room: ',rm['name'])
        #     for dy in days:
        #         print('day: ',dy)
        #         for sc in setsSched:
        #             if sc['day1']==dy:
        #                 print(sc)

        setsSched.sort(key=lambda x: x['code'])                
        i = 0        
        for sc in setsSched:   
            print(sc)         
            #if sc['type']=='Laboratory' or sc['type']=='Lecture':
            #if sc['type']=='Laboratory' and sc['isLabSched']==True:            
            #if sc['type']=='Laboratory' and sc['isLabSched']==False:
            #if sc['type']=='Lecture':
            #if sc['type']=='Laboratory':
                
                # dd = ''
                # if sc['day1']!=None:
                #     dd = dd +'room: '+sc['room1']+' ('+sc['day1']+' '+str(sc['timeA1'])+'-'+str(sc['timeA2'])+')'
                # if sc['day2']!=None:
                #     dd = dd +'room: '+sc['room2']+' ('+ sc['day2']+' '+str(sc['timeB1'])+'-'+str(sc['timeB2'])+')'
                # if sc['day3']!=None:
                #     dd = dd +'room: '+sc['room3']+' ('+ sc['day3']+' '+str(sc['timeC1'])+'-'+str(sc['timeC2'])+')'

                #print(sc['code'],' schedule: ',dd,' instructor: ',sc['instructor'],' type: ',sc['type'],' major: ',sc['maj'],' prog: ',sc['prog'])                
                #print(sc['code'],' schedule: ',dd,' instructor: ',sc['instructor'],' type: ',sc['type'])
                #print(sc['code'])
                #print(sc['instructor'],' ',dd)                
                #i=i+1

        #print('Total Output = ',i)        
        
        #==== Check By Room
        # setsSched.sort(key=lambda x: x['code'])
        # rm = 'CL3'
        # print('====================')
        # print('Room: ',rm)
        # for sc in setsSched:            
        #     if sc['room1'] == rm or sc['room2'] == rm or sc['room3'] == rm:
        #         dd = ''
        #         if sc['day1']!=None:
        #             dd = dd +'room: '+sc['room1']+' ('+sc['day1']+' '+str(sc['timeA1'])+'-'+str(sc['timeA2'])+')'
        #         if sc['day2']!=None:
        #             dd = dd +'room: '+sc['room2']+' ('+ sc['day2']+' '+str(sc['timeB1'])+'-'+str(sc['timeB2'])+')'
        #         if sc['day3']!=None:
        #             dd = dd +'room: '+sc['room3']+' ('+ sc['day3']+' '+str(sc['timeC1'])+'-'+str(sc['timeC2'])+')'
        #         print(sc['code'],' schedule: ',dd,' instructor: ',sc['instructor'],' type: ',sc['type'])
        # #==== Check By Room

        # #==== Check By Instructor
        # #setsSched.sort(key=lambda x: x['day1'])
        # rm = 'Prof 7'
        # print('====================')
        # print('Instructor: ',rm)
        # for sc in setsSched:            
        #     if sc['instructor'] == rm:
        #         dd = ''
        #         if sc['day1']!=None:
        #             dd = dd +'room: '+sc['room1']+' ('+sc['day1']+' '+str(sc['timeA1'])+'-'+str(sc['timeA2'])+')'
        #         if sc['day2']!=None:
        #             dd = dd +'room: '+sc['room2']+' ('+ sc['day2']+' '+str(sc['timeB1'])+'-'+str(sc['timeB2'])+')'
        #         if sc['day3']!=None:
        #             dd = dd +'room: '+sc['room3']+' ('+ sc['day3']+' '+str(sc['timeC1'])+'-'+str(sc['timeC2'])+')'
        #         print(sc['code'],' schedule: ',dd)
        # #==== Check By Instructor