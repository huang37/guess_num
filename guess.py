import random
first = input('開始值：')
last = input('結束值：')
r = random.randint(first,last)
count = 0
while True:
  count += 1
  num = input('請猜數字：')
  num = int(num)
  if num == r:
    print('你猜中了！！')
    print('你共猜了', count, '次')
    break
  elif num > r:
    print('比答案大')
  elif num < r:
    print('比答案小')
  print('這是你猜的第', count, '次')