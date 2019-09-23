nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []
for i in nums:
    my_list.append(i)
print(my_list)

my_list = [n for n in nums]
print(my_list)
for i in nums:
    my_list.append(i ** 2)
print(my_list)

my_list = [n ** 2 for n in nums]
print(my_list)

my_list = list(map(lambda n: n ** 2, nums))
print(my_list)

my_list = [n for n in nums if n % 2 == 0]
print(my_list)

letters = 'abcd'
my_list = [(letter, num) for letter in letters for num in nums]
print(my_list)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_list = list(zip(names, heros))
print(my_list)

my_dict = dict(zip(names, heros))
print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for i in nums:
    my_set.add(i)
print(my_set)
my_set = {i for i in nums}
print(my_set)

"""Generator Expression"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n ** 2


my_gen = gen_func(nums)
my_gen = (n ** 2 for n in nums)
for i in my_gen:
    print(i)
