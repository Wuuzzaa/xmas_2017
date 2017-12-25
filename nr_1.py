file_path = "data/drilling.txt"

file = open(file_path)
zeilen = file.readlines()
drillinge = 0

for zeile in zeilen:
    for char in range(len(zeile)-1):
        #if zeile[i] == zeile[i+1] and zeile[i] == zeile[i+2]:
        if zeile[char + 1] == zeile[char] == zeile[char + 2]:
            drillinge += 1

print("Es gibt {} Drillinge".format(drillinge))
print("Es sind {} Zeilen".format(len(zeilen)))