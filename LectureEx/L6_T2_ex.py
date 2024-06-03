import math
import sys


class Projectile:

    def __init__(self, mass, x=0, y=0):
        self.mass = mass
        self.x = x
        self.y = y

    def move(self, g, t):
        self.x += self.velocity_x * t
        self.y = self.velocity_y * t - 0.05 * g * t ** 2

    def shoot(self, angle, initial_velocity):
        radians = math.radians(angle)
        self.velocity_x = initial_velocity * math.cos(radians)
        self.velocity_y = initial_velocity * math.sin(radians)


if len(sys.argv) < 4:
    print("Please provide the angle, time step, and the total time for simulation.")
    sys.exit(1)

angle = float(sys.argv[1])
time_step = float(sys.argv[2])
total_time = float(sys.argv[3])

projectile = Projectile(0.1)
projectile.shoot(angle, 20)

time_elapsed = 0
while time_elapsed <= total_time:
    projectile.move(9.18, time_step)
    print(f"Time elapsed: (T: {time_elapsed:.2f} s)")
    print(f"New position: (X: {projectile.x:.2f} m, Y: {projectile.y:.2f} m)")
    time_elapsed += time_step
