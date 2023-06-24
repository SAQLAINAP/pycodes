database = [
    {"name":"Rome", "ancient":True, "Asian":False, "European":True , "American":False ,"Tourist":True, "expensive":True, "Crowded":False},

    {"name": "Paris", "ancient": False, "Asian": False, "European": True, "American":False, "Tourist": True, "expensive": True,"Crowded": False},

    {"name": "Dubai", "ancient": False, "Asian": True, "European": False, "American":False, "Tourist": True, "expensive": True,"Crowded": True},

    {"name": "New York", "ancient": False, "Asian": False, "European": False, "American":True, "Tourist": False, "expensive": True,"Crowded": False},

    {"name": "Mexico City", "ancient": False, "Asian": False, "European": False, "American":True, "Tourist": False, "expensive": False,"Crowded": True},

    {"name": "Sydney", "ancient": False, "Asian": False, "European": False, "American":False, "Tourist": True, "expensive": True,"Crowded": True},

    {"name": "Bangalore", "ancient": False, "Asian": True, "European": False, "American":False, "Tourist": False, "expensive": False,"Crowded": True},

    {"name": "Athens", "ancient": True, "Asian": False, "European": True, "American":False, "Tourist": True, "expensive": False,"Crowded": False},

    {"name": "Doha", "ancient": False, "Asian": True, "European": False, "American":False, "Tourist": True, "expensive": True,"Crowded": False},
]

def take_chance(answer, property):
    if answer == "y":
        ans = True
    else:
        ans = False

    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

    if len(database) == 1:
        print("your city is "+database[0]["name"])
        quit()


ans = input("is your city ancient(y,n)")
take_chance(ans, "ancient")


ans = input("Is your city Asian(y,n)")
take_chance(ans, "Asian")

ans = input("Is your city in a European(y,n)")
take_chance(ans,"European")

ans = input("Is your city in a American(y,n)")
take_chance(ans,"American")

ans = input("Is your city Tourist(y,n)")
take_chance(ans,"Tourist")

ans = input("Is your city expensive(y,n)")
take_chance(ans,"expensive")

ans = input("Is your city Crowded(y,n)")
take_chance(ans,"Crowded")