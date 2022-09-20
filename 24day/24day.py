## 리스트의 생성과 초기화 ##

aa = []
bb = []
Value = 0

for i in range(0, 100) :
  aa.append(Value)
  Value += 2

for i in range(0, 100) :
  bb.append(aa[99 - i])

print("bb[0]에는 %d이, bb[99]에는 %d이 입력됩니다." % bb[0], bb[99])