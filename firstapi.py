from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


students = {
    1: {
        'name' : 'Sai Win Maung',
        'age' : 12,
        'major' : 'Mechatronics'
    }
}

class Student(BaseModel):
    name : str
    age : int
    major : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional [int] = None
    major : Optional[str] = None
     


@app.get('/get_student/{student_id}')
async def get_student(student_id :int):
    return students[student_id]


@app.get('/get_student_byname/{student_id}')
async def get_byname(name :str, student_id :int):
    for stuent in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {'Data' : 'Not Found'}


@app.post('/create_student/{student_id}')
async def create_student(student_id : int, student : Student):
    if student_id in students:
        return { 'Error' : 'Student has been exist'}
    
    students[student_id] = student
    return students[student_id]


@app.put('/update_student/{student_id}')
async def update_student(student_id : int, student : UpdateStudent):
    if student_id not in  students:
        return { 'Error' : 'Student does not exist'}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age
    if student.major != None:
        students[student_id].major = student.major
    
    return students[student_id]

@app.delete('/delete_student/{student_id}')
async def delete_student(student_id :int):
    if student_id not in students:
        return {'Error' : 'Student does not exist'}
    
    del students[student_id]
    return { "Message" : 'Student Delete Successful'}