import socket
import struct
from threading import Thread

import time

LISTEN_PORT = 8888
CAR_PORT = 8888
CAR_IP = "192.168.0.1"

class GyroReading:
    pitch = 0
    roll = 0
    acceleration_x = 0
    acceleration_y = 0
    acceleration_z = 0

def get_car_command(speed, direction):
    return struct.pack("<hh", speed, direction)

class RCCar:

    def __init__(self):
        self.speed = 0
        self.direction = 0
        # create sockets for sending and receiving
        self.send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recv_sock.bind(("127.0.0.1", LISTEN_PORT))
        # create threads
        self.recv_thread = Thread(target=self.receive_target)
        self.send_thread = Thread(target=self.send_target)
        self.recv_thread.start()
        self.send_thread.start()
        self.on_data = None

    def send_target(self):
        while True:
            cmd = get_car_command(self.speed, self.direction)
            self.send_sock.sendto(cmd, (CAR_IP, CAR_PORT))
            time.sleep(0.25)

    def receive_target(self):
        while True:
            data, addr = self.recv_sock.recvfrom(255)
            print("received data: %s" % str(data))
            if self.on_data is not None:
                print(data)

    def set_speed(self, speed: int):
        """
        Sets the speed of the car.

        :param int speed: The speed to set the car, where the speed is in the range
            (-100, 100) where negative numbers are reverse, and positive numbers are forward,
            and a value of 0 will stop the car
        """
        print("Set speed: %d" %speed)
        self.speed = speed

    def set_direction(self, direction: int):
        """
        Sets the direction of the car.

        :param int direction: The direction to set the car towards, where direction is in
        the range (-100, 100) where -100 turns the car fully to the left, and 100 turns the car fully to the right
        Setting the direction to 0 will drive the car forward
        """
        print("Set direection: %d" %direction)
        self.direction = direction