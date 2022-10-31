import re, os

#1
with open("myfullname.txt", 'r') as f:
    data = f.read()
    check = re.compile(r"(Ch\w+|Au\w+)")
    the_list = check.findall(data)
    print(f"\n 1) My full name is {the_list[0]} {the_list[1]} {the_list[2]}")

#2
path = os.getcwd()
print("\n2) " +path)

# 3
with open("baby2008.html", "r") as h:
    data = h.read()
    x = re.sub(r'<.*?>', ' ', data)
    names = re.compile(r'\s*[1-9]+\s*([A-Z][a-z]+)\s*([A-Z][a-z]+)')
    the_names = names.findall(x)
    baby_names = []
    male_names = []
    female_names = []
    for x in range(len(the_names)):
        if x == 0:
            continue
        else:
            male = the_names[x][0]
            female = the_names[x][1]
            baby_names.append(male)
            baby_names.append(female)
            male_names.append(male)
            female_names.append(female)
    print("")
    print(baby_names)
    print(male_names)
    print(female_names)
