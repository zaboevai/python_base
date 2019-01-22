
import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def draw_line_rainbow(start_x = 0, end_x = 100):
    step = 0
    for color in rainbow_colors:
        start_point = sd.get_point(start_x+step, start_x)
        end_point = sd.get_point(end_x+step, end_x)
        sd.line(start_point=start_point, end_point=end_point, color=color, width=4)
        step += 5


def draw_rainbow(x=0, y=100):
    step = 0
    for color in rainbow_colors[::-1]:
        start_point = sd.get_point(x, -y)
        sd.circle(center_position=start_point, radius=500+step, color=color, width=30)
        step += 30

