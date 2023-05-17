import turtle as t
def draw_circle(circle_color, circle_radius):
    t.pendown()
    t.fillcolor(circle_color)
    t.begin_fill()
    t.circle(circle_radius)
    t.end_fill()
    t.penup()
    t.setpos(50)

color_list = ["yellow", "red", "blue", "green"]
circle_radius = int(input("radius:"))
circle_color = color_list[0]






