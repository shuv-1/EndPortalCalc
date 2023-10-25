import math

# data entry

FirstLocX, FirstLocZ, FirstRot = input("First shot. X, Z, camera angle. Enter them through the space bar: ").split()
FirstLocX = float(FirstLocX)
FirstLocZ = float(FirstLocZ)
FirstRot = float(FirstRot)

SecLocX, SecLocZ, SecRot = input("Second shot. X, Z, camera angle. Enter them through the space bar: ").split()
SecLocX = float(SecLocX)
SecLocZ = float(SecLocZ)
SecRot = float(SecRot)

# converting the entered data into a coordinate system I am comfortable with

if 0.0 > FirstRot > -180.0:
    FirstRot = abs(FirstRot)

elif 0.0 < FirstRot < 180.0:
    FirstRot = -FirstRot

elif FirstRot == 0.0 or FirstRot == 180.0 or FirstRot == -180.0:
    FirstRot = FirstRot


if 0.0 > SecRot > -180.0:
    SecRot = abs(SecRot)

elif 0.0 < SecRot < 180.0:
    SecRot = -SecRot

elif SecRot == 0.0 or SecRot == 180.0 or SecRot == -180.0:
    SecRot = SecRot

# angle-to-radian conversion
FirstRot = math.radians(FirstRot)
SecRot = math.radians(SecRot)


# coefficient search b
def findb(x, z, rotate):
    k = math.tan(rotate)
    b = x - z * k
    return b


b1 = findb(FirstLocX, FirstLocZ, FirstRot)
b2 = findb(SecLocX, SecLocZ, SecRot)

# last function and coordinate output
k1 = math.tan(FirstRot)
k2 = math.tan(SecRot)


def lastfunc(k1, k2, b1, b2):
    z = (b2 - b1) / (k1 - k2)
    x = k1 * z + b1
    z = int(z)
    x = int(x)
    print("Coordinates: ")
    print(str(x) + " ~ " + str(z))


lastfunc(k1, k2, b1, b2)
print()
print("Warning if the second throw points in a completely different direction, try going back 50-100 blocks")
