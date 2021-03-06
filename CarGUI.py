import os
from sys import platform
from tkinter import *

#GUI For Group 8's RC Car
#Sean Jungst
from car_interface import RCCar, GyroReading

car = RCCar()

#car.on_reading =

#GUI window
root = Tk()
root.title("RC GUI")
theLabel = Label(root, text="Group 8's RC Car GUI", font=("Helvetica", 18), fg="blue", bg="dark gray")
root.geometry("900x650")
root.configure(bg="dark gray")
theLabel.pack()

#Display gyro information

textBox1 = Text(root, height=1, width=12, font=("Helvetica", 16))
textBox1.pack(pady=5)
textBoxAccX = Text(root, height=1, width=20, font=("Helvetica", 16))
textBoxAccX.pack()
textBox2 = Text(root, height=1, width=12, font=("Helvetica", 16))
textBox2.pack(pady=5)
textBoxAccY = Text(root, height=1, width=20, font=("Helvetica", 16))
textBoxAccY.pack()
textBox1.insert(END, "Acceleration x:")
textBox2.insert(END, "Acceleration y:")
textBox3 = Text(root, height=1, width=12, font=("Helvetica", 16))
textBox3.pack(pady=5)
textBoxAccZ = Text(root, height=1, width=20, font=("Helvetica", 16))
textBoxAccZ.pack()
textBox4 = Text(root, height=1, width=5, font=("Helvetica", 16))
textBox4.pack(pady=5)
textBoxNewPitch = Text(root, height=1, width=20, font=("Helvetica", 16))
textBoxNewPitch.pack()
textBox3.insert(END, "Acceleration z:")
textBox4.insert(END, "Pitch:")
textBox5 = Text(root, height=1, width=5, font=("Helvetica", 16))
textBox5.pack(pady=5)
textBoxNewRoll = Text(root, height=1, width=20, font=("Helvetica", 16))
textBoxNewRoll.pack()
textBox6 = Text(root, height=1, width=5, font=("Helvetica", 16))
textBox6.pack(pady=5)
textBoxNewYaw = Text(root, height=1, width=20, font=("Helvetica", 16))
textBoxNewYaw.pack()
textBox5.insert(END, "Roll:")
textBox6.insert(END, "Yaw:")

textBox1.config(state=DISABLED)
textBox2.config(state=DISABLED)
textBox3.config(state=DISABLED)
textBox4.config(state=DISABLED)
textBox5.config(state=DISABLED)
textBox6.config(state=DISABLED)

#data
#textBoxAccX
#textBoxAccY
#textBoxAccZ
#Pitch
#Yaw
#Roll

# textBox3.pack(side=RIGHT)
# textBox4.pack(side=RIGHT)
# textBox1.pack(side=TOP)
# textBox2.pack(side=TOP)

#buttons for movement

# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(bottomFrame, text="Forwards", fg="blue")
# button2 = Button(bottomFrame, text="Left", fg="blue")
# button3 = Button(bottomFrame, text="Backwards", fg="blue")
# button4 = Button(bottomFrame, text="Right", fg="blue")
#
# button1.pack(side=TOP)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=LEFT)

#Sliders for steering and acceleration

#AccelerationSlider = Scale(root, orient=HORIZONTAL, length=350, width=20, from_=100,to=-100, tickinterval=10).pack()
#SteeringSlider = Scale(root, orient=HORIZONTAL, bg="dark gray", length=350, width=20, from_=-45,to=45, tickinterval=5).pack()

#gyroscope information
def on_gyroscope(gyroscope: GyroReading):
    value = """
Acceleration_x: {accel_x},
Acceleration_y: {accel_y},
Acceleration_z: {accel_z},
Pitch: {pitch},
Roll: {roll}
    """.format(
        accel_x = gyroscope.acceleration_x,
        accel_y = gyroscope.acceleration_y,
        accel_z = gyroscope.acceleration_z,
        pitch = gyroscope.pitch,
        roll = gyroscope.roll
    )
    #Set tkinter text box with values
    textBoxAccX.delete(1.0, END)
    textBoxAccX.insert(END, gyroscope.acceleration_x)
    textBoxAccY.delete(1.0, END)
    textBoxAccY.insert(END, gyroscope.acceleration_y)
    textBoxAccZ.delete(1.0, END)
    textBoxAccZ.insert(END, gyroscope.acceleration_z)
    textBoxNewPitch.delete(1.0, END)
    textBoxNewPitch.insert(END, gyroscope.pitch)
    #display largest roll todo
    textBoxNewRoll.delete(1.0, END)
    textBoxNewRoll.insert(END, gyroscope.roll)

#handle key presses
def on_key_press(key):
    if key.keysym == 'Up':
        car.set_speed(100)
    if key.keysym == 'Down':
        car.set_speed(-100)
    if key.keysym == 'Left':
        car.set_direction(-100)
    if key.keysym == 'Right':
        car.set_direction(100)
    print("pressed: %s" % key.keysym)

#handle key releases
def on_key_release(key):
    if key.keysym == 'Up' or key.keysym == 'Down':
        car.set_speed(0)
    if key.keysym == 'Left' or key.keysym == 'Right':
        car.set_direction(0)
    print("released: %s" % key.keysym)

if __name__ == "__main__":
    try:
        if platform == "linux":
            os.system('xset r off')
        frame = Frame(root, width=900, height=650, bg="dark gray")
        frame.bind("<Key>", on_key_press)
        frame.bind("<KeyRelease>", on_key_release)
        frame.pack()
        frame.focus_set()
        root.mainloop()
    except:
        if platform == "linux":
            os.system('xset r on')
