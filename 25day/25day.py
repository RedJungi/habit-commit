## 2차원 리스트 ##

from multiprocessing import Value


list1 = []
list2 = []
Value = 1
for i in range(0, 3):
  for k in range(0, 4):
  list1.append(Value)
  Value += 1
  list2.append(list1)
  list1 = []

  for i in range(0, 3):
    for k in range(0, 4):
      print("%3d" % list2[i][k], end = " ")
      print("")