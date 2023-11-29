person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
}
print(person)
print(person["name"])
print(person["hobby"])
person["surname"]="Nowak"
print(person["surname"])
#1
if person["married"]==False:
    person["married"]=True
else:
    person["married"]=False
#2
person["married"] = not person["married"]


person["gender"]="male"

#1
person["hobby"].append("bicycle")
#2
person["hobby"]=person["hobby"]+['bicycle']

person["phone"]["work"]='313131444'


