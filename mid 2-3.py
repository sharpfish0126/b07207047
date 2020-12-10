# 3
# -*- coding: utf8 -*-

location = input()
f = open(location, "r", encoding='cp950')
type1 = input()

data_dict = {}
for data in f:
  data = data.split(",")
  for z in range(len(data)):
      if z not in data_dict:
          data_dict[z] = []
          data_dict[z].append(data[z])
      else:
          data_dict[z].append(data[z])

print(data_dict)




if type1 == "TYPE":
    for i in range(len(data_dict)):
        while True:
            try:
                a = float(data_dict[i][0])
            except ValueError:
                a = "none"
        if float(data_dict[i][0]) != "none":
            print(i, " ", " numerical", sep="")
        else:
            print(i, " ", " categorical", sep="")


