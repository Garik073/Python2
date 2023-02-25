def same_by(condition, nums):
    return len(set(map(condition, nums))) == 1


values = [0, 2, 10, 5]
print(same_by(lambda x: x % 2, values))

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')