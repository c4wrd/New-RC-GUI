class GyroReading:
    pitch = 0
    yaw = 0
    roll = 0
    acceleration_x = 0
    acceleration_y = 0
    acceleration_z = 0

class CarResponse:
    gyro_reading: GyroReading = None
    speed: int = None
    direction: int = None

class RCCar:

    def set_speed(speed: int):
        """
        Sets the speed of the car.

        :param int speed: The speed to set the car, where the speed is in the range
            (-100, 100) where negative numbers are reverse, and positive numbers are forward,
            and a value of 0 will stop the car
        """
        print("Set speed: %d" %speed)

    def set_direction(direction: int):
        """
        Sets the direction of the car.

        :param int direction: The direction to set the car towards, where direction is in
        the range (-100, 100) where -100 turns the car fully to the left, and 100 turns the car fully to the right
        Setting the direction to 0 will drive the car forward
        """
        print("Set direection: %d" %direction)
