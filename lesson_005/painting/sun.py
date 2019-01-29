import simple_draw as sd


def draw_sun(start_point, radius=40, length=100, angle_step=20, color=sd.COLOR_YELLOW):

    step = angle_step
    for i in range(0, 18):
        length_rays = length
        vector = sd.get_vector(start_point, 5+step, length_rays)
        vector.draw(color=sd.background_color)
        # if i == 0:
        #     vector = sd.get_vector(start_point, 0, sd.random_number(radius, length))
        # else:

        if i % sd.random_number(1, 5) == 0:
            length_rays = length_rays // 1.5
            print(i)

        vector = sd.get_vector(start_point, 5+step, length_rays)
        step += angle_step
        vector.draw(color=sd.COLOR_YELLOW)

    sd.circle(center_position=start_point, radius=radius, width=0, color=color)


if __name__ == '__main__':
    while True:
        sd.start_drawing()

        draw_sun(sd.get_point(400, 400))

        sd.sleep(0.2)
        sd.finish_drawing()

        if sd.user_want_exit():
            break
