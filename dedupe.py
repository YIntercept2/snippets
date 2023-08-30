#dedupe - open a list of strings and remove all duplicates
import sys
results = []
#name of the input file to dedupe
file = open(sys.argv[1], "r")
while True:
  result = file.readline()
  results.append(result)
  if result == "":
    break

file.close()
print(results)

uniques = []

for i in results:
  if i not in uniques:
    uniques.append(i)


print("length of unique: " + str(len(uniques)))

#writes to the second argument passed to the script
file = open(sys.argv[2], 'a+')
for unique in uniques:
  file.write(unique)
  file.write("\n")

file.close()