from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()
movement_motors = MotorPair('E', 'A')
roll_target = 89.95
power = 3
integral = 0
#Not actual game values (k)
kp = 0
ki = 0
kd = 0
# Write your program here.
hub.light_matrix.show_image('HAPPY')
wait_for_seconds(3)
while True:
    error = roll_target - hub.motion_sensor.get_roll_angle()
    integral = integral + error * 0.25
    derivative = error - prev_error
    prev_error = error
    result = error * kp + integral * ki + derivative * kd
    print(
        "error:",
        error,
        "integral:",
        integral,
        "derivative:",
        derivative,
        "prev_error:",
        prev_error,
        "result:",
        result
    )
    movement_motors.start(steering=0, speed=result * power)

