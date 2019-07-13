# with open("C:\\Users\\rafae\\Desktop\\sample.txt", 'r') as file_read:
#     new_set = set()
#     aline = file_read.readline()
#     while aline:
#         new_word = aline.split(' ')
#         for word in new_word:
#             new_set.add(word)
#         aline = file_read.readline()
#
# print(new_set)


# import random
#


# x = {1, 2, 3}
# y = {3, 2, 1}
#
# print(y.intersection(x))

# import random

# random.seed(2)

# print(random.random())

# random.seed(2)

# print(random.random())

import turtle
import random
wn = turtle.Screen()
rafi = turtle.Turtle()
rafi.speed(2)
rafi.shape('turtle')

for i in range(0, 100):
    for aColor in ["yellow", "red", "purple", "dark blue", 'black', 'dark orange', 'brown']:
        rafi.color(aColor)
        rafi.goto((random.randrange(-100, 100)), (random.randrange(-100, 100)))
        rafi.goto(0, 0)

wn.exitonclick()

# import turtle
# import random
#
# dic = {}
# for i in range(1, 1000):
#     for aColor in ["yellow", "red", "purple", "dark blue", 'black', 'dark orange', 'brown']:
#     r = int(random.gauss(200, 50))
#     if r not in dic:
#         dic[r] = 1
#     else:
#         dic[r] = dic[r] + 1
#         rafi.color(aColor)
#         rafi.goto()
#         rafi.goto(0, 0)
# print(dic)
#
# wn = turtle.Screen()
# rafi = turtle.Turtle()
# rafi.speed(200)
# rafi.shape('turtle')




