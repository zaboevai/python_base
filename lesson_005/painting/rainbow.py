
import simple_draw as sd

rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

def draw_line_rainbow(start_x = 0, end_x = 100):
    step = 0
    for color in rainbow_colors:
        start_point = sd.get_point(start_x+step, start_x)
        end_point = sd.get_point(end_x+step, end_x)
        sd.line(start_point=start_point, end_point=end_point, color=color, width=5)
        step += 5


def draw_rainbow(x=0, y=0, radius=500, width=1, rainbow_colors=rainbow_colors, game_tick=0):

    step = 0
    for num, color in enumerate(rainbow_colors):
        start_point = sd.get_point(x, -y)
        sd.circle(center_position=start_point, radius=radius+step, color=color, width=width+1)
        step += width

    if game_tick % 2 == 1:
        rainbow_colors.append(rainbow_colors[0])
        rainbow_colors.remove(rainbow_colors[0])



if __name__ == '__main__':

    while True:

        sd.start_drawing()
        draw_rainbow(width=6)
        sd.finish_drawing()
        sd.sleep(0.1)

        if sd.user_want_exit():
            break


