import serial


def receive_from_arduino():
    ser = serial.Serial('9600')

    read_value = ser.write("lola")

    print(read_value)


if __name__ == '__main__':
    receive_from_arduino()
