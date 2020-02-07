import csv
with open('year2017.csv') as fileobj:
    dataobj = csv.DictReader(fileobj, delimiter=',', skipinitialspace=True)
    listobj = list(dataobj)
country_killed = {}
for row in listobj:
    key = row['Month']
    value = row['Killed']
    if value != '':
        value = int(float(value))
    else:
        value = 0
    if key in country_killed:
        country_killed[key] += value
    else:
        country_killed[key] = value
for i in country_killed:
    print(i, '', country_killed[i])
