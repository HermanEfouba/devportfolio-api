from models import Profile

profiles = []

def get_profile_by_id(pid: int):
    for p in profiles:
        if p.id == pid:
            return p
    return None
