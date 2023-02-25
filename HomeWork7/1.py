c = input()
st = c.lower().split()
f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
t = f(st[0])
if all([f(i) == t for i in st]):
    print('Парам пам-пам')
else:
    print('Пам парам')