from turtle import Turtle, mainloop, numinput

t = Turtle()

# t.forward(200)
# t.left(90)
# t.forward(100)
# t.circle(100, 180)
# t.forward(100)

t.width(5)
t.color('blue', 'yellow')

n = int(numinput('Pytanie', 'Ile wierzchokw'))

t.begin_fill()

for i in range(n):
    t.forward(1000/n)
    t.left(360/n)

t.end_fill()
mainloop()

