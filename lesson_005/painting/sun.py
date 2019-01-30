import simple_draw as sd


tick = 0
sun_start_point = sd.get_point(100, 100)
sun_size_step = 5


def draw_sun(start_point,
             radius=40,
             length=100,
             rays_count=9,
             move_step=1,
             size_step=1,
             color=sd.COLOR_YELLOW):

    rays_angle = 360 // rays_count
    point = start_point

    sd.circle(center_position=point, radius=length, width=0, color=sd.background_color)

    if point.y < sd.resolution[1]:
        next_point = sd.get_point(point.x+move_step, point.y+move_step)
    else:
        next_point = point

    rays_step = rays_angle

    for i in range(0, rays_count):
        length_rays = length
        if i % sd.random_number(1, 3) == 0:
            length_rays = 0

        vector = sd.get_vector(start_point=next_point, angle=rays_step, length= length_rays - size_step, width=2)
        rays_step += rays_angle
        vector.draw(color=color)

    sd.circle(center_position=next_point, radius=radius + 20 - size_step, width=0, color=sd.background_color)

    sd.circle(center_position=next_point, radius=radius - size_step, width=0, color=color)

    return next_point


if __name__ == '__main__':

    while True:

        sd.start_drawing()
        tick += 1

        if tick % 5 == 0:
            sun_size_step += 2
        # sun_size_step = 5

        sun_start_point = draw_sun(start_point=sun_start_point, radius=100, length=200, rays_count=36,
                                   move_step=2, size_step=sun_size_step, color=sd.COLOR_YELLOW)

        sd.sleep(0.05)
        sd.finish_drawing()

        if sd.user_want_exit():
            break
