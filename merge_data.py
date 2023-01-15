import csv

data1 = []
data2 = []

with open("result.csv",'r',encoding="utf8")as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data1.append(i)


with open("result2.csv","r",encoding="utf8")as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data2.append(i)

#print(data1)
header1 = data1[0]
#print(data2)
header2 = data2[0]
header = header2+header1

new_data1 = data1[1:]
new_data2 = data2[1:]

new_data = []

for index,data in enumerate(new_data1):
    new_data.append(new_data2[index]+new_data1[index])

with open("final_result.csv","w",encoding="utf8",newline="")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(new_data)
    