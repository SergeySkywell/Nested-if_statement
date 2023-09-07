# Задание 1

print('Задание 1')

x = int(input('Введите икс: '))
y = int(input('Введите игрек: '))

if x < y:
  print('X меньше Y')

if x > y:
  print('X больше Y')

if x == y:
  print('X равен Y')

# Задание 2

print('Задание 2')

money = int(input('Введите сумму денег на счету: '))

course_price = 75000

if money >= course_price:
  money -= course_price
  if money < 5000:
    money += 1000
    print('Курс успешно приобретён! Вам сделана скидка в 1000 рублей.')
  else:
    print('Курс успешно приобретён!')
else:
  print('Недостаточно денег на счету. =(')

# Задание 2

print('Задание 3')

money = int(input('Сколько денег дала мама: '))
cheese_price = 60
ice_cream_price = 20

if money >= cheese_price:
  money -= cheese_price
  print('Денег на сыр хватило.')
  if money >= ice_cream_price:
    money -= ice_cream_price
    print('И на мороженое тоже хватило. =)')
  else:
    print('А на мороженку вот не хватило. =(')
else:
  print('Денег не хватило ни на сыр, ни на мороженое...')
