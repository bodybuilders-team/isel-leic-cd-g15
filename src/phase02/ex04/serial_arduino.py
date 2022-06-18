import serial


def receive_from_arduino(port):
    """
    Receives and prints data from the Arduino, using the serial port.

    :param port: The serial port to use.
    """

    ser = serial.Serial(port)

    read_value = ser.write("lola")

    print(read_value)


# Tests
if __name__ == '__main__':
    receive_from_arduino('9600')
