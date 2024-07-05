import turtle
import time
import random

WIDTH,HEIGHT=900,600
COLORS=["green",'pink','red','black','cyan','orange','yellow','purple','violet','light salmon']


def get_number_of_racers():
    racers=0
    while True:
        racers=input("Enter the number of turtles (2-10): ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("Input is not numeric So please try again")
            continue
        if 2<=racers<=10:
            return racers
        else:
            print('Number is not in range 2-10, please try again')

def race(colors):
    turtles=create_turtles(colors)
    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y>(HEIGHT)//2 - 20:
                return colors[turtles.index(racer)]





def create_turtles(colors):
    turtles=[]
    spacingx=WIDTH//(1+len(colors))
    for i, color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 +(i+1)*spacingx,-HEIGHT//2 +30)
        racer.pendown()
        turtles.append(racer)
    return turtles



def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")


racers= get_number_of_racers()
init_turtle()

random.shuffle(COLORS)

colors = COLORS[:racers]

winner=race(colors)
print(winner," has won the game")
time.sleep(10)