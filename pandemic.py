from Person import Person
import tkinter as tk
from random import randint


def pauseresume():
    global running
    if running:
        running = False
    else:
        running = True


germs_radius = Person.radius
window_size = 666


def move():
    global running, speed, canvas
    if running:
        # moving every dot
        for person in people:
            person.move()
        # sickness spreading algorithm
        for person1 in people:
            for person2 in people:
                if person1.is_sick and (not person2.is_sick) and person1.distance(person2) < germs_radius:
                    person2.is_sick = True
                    canvas.itemconfig(person2.circle, fill="red", outline='red')
    window.after(30, move)


def change_values(speed_var, amount_var):
    global speed
    global amount
    global canvas
    if speed_var.get():
        new_speed = int(speed_var.get())
        if new_speed != speed:
            speed = new_speed
            for person in people:
                person.set_speed(speed)

    if amount_var.get() and (int(amount_var.get()) > 0):
        diff = int(amount_var.get()) - amount
        if diff < 0:
            for i in range(-diff):
                canvas.delete(people[-1].circle)
                del people[-1]
        elif diff == 0:
            pass
        else:
            for i in range(diff):
                people.append(Person(canvas,
                                     randint(Person.radius, window_size-Person.radius),
                                     randint(Person.radius, window_size-Person.radius),
                                     speed=speed,
                                     window_size=window_size))
        amount = len(people)


# --- main ---

# creating canvas and buttons
window = tk.Tk()
window.title('pandemic')
canvas = tk.Canvas(window, bg="white", height=window_size, width=window_size)
pauseresume_btn = tk.Button(window, text="Pause/Resume", command=lambda: pauseresume())
submit_btn = tk.Button(window, text="Submit", command=lambda: change_values(speed_var, amount_var))


# creating variables for storing text from input widgets
speed_var = tk.StringVar()
amount_var = tk.StringVar()

# creating input widgets
speedlbl = tk.Label(window, text="Enter speed")
speedentry = tk.Entry(window, textvariable=speed_var)
amountlbl = tk.Label(window, text="Enter amount")
amountentry = tk.Entry(window,  textvariable=amount_var)

# packing content
pauseresume_btn.pack(side='top')
speedlbl.pack(side='top')
speedentry.pack(side='top')
amountlbl.pack(side='top')
amountentry.pack(side='top')
submit_btn.pack(side='top')
canvas.pack()

# creating objects
amount = 8
speed = 5
people = [Person(canvas,
                 randint(Person.radius, window_size-Person.radius),
                 randint(Person.radius, window_size-Person.radius),
                 is_sick=True,
                 speed=speed,
                 window_size=window_size)]
for i in range(amount-1):
    people.append(Person(canvas,
                         randint(Person.radius, window_size-Person.radius),
                         randint(Person.radius, window_size-Person.radius),
                         speed=speed,
                         window_size=window_size))

running = True
move()

window.mainloop()
