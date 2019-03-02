import sys

weight = float(sys.argv[1])    # in kg
height = float(sys.argv[2])    # in meters
bmi = weight/height**2
print(bmi)
