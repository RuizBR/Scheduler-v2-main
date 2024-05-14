from constraints.validation.validateData_Instructor import validateData_Instructor
def createInstructor(sched,instructor):

    sched.sort(key=lambda x: x['code'])
    
    for sb in sched:        
        if sb['instructor']==None:
            inssp = []
            for ins in instructor:
                for sp in ins['specialized']:
                    if sp['code']==sb['codeOrig']:
                        teacher_info = {
                            'fname': ins['fname'],
                            'sname': ins['sname'],
                            }
                        inssp.append(teacher_info)                                               
            
            if len(inssp)==1:
                i = inssp[0]
                name = i['fname']+' '+i['sname']                
                if validateData_Instructor(sched,name,sb) == True:
                    sb['instructor'] = name

            if len(inssp)>1:
                for i in inssp:
                    name = i['fname']+' '+i['sname']
                    if validateData_Instructor(sched,name,sb) == True:
                        sb['instructor'] = name
    
        