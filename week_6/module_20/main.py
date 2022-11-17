import csv

with open("./data/friendsData.csv", "r") as file :
    infos = csv.reader(file)
    for info in infos :
        print(info[2])