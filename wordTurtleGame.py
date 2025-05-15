import turtle
import random

# turtle code
f = turtle.Turtle()
t = turtle.Turtle()
turtle.bgcolor("light sea green")

t.pensize(100)
t.shape("turtle")
t.speed(1)
t.penup()
t.goto(-400, 0)

f.pensize(20)
f.shape("square")
f.pencolor("white")
f.speed(2)
f.penup()
f.goto(200, 0)
f.pendown()
f.lt(90)
f.fd(200)
f.bk(5)
f.rt(90)
f.pensize(1)
f.fd(160)
f.lt(90)
f.pensize(20)
f.fd(5)
f.bk(200)
f.fd(155)
f.lt(90)
f.pensize(1)
f.fd(160)
f.bk(20)

f.shape("classic")
f.pensize(5)
f.lt(90)
f.bk(25)
f.lt(90)
f.fd(15)
f.bk(15)
f.lt(90)
f.bk(10)
f.rt(90)
f.fd(10)
f.bk(10)
f.rt(90)
f.fd(15)
f.penup()

f.lt(90)
f.fd(25)

f.pendown()
f.lt(90)
f.fd(25)
f.bk(25)
f.penup()

f.rt(90)
f.fd(10)

f.pendown()
f.lt(90)
f.fd(25)
f.rt(140)
f.fd(32)
f.lt(140)
f.fd(25)
f.bk(25)
f.penup()

f.rt(90)
f.fd(10)

f.pendown()
f.lt(90)
f.fd(25)
f.bk(25)
f.penup()

f.rt(90)
f.fd(10)

f.pendown()
f.fd(15)
f.lt(90)
f.fd(12)
f.lt(90)
f.fd(15)
f.rt(90)
f.fd(12)
f.rt(90)
f.fd(15)

f.penup()
f.rt(90)
f.fd(25)
f.lt(90)
f.fd(10)

f.pendown()
f.lt(90)
f.fd(25)
f.bk(14)
f.rt(90)
f.fd(15)
f.rt(90)
f.bk(14)
f.fd(25)

f.penup()
f.lt(90)
f.fd(200)

# Game logic
score = 0

print('In this game you have to guess the right word.\n ')

word_list = ['python', 'programming', 'language', 'concatenate', 'computer', 'science', 'debugging', 'syntax', 'argument', 'datatype']

random.shuffle(word_list)

for word in word_list:
    L1 = list(word)
    random.shuffle(L1)
    shuffle_words = ' '.join(L1)
    print(shuffle_words + '\n')

    ans = input()

    if ans == word:
        score += 2
        print('correct.\n')
        t.forward(80)  
    else:
        print('wrong.\n')
        t.bk(10)
    if score >= 16:
        print('Congratulations! You won the game :) \n')
        break


print('Thanks for playing, your final score = ', score)

