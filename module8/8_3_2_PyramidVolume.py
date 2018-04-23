def pyramid_volume(base_length, base_width, pyramid_height):
    base_area = base_length * base_width
    total_volume = base_area * (pyramid_height * 1/3)
    return total_volume


print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(7.0, 5.1, 6.0))

