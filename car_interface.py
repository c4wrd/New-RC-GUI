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
        raise NotImplementedError("Not implemented")

    def set_direction(direction: int):
        """
        Sets the direction of the car.

        :param int direction: The direction to set the car towards, where direction is in
        the range (-45, 45) which is the degrees to the left or right (left is negative, right is positive).
        Setting the direction to 0 will drive the car forward
        """
        raise NotImplementedError("Not implemented")
