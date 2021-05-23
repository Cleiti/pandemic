import tkinter as tk
from random import uniform, randint
from math import sqrt


class Person:
    def __init__(self, canvas, x, y):
        self.is_sick = False
        if self.is_sick:
            self.color = "red"
            self.outline = "red"
        else:
            self.color = "blue"
            self.outline = "blue"

        self.canvas = canvas

        self.x = x
        self.y = y

        self.x_velocity = uniform(-1, 1)
        self.y_velocity = uniform(-1, 1)

        while self.x_velocity == 0 and self.y_velocity == 0:  # avoiding (0,0) values
            self.x_velocity = uniform(-1, 1)
            self.y_velocity = uniform(-1, 1)
        cur_speed = self.y_velocity**2 + self.x_velocity**2
        adj_fact = sqrt((Person.speed**2)/cur_speed)
        self.x_velocity = self.x_velocity*adj_fact
        self.y_velocity = self.y_velocity*adj_fact

        self.circle = canvas.create_oval([self.x, self.y, self.x+self.size, self.y+self.size], outline=self.outline,
                                         fill=self.color)

    size = 30
    amount = 30
    speed = 15

    def move(self):

        self.canvas.move(self.circle, self.x_velocity, self.y_velocity)

        coordinates = self.canvas.coords(self.circle)
        self.x = coordinates[0]
        self.y = coordinates[1]

        # if outside screen bounce
        if self.x < 0 or self.x > (500 - Person.size):
            self.x_velocity = -self.x_velocity
        if self.y < 0 or self.y > (500 - Person.size):
            self.y_velocity = -self.y_velocity


def start():
    """starting process"""
    pass
    # TODO: finish start() function


def stop():
    """stopping process"""
    pass
    # TODO: finish stop() function


def move():
    for item in people:
        item.move()

    window.after(33, move)


# --- main ---

# creating canvas and buttons
window = tk.Tk()
canvas = tk.Canvas(window, bg="white", height=500, width=500)
startb = tk.Button(window, text="Start", command=start())
stopb = tk.Button(window, text="Stop", command=stop())

# creating variables for storing text from input widgets
speed_var = tk.StringVar()
amount_var = tk.StringVar()

speedlbl = tk.Label(window, text="Enter speed")
speedentry = tk.Entry(window, textvariable=speed_var)
amountlbl = tk.Label(window, text="Enter amount")
amountentry = tk.Entry(window,  textvariable=amount_var)

# packing content
startb.pack(side='top')
stopb.pack(side='top')
speedlbl.pack(side='top')
speedentry.pack(side='top')
amountlbl.pack(side='top')
amountentry.pack(side='top')
canvas.pack()

# getting variables from text fields
if speed_var.get():
    Person.speed = int(speed_var.get())
if amount_var.get():
    Person.amount = int(amount_var.get())

# creating objects
people = []
for i in range(Person.amount):
    p = Person(canvas, randint(0+Person.size, 500-Person.size), randint(0+Person.size, 500-Person.size))
    people.append(p)

move()

window.mainloop()
