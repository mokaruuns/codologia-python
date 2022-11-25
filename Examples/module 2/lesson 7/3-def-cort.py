def getDate(dateString):
    day = int(dateString[0:2])
    month = int(dateString[3:5])
    year = int(dateString[6:10])
    return day, month, year


date = "17.03.2019"
print(getDate(date))
