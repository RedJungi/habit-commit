## if문을 활용하여 할인 프로그램 만들기 ##

grade = input('등급을 입력해주세요(gold silver,bronze)')
payment = int(input('지불할 금액을 입력해주세요'))

if grade == 'gold' :
  payment = payment * 0.7 # 할인률 30%
elif grade == 'silver':
  payment = payment * 0.8 # 할인률 20%
elif grade == 'bronze':
  payment = payment * 0.9 # 할인률 10%
else:
  print('해당 등급은 없습니다.')

print('당신의 등급은',grade)
print('지불할 금액은',payment)