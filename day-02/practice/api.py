# import requests

# api_url = "https://jsonplaceholder.typicode.com/todos/1" # server URL (API)

# response = requests.get(url=api_url)

# for key,value in response.json().items():
#     if key == "userId":
#         if value in [100,200,300]:
#             print("User found")


import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=url)

print(response)
print("----------------------------")
print("----------------------------")

print(dir(response))

print("----------------------------")
print("----------------------------")
print(response.json())

# for key,value in response.json().items():
#     print(f"{key} : {value}")

# for key,value in response.json().items():
#     if key == "completed":
#         if value == False:
#             print("The data is not updated")


# for key,value in response.json().items():
#     if key == "userId":
#         if value in [1,2,3,4]:
#             print("User found")
#         else:
#             print("User Not Found")

for key,value in response.json().items():
    if key == "userId":
        if value in [1,2,3,4]:
            print("User found")
        else:
            print("User Not Found")
