import json
from candidate import Candidate

def load_candidates(base):
    with open(base, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def get_all(data):
    arr = []
    for i in data:
        #skills_old = i['skills'].split(',')
        #skills = [skill.strip().lower() for skill in skills_old]
        candidate = Candidate(i['pk'], i['name'], i['position'], i['skills'].lower(), i['picture'])
        arr.append(candidate)
    return arr
def get_by_pk(pk, data):
    for i in data:
        if i.pk == pk:
            return pk
def get_by_skills(skill, data):
    arr = []
    for i in data:
        if skill in i.skills:
            arr.append(i)
    return arr
print(get_all(load_candidates('candidates.json')))