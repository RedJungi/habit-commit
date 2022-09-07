## 윤년 계산하기 ##

# 전역 변수 부분 #
year = int(input())

# 메인 코드 부분 #

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    # 윤년이 맞으면 yes
    print('yes')
else:
    # 윤년이 아니면 no
    print('no')
