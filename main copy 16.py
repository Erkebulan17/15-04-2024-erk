b = {
    "car" : "Toyota",
    "model" :"camry",
    "imeges" : ['https://cam50-imege','https://cam75-imege'],
    "price" : 25000000,
    "is_published" : True
    }

a = {
    "car" : "Toyota",
    "model" :"camry",
    "imege" : ['https://cam50-imege'],
    }


list_1 = [
    {
        "name" :"Kanat",
        "last_name":"Erbolov",
        "age": 43
    },
    {
        "name": "Miras",
        "last_name": "Miko",
        "age": 18
    },
    {
        "name": "Agibay",
        "last_name": "Zhandosov",
        "age": 99
    }
]
t=0
for n in list_1:
    t += n["age"]

n=len(list_1)
c = t/n
print(c)
