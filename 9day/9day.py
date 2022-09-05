## 비트 연산자 ##

a = ord('A')
mask = 0x0F

print("%x & %x = %x" % (a, mask, a & mask))
print("%X & %X = %x" % (a, mask, a | mask))

mask = ord('a') - ord('A')

b = a ^ mask
print("%c ^ %d = %c" % (a, mask, b))
a = b ^ mask
print("%c ^ %d = %c" % (b, mask, a))

## 시프트 연산자 ##

a = 100
result = 0
i = 0

for i in range(1, 5):
  result = a << i
  print("%d << %d = %d" % (a, i, result))

for i in range(1, 5):
  result = a >> i
  print("%d >> %d = %d" % (a, i, result))