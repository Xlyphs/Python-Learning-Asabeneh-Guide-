# Line equation: y = 2x - 2
# This is in the form: y = mx + b

m = 2      # This is the slope (number before x)
b = -2     # This is y-intercept (number alone)

print("For y = 2x - 2:")
print(f"Slope = {m}")

# Y-intercept: When x = 0
print(f"Y-intercept = (0, {b})")

# X-intercept: When y = 0
# Solve: 0 = 2x - 2
# Add 2 to both sides: 2 = 2x
# Divide by 2: x = 1
print(f"X-intercept = (1, 0)")

import math

# Points
point1 = (2, 2)   # (x1, y1)
point2 = (6, 10)  # (x2, y2)

print("\nFor points (2,2) and (6,10):")

# Slope formula: (y2 - y1) / (x2 - x1)
slope = (10 - 2) / (6 - 2)
print(f"Slope = (10-2)/(6-2) = 8/4 = {slope}")

# Distance formula: sqrt[(x2-x1)² + (y2-y1)²]
dx = 6 - 2   # = 4
dy = 10 - 2  # = 8
distance = math.sqrt(dx*dx + dy*dy)
print(f"Distance = √(4² + 8²) = √(16 + 64) = √80 ≈ {distance:.2f}")

print(m == slope)