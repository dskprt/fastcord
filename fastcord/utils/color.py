def int_from_rgb(r, g, b):
    return (r << 16) + (g << 8) + b

def rgb_from_int(color):
    return ((color >> 16) & 255), ((color >> 8) & 255), (color & 255)
