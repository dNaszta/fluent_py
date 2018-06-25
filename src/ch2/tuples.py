import os

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude)

b = 1
a = 2
a, b = b, a
print(b)

t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient, remainder)

_, dirname = os.path.split('/var/log/ize.md')
print(dirname)

#29
