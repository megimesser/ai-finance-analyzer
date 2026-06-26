import fastapi
from fastapi import FastAPI, Path # import von fastapi als objekt
import uvicorn

app = FastAPI()

#Endpoint
#localhost/delete-user 

#GET 
#POST
#PUT
#DELETE

#Endpunkt
@app.get("/")
def index():
    return {"name": "First Data"}




# Startbefehl 
#uvicorn myapi:app --reload


# Swagger UI - Test 
#http://127.0.0.1:8000/docs#/default/index_get


# Endpointparameter 

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}


#google.com/get-student

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="ID of the student you want to watch",ge=0)):
    #try: 
    return students[student_id]   
    #except KeyError:
    #    return "kein Student mit dieser Nummer"


# ge, get,lt,le -> Wieviel Größer oder kleiner müssen die values bei der eingabe sein 
