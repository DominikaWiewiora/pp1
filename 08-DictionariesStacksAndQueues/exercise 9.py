countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Germany", "population":83000000},
    {"name":"Spain", "population":47000000},
    {"name":"Italy", "population":59000000},
    {"name":"France", "population":67000000},
]
print("COUNTRY"+" POPULATION")
i=0
while i<len(countries):
    print(countries[i]["name"]+str(countries[i]["population"]))
    i+=1
