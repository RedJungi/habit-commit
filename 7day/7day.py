## 관계 연산자 ##

a,b = 100, 200

print(a == b, a != b, a > b, a < b, a >= b, a <= b)

## 논리 연산자 ##

a = 99
(a > 100) and (a < 200)
(a > 100) or (a < 200)
not(a == 100)

## 비트 연산자 ##

a = ord('A')
mask = 0x0F

print("%x & %x = %x" % (a, mask, a & mask))
print("%X & %X = %X" % (a, mask, a | mask))

mask = ord('a') - ord('A')

b = a ^ mask
print("%c ^ %d = %c" % (a, mask, b))
a = b ^ mask
print("%c ^ %d = %c" % (b, mask, a))