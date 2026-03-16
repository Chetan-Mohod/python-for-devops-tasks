# info = {
#     "name" : "Shubham Bhaiya", #str
#     "city" : "Pune", #str
#     "qualification": "Mtech",
#     "age" : 29, # int
#     "salary": 22.5, # float
#     "married": True, # Bool
#     "favourites" : ["teaching", "movies", 18]
# }

# print("I live in",info["city"])
# print("I love ", info.get("favourite","Not Found"))

# info.update({"channel": "TrainWithShubham"})

# print(dir(info))

# for key,value in info.items():
#     print(key,value)


info = {
    "name" : "Chetan Mohod",
    "age" : 28,
    "salary" : 1.9,
    "city" : "Amravati",
    "favourites" : ["Learning","Movies","Travel"],
    "profession" : "Senior DevOps Engineer"
}

print("My name is", info["name"])
print("I have hobby of",info.get("favrouite","Not Found"))

print("I love to", info["favourites"][2])

print(dir(info["favourites"]))

print(info["favourites"].index.__doc__)

info["favourites"].reverse()
print("All hobbies:", info["favourites"])

info.update({"Married" : False})

print(info)

print(dir(info))

for key,value in info.items():
    print(f"{key}:{value}")
