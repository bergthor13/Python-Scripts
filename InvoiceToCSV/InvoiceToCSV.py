import re
import csv
import os
import sys
import locale

def getYear(dueYear, dueMonth, currMonth):
    if currMonth == dueMonth:
        return dueYear
    if dueMonth < currMonth:
        return dueYear - 1
    else:
        return dueYear

locale.setlocale(locale.LC_ALL, 'is_IS')

for f in sys.argv[1:]:
    with open(os.path.splitext(f)[0] + ".csv", 'wb') as csvFile:
        total = 0
        dueMonth = 0
        dueYear = 0
        spamwriter = csv.writer(csvFile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open(f) as f:
            content = f.readlines()
            for x in content:
                matchDate = re.match(r"([0-9][0-9]).([0-9][0-9]).([0-9][0-9][0-9][0-9])", x)
                if matchDate:
                    dueYear = int(matchDate.groups()[2])
                    dueMonth = int(matchDate.groups()[1])
                    break
            for x in content:
                matchObj1 = re.findall(r"([0-9][0-9]\.[0-9][0-9])	 ([0-9]*)	 (.*?)	 ([.0-9-]*)", x)
                matchObj2 = re.findall(r"^([0-9][0-9]\.[0-9][0-9])[\t]* (.+?)	[ ]*?.*?[\t]* ([0-9\.-]*)[\t]* ([0-9\.-]*)$", x)
                if (matchObj1):
                    for ex in matchObj1:
                        currMonth = int(ex[0][3:5])
                        useYear = str(getYear(dueYear, dueMonth, currMonth))

                        if ex == None:
                            continue
                        if ex[-1] == "":
                            continue

                        if ex[-1][-1] == "-":
                            value = int("-" + ex[-1][:-1].replace(".",""))
                            spamwriter.writerow([ex[0]+"."+useYear, ex[2], value*-1])
                            total += value
                        else:
                            value = int(ex[-1].replace(".",""))
                            spamwriter.writerow([ex[0]+"."+useYear, ex[2], value*-1])
                            total += value
                        currMonth = ex[0][3:4]
                if (matchObj2):
                    for ex in matchObj2:
                        currMonth = int(ex[0][3:5])
                        useYear = str(getYear(dueYear, dueMonth, currMonth))
                        
                        if ex == None:
                            continue
                        if ex[-1] == "":
                            continue
                        
                        if ex[-1][-1] == "-":
                            value = int("-" + ex[-1][:-1].replace(".",""))
                            spamwriter.writerow([ex[0]+"."+useYear, ex[1], value*-1])
                            total += value
                        else:
                            value = int(ex[-1].replace(".",""))
                            spamwriter.writerow([ex[0]+"."+useYear, ex[1], value*-1])
                            total += value

            
            print(locale.format('%d kr.', total, grouping=True))
            total = 0