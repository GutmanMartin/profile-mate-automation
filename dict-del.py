import csv
import os

directory = './'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if f[-4:] == ".csv":
            merge(f)




outputFile = open("./output.csv", "w", newline="", encoding="utf-8")
outputWriter = csv.DictWriter(f, ["username","Public Email","Follower Count","Following Count","Engagement Rate oF account,Website in URL","Total Posts,Business Category name","Phone Country Code,Public Phone Number","Link to Account","Is Private Account","Is business Account","id","fullName","city","bio"])


outputList = []





def merge(f):
    file = open(f, "r", encoding="utf-8")

    data = csv.DictReader(file)

    for row in data:
        
        print(row["username"])
    

"""

with open(INPUT_FILE_1, encoding='utf-8') as file1:
    file1 = csv.DictReader(f)(file1)
    for row in file1:
        if len(row[1]) > 0:
            if not row[1] in outputList:
                outputList.append(row[0])
                outputWriter.writerow(row)



with open(INPUT_FILE_2) as file2:
    file2 = csv.reader(file2)
    for row in file2:
        if len(row[1]) > 0:
            if not row[1] in outputList:
                outputList.append(row[4])
                outputWriter.writerow(row)

"""

file1.close()

outputFile.close()