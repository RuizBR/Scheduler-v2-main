import requests
from flask import Flask, jsonify
from getData.student_data import fetch_student_data
from getData.room_data import fetch_room_data
from getData.teacher_data import fetch_teacher_data
from getData.course_data import fetch_course_data
from getData.curriculum_data import fetch_curriculum_data
from algorithm.generateSched import generateSched

class Scheduler:
    def __init__(self) -> None:
        self.getData()
    
    def getData(self):
        self.programs = fetch_student_data()
        self.courses = fetch_course_data()
        self.instructors = fetch_teacher_data()
        self.rooms = fetch_room_data()
        self.curriculum = fetch_curriculum_data()
        # program_curriculum_data = {}
        # indexed_curriculum = {}
        # for curriculum in self.curriculum:
        #     # print(curriculum)
        #     key = (curriculum['program'], curriculum['major'], curriculum['year'], curriculum['semester'])
        #     indexed_curriculum.setdefault(key, []).extend(curriculum['curriculum'])

        # for student in self.programs:
        #     # print(student)
        #     student_id = student['_id']
        #     key = (student['program'], student['major'], student['year'], student['semester'])
        #     program_curriculum_data[key] = {}
        #     for course in indexed_curriculum.get(key, []):
        #         program_curriculum_data[key][course['code']] = student['block']

        # print(program_curriculum_data)
        generateSched(self.programs, self.courses, self.instructors,self.rooms,self.curriculum,sem = '1st')
       
  
if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    scheduler = Scheduler()
    # scheduler.getData()
    # p = scheduler.CSP()
    # print(p)

    

    