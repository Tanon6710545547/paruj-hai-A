import turtle
from ball import Ball
from seven_segments_proc import tou
import random

class Run:
    def __init__(self):
        self.num_balls = 5
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

        # create random number of balls, num_balls, located at random positions within the canvas
        for i in range(self.num_balls):
            self.xpos.append(random.uniform(-1*self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1*self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(10*random.uniform(-1.0, 1.0))
            self.vy.append(10*random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

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

dt = 0.2  # time step
ving = Run()
bon = Ball()
Tom = turtle.Turtle()
tom_color = (255, 0, 0)
test = tou(Tom, tom_color)
delay_in_seconds = 0.01  # ลดเวลาลงเยอะ เพื่อให้อัพเดทบ่อยขึ้น
num = 0
frame_count = 0

# สร้าง turtle สำหรับวาดกรอบแยก (วาดครั้งเดียว)
border_turtle = turtle.Turtle()
border_turtle.hideturtle()
border_turtle.speed(0)
border_turtle.penup()
border_turtle.goto(-ving.canvas_width, -ving.canvas_height)
border_turtle.pensize(10)
border_turtle.pendown()
border_turtle.color((0, 0, 0))
for i in range(2):
    border_turtle.forward(2*ving.canvas_width)
    border_turtle.left(90)
    border_turtle.forward(2*ving.canvas_height)
    border_turtle.left(90)

# สร้าง turtle objects สำหรับแต่ละลูกบอล (ใช้ซ้ำไม่ต้องสร้างใหม่)
ball_turtles = []
for i in range(ving.num_balls):
    ball_t = turtle.Turtle()
    ball_t.hideturtle()
    ball_t.speed(0)
    ball_t.penup()
    ball_t.color(ving.ball_color[i])
    ball_t.shape("circle")
    ball_t.shapesize(ving.ball_radius / 10, ving.ball_radius / 10)
    ball_turtles.append(ball_t)

while True:
    # อัพเดทตำแหน่งลูกบอล
    for i in range(ving.num_balls):
        bon.move_ball(i, ving.xpos, ving.ypos, ving.vx, ving.vy, dt)
        bon.update_ball_velocity(i, ving.xpos, ving.ypos, ving.vx, ving.vy, ving.canvas_width, ving.canvas_height, ving.ball_radius)
        # เลื่อนลูกบอลไปตำแหน่งใหม่
        ball_turtles[i].goto(ving.xpos[i], ving.ypos[i])
        ball_turtles[i].showturtle()
    
    # อัพเดทตัวเลขทุก 20 เฟรม
    frame_count += 1
    if frame_count % 20 == 0:
        test.clear()
        test.draw(Tom, num)
        num = (num + 1) % 10
    
    turtle.update()
    test.my_delay(delay_in_seconds)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()