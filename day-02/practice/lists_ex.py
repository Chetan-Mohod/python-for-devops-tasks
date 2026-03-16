# a = [100,200,300, True, 4.6]    # LIST banane ka 1la tareeka
# print(type(a))
# a.append(500)
# print(a)

# clouds = list() # LIST banane ka 2sra tareeka
# print(type(clouds))

# clouds.append("aws")
# clouds.append("azure")
# clouds.append("gcp")
# clouds.append("ibm")
# clouds.append("alibaba")
# clouds.append("utho")
# print(clouds)
# print("Length of list is:", len(clouds))
# print("World Leader for Cloud Service Provider is:",clouds[0])
# print("Indian Cloud Service Provider is:",clouds[-1])

# print(dir(clouds))
# print(clouds.extend.__doc__)


# # ['aws', 'azure', 'gcp', 'ibm', 'alibaba', 'utho']
# # range(5) -> 0,1,2,3,4

# # iterate a list
# for cloud in clouds:
#     if cloud == "aws":
#         print(f"{cloud} Market Leader + coverd in course")
#     elif cloud == "utho":
#         print(f"{cloud} Indian Cloud")
#     elif cloud == "azure" or cloud == "gcp":
#         print(f"{cloud} DevOps - Zero To Hero Me vo bhi cover karoonga")
#     else:
#         print(f"{cloud} baaki nahi honge")

# a = 100
# a = 200
# print(type(a))
# print(a)


a = [100,200,4.5,True,"hello"] #LIST

print(type(a))
# new_value = print(input("Enter any value:"))
a.append(input("Enter any value to add into LIST:"))
print(a)

cloud = list()

print(type(cloud))
cloud.append("aws")
cloud.append("azure")
cloud.append("gcp")
cloud.append("ibm")
cloud.append("utho")
print("Length of the cloud list is:",len(cloud))
print("World best cloud service provider is:", cloud[0])
print("Indian cloud provider name is:",cloud[-1])

print(dir(cloud))

print(cloud.count.__doc__)



for cloud in cloud:
    if cloud == "aws":
        print(f"{cloud} is Market Leader")
    elif cloud == "utho":
        print(f"{cloud} is Indian Cloud")
    elif cloud == "azure" or cloud == "gcp":
        print(f"{cloud} is one of the top two cloud provider")
    else:
        print(f"{cloud} is also cloud provider")
