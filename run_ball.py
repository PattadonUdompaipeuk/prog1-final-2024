import turtle
import ball
import random
import seven_segments_proc

class BouncingBall:
    def __init__(self, num_balls):
        # self.num_balls = num_balls
        # turtle.speed(0)
        # turtle.tracer(0)
        # turtle.hideturtle()
        # self.canvas_width = turtle.screensize()[0]
        # self.canvas_height = turtle.screensize()[1]
        # print(self.canvas_width, self.canvas_height)
        # ball_radius = 0.05 * canvas_width
        # turtle.colormode(255)
        # xpos = []
        # ypos = []
        # vx = []
        # vy = []
        # ball_color = []
        self.num_balls = num_balls
        self.ball_list = []
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)

        ball_radius = 0.05 * self.canvas_width
# create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(self.num_balls):
            # xpos.append(random.uniform(-1*canvas_width + ball_radius, canvas_width - ball_radius))
            # ypos.append(random.uniform(-1*canvas_height + ball_radius, canvas_height - ball_radius))
            # vx.append(10*random.uniform(-1.0, 1.0))
            # vy.append(10*random.uniform(-1.0, 1.0))
            # ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            x = -self.canvas_width + (i + 1) * (2 * self.canvas_width / (self.num_balls + 1))
            y = 0.0
            vx = 10 * random.uniform(-1.0, 1.0)
            vy = 10 * random.uniform(-1.0, 1.0)
            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball_list.append(ball.Ball(ball_radius, x, y, vx, vy, ball_color, i))


    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)


# hold the window; close it by clicking the window close 'x' mark


