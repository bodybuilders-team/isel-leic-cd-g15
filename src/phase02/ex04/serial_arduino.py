import serial


def receive_from_arduino(port):
    """
    Receives and prints data from the Arduino, using the serial port.

    :param port: The serial port to use.
    """

    ser = serial.Serial(port, baudrate=9600)
    while True:
        read_value = ser.readline()

        print(read_value)


# Tests
if __name__ == '__main__':
    receive_from_arduino('COM4')
    import sys
    sys.exit(0)
