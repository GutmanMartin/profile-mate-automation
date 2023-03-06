import csv

INPUT_FILE_1 = "./input1.csv"
INPUT_FILE_2 = "./input2.csv"

outputList = []


with open(INPUT_FILE_1) as file1:
    file1 = csv.reader(file1)
    for row in file1:
        if not row[0] in outputList:
            outputList.append(row[0])

with open(INPUT_FILE_2) as file2:
    file2 = csv.reader(file2)
    for row in file2:
        if not row[0] in outputList:
            outputList.append(row[0])


outputFile = open("./output.csv", "w", newline="")
outputWriter = csv.writer(outputFile)
for i in outputList:
    outputWriter.writerow([i])

outputFile.close()