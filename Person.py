from random import uniform
from math import sqrt


class Person:
    radius = 30

    def __init__(self, canvas, x, y, is_sick=False, speed=5, window_size=500):
        self.speed = speed
        self.is_sick = is_sick
        self.window_size = window_size
        if self.is_sick:
            self.color = "red"
            self.outline = "red"
        else:
            self.color = "blue"
            self.outline = "blue"

        self.canvas = canvas

        self.x = x
        self.y = y

        self.x_velocity = 0
        self.y_velocity = 0

        # creating initial dx, dy values (direction)
        while self.x_velocity == 0 and self.y_velocity == 0:  # avoiding (0,0) values
            self.x_velocity = uniform(-1, 1)
            self.y_velocity = uniform(-1, 1)

        # normalizing speed and setting new speed
        cur_speed2 = self.y_velocity**2 + self.x_velocity**2
        adj_fact = sqrt((self.speed**2)/cur_speed2)
        self.x_velocity = self.x_velocity*adj_fact
        self.y_velocity = self.y_velocity*adj_fact

        self.circle = canvas.create_oval([self.x, self.y, self.x+Person.radius, self.y+Person.radius],
                                         outline=self.outline, fill=self.color)

    def move(self):
        # print(f'dx={self.x_velocity}, dy={self.y_velocity}')
        # print(f'v={self.x_velocity**2+self.y_velocity**2}')
        self.canvas.move(self.circle, self.x_velocity, self.y_velocity)

        coordinates = self.canvas.coords(self.circle)
        self.x = coordinates[0]
        self.y = coordinates[1]

        # if outside screen bounce
        if self.x < 0 or self.x > (self.window_size - Person.radius):
            self.x_velocity = -self.x_velocity
        if self.y < 0 or self.y > (self.window_size - Person.radius):
            self.y_velocity = -self.y_velocity

        # print(f'my speed = {sqrt(self.y_velocity**2 + self.x_velocity**2)}')

    def distance(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def set_speed(self, speed):
        cur_speed2 = self.y_velocity**2 + self.x_velocity**2
        adj_fact = sqrt((speed**2)/cur_speed2)
        self.x_velocity = self.x_velocity*adj_fact
        self.y_velocity = self.y_velocity*adj_fact
