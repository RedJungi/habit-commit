## while 문을 활용하여 두 수의 합계를 계산하는 프로그램 ##

hap = 0
a, b = 0, 0

while True :
  a = int(input("더할 첫 번째 수를 입력하세요 : "))
  b = int(input("더할 두 번째 수를 입력하세요 : "))
  hap = a + b
  print("%d + %d = %d" % (a, b, hap))