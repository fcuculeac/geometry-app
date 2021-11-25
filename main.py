from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

    def distance_from_point(self, other_point):
        # distance is square root between
        return ((self.x - other_point.x) ** 2 +
                (self.y - other_point.y) ** 2) ** 0.5

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def rectangle_area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


class GuiPoint(Point):

    def draw(self, canvas: turtle.Turtle, size=5, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)
        canvas.hideturtle()


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


# gui_rectangle = GuiRectangle(Point(randint(0, 200), randint(0, 200)),
#                              Point(randint(10, 200), randint(10, 200)))
#
my_turtle = turtle.Turtle()
# gui_rectangle.draw(my_turtle)
# gui_point = GuiPoint(200, 30)
# gui_point.draw(my_turtle)
#
# turtle.done()

rect1 = GuiRectangle(
    Point(randint(0, 200), randint(0, 200)),
    Point(randint(201, 300), randint(201, 300))
)
rect1.draw(my_turtle)
print(f"Rectangle coordinates: {rect1.point1} and {rect1.point2}.")

user_point = GuiPoint(float(input("Guess x: >>> ")), float(input("Guess y: >>> ")))
user_point.draw(my_turtle)
print(f"The point {user_point} is in the rectangle: \
{user_point.falls_in_rectangle(rect1)}")

user_area = float(input("Guess area >>> "))
# if user_area == rect1.rectangle_area():
#     print("You guess correctly.")
# else:
#     print(f"Your guess is wrong. Area is {rect1.rectangle_area()}")

print(f"You off by {rect1.rectangle_area() - user_area} ")

turtle.done()
