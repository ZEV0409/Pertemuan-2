from controller import Robot
import math


robot = Robot()
timestep = int(robot.getBasicTimeStep())


rot = robot.getDevice("joint_rot")
trans = robot.getDevice("joint_trans")
rot.setPosition(float('inf'))
trans.setPosition(float('inf'))
rot.setVelocity(1.0)
trans.setVelocity(1.0)


# Target posisi end-effector
x_target = 1.0
y_target = 0.5


# Hitung sudut rotasi
theta = math.atan2(y_target, x_target)
# Hitung translasi prismatic
jarak = math.sqrt(x_target**2 + y_target**2)


rot.setPosition(theta)
trans.setPosition(jarak)


while robot.step(timestep) != -1:
pass