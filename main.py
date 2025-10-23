from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

# Mendefinisikan model data menggunakan pydantic agar strukturnya benar
class Scholarship(BaseModel):
    name: str
    country: str
    registration: str
    deadline: str

app = FastAPI() # Instance aplikasi FastAPI

# Membuat dictionary database beasiswa
scholarships = {
    1: Scholarship(name="Beasiswa Mext Hokkaido University 2026", country= "Jepang", registration= "01-10-25", deadline= "04-12-25"),
    2: Scholarship(name="Beasiswa The Chinese University of Hong Kong", country= "Tiongkok", registration= "15-09-25", deadline= "09-03-26"),
    3: Scholarship(name="Beasiswa KAUST 2026", country= "Saudi Arabia", registration= "05-08-25", deadline= "01-10-25")
}

# Membuat endpoint dengan CRUD API

@app.get("/")
def home():
    return {"message": "Welcome to Asah Cita Scholarships Calendar API!"}

@app.get("/scholarships", response_model=Dict[int, Scholarship])
def get_all_scholarships():
    return scholarships

@app.get("/scholarships/{scholarships_id}", response_model=Scholarship)
def get_scholarships_by_id(scholarships_id: int):
    if scholarships_id in scholarships:
        return scholarships[scholarships_id]
    return {"Data": "Not Found"}

@app.post("/scholarships", response_model=Scholarship)
def post_scholarship_by_id(scholarship: Scholarship):
    new_id = max(scholarships.keys()) + 1
    scholarships[new_id] = scholarship
    return scholarship

@app.put("/scholarships/{scholarships_id}", response_model=Scholarship)
def update_scholarships_by_id(scholarships_id: int, updated_scholarships: Scholarship):
    if scholarships_id not in scholarships:
        return {"Data": "Not Found"}
    scholarships[scholarships_id] = updated_scholarships
    return updated_scholarships

@app.delete("/scholarships/{scholarships_id}")
def delete_scholarship(scholarships_id: int):
    if scholarships_id not in scholarships:
        return {"Data": "Not Found"}
    del scholarships[scholarships_id]
    return {"message": "Data successfully removed"}
