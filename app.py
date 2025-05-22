from fastapi import FastAPI, HTTPException
from models import Profile
from data import profiles, get_profile_by_id

app = FastAPI()

@app.get("/profiles")
def list_profiles():
    return profiles

@app.post("/profiles")
def create_profile(profile: Profile):
    profiles.append(profile)
    return profile

@app.get("/profiles/{profile_id}")
def get_profile(profile_id: int):
    profile = get_profile_by_id(profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@app.delete("/profiles/{profile_id}")
def delete_profile(profile_id: int):
    profile = get_profile_by_id(profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    profiles.remove(profile)
    return {"message": "Deleted"}

@app.get("/profiles/skills")
def list_by_skills():
    skills = {}
    for p in profiles:
        for skill in p.skills:
            skills.setdefault(skill.lower(), []).append(p)
    return skills
