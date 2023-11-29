##import-->open+"w"-->json.dump()-->close
import json

movie= {
    "title":"Notebook",
    "year":2004,
    "actor":{"leading":"Rachel McAdams","supporting":"Joan Allen"},
    "oscar":False,
    "genre":"drama"
}

with  open("favourite.json","w") as file:
    json.dump(movie,file,indent=4)

