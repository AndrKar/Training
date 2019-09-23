nums = [1, 2, 3, 4, 5]

for _ in nums:
    if _ == 3:
        print('Founded!')
        # break
        continue
    print(_)
for num in nums:
    for letter in 'abcdefg':
        print(num, letter, sep='/////')
for i in range(1, 10):
    print(i)
