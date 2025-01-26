students={
    "name":"Ali Raza",
    "class":"AI",
    "roll_no":123,
    "subjects":{
        "subject1":"Maths",
        "subject2":"Physics",
        "subject3":"Chemistry"
    }
}

print(students)

# print(students["subjects"]["subject1"])
# print(students["subjects"]["subject2"])
# print(students["subjects"]["subject1"])

member1 = {
    "name": "Ali ",
    "passion": "vocals"
}
member2 = {
    "name": "Ahmed",
    "passion": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])