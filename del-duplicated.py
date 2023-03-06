import csv

outputFile = open("./output.csv", "w", newline="", encoding="utf-8")
outputWriter = csv.writer(outputFile)

INPUT_FILE_1 = "./input1.csv"
INPUT_FILE_2 = "./input2.csv"

outputList = []


with open(INPUT_FILE_1, encoding='utf-8') as file1:
    file1 = csv.reader(file1)
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


outputFile.close()