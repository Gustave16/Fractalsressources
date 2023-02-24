#use this file combine with the "main2" to generate fractals

Width = 1920
Height = 1080

max_x = 1.6
max_y = 1.0
offset_x = -1.6
offset_y = -1.0

borders = 1.0
iterations = 100
color_mode = 1
complex_number = complex(-0.75, 0)
Height = (max_y - offset_y) * float(Width) / (max_x - offset_x)
Height = int(Height)
size = Width, Height
