import csv
dataset1 = []
dataset2 = []
with open("dataset_1.csv") as f:
    csvreader = csv.reader(f)
    for eachrow in csvreader:
        dataset1.append(eachrow)

with open("dataset_2_sorted.csv") as f:
    csvreader = csv.reader(f)
    for eachrow in csvreader:
        dataset2.append(eachrow)
header1 = dataset1[0]
planetsdata1 = dataset1[1:]

header2 = dataset2[0]
planetsdata2 = dataset2[1:]

headers = header1+header2

print(len(dataset1))
print(len(dataset2))
planetdata = []
for index,data in enumerate(planetsdata1):
    planetdata.append(data+planetsdata2[index])

with open("mergecsv.csv","a+",newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)

print(len(planetdata))
