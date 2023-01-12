import random
from tkinter import *
import time

root = Tk()
c = Canvas(root, width=600, height=600, background='black')
c.pack()


def move(n):
    for a in range(n, 0, -1):
        c.move(ball, 0, -a)
        root.update()
        time.sleep(0.1)
    for b in range(n):
        c.move(ball, 0, b)
        root.update()
        time.sleep(0.003 * b)
    c.move(ball, 0, 600 - c.coords(ball)[3])
    root.update()
    time.sleep(0.1)


ball = c.create_oval(280, 580, 300, 600, fill='gray', outline='white')
li = sorted(random.sample(range(0, 25), 6), reverse=True)
for i in range(len(li)):
    move(li[i])
c.delete(ball)
root.mainloop()
