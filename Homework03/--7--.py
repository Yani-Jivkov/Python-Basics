from math import pi

form = str(input())

if form == 'square':
    wall = float(input())
    face_square = wall * wall
    print(f'{face_square:.3f}')
elif form == 'rectangle':
    wall1 = float(input())
    wall2 = float(input())
    face_rectangle = wall1 * wall2
    print(f'{face_rectangle:.3f}')
elif form == 'circle':
    radius = float(input())
    face_circle = pi * radius ** 2
    print(f'{face_circle:.3f}')
elif form == 'triangle':
    wall1 = float(input())
    height = float(input())
    face_triangle = (wall1 * height) / 2
    print(f'{face_triangle:.3f}')