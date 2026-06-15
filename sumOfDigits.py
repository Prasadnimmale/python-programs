num = 123456
sum = 0

while num > 0:
    sum += num % 10
    num //= 10

print("Sum =", sum)