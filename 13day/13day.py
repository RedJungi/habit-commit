## if문을 활용하여 학점 계산 프로그램 ##

score = int(input('점수를 입력해주세요.'))
if score >= 90:
  print('A')
elif score >= 80:
  print('B')
elif score >= 70:
  print('C')
elif score >= 60:
  print('D')
else :
  print('F')