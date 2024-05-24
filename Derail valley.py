import time
import serial.tools.list_ports
import pyautogui

pyautogui.PAUSE = 0.001

previous_throttle = 0
previous_train_brake = 0
previous_ind_brake = 0
# Function to read data from USB port
def read_usb_port(device_name):
    try:
        ports = list(serial.tools.list_ports.comports())
        for port, desc, hwid in ports:
            if device_name in desc:
                ser = serial.Serial(port=port, baudrate=9600, timeout=1, write_timeout=1)
                ser.reset_input_buffer()  # Clear any existing data in the buffer
                print(f"Connected to USB port: {port} ({desc})")
                while True:
                    try:
                        data = ser.readline().decode().strip()  # Read data from USB port
                        if data:
                            string_split(data)
                    except serial.SerialException:
                        break  # Break out of the loop on serial exception
                break
        else:
            print(f"No USB device with name '{device_name}' found.")
    except Exception as e:
        print(f"Error: {e}")


def string_split(data):
    values_list = data.split()
    if len(values_list) >= 3:
        keyboard_control(values_list[0], values_list[1], values_list[2])
        print(values_list)

def keyboard_control(throttle_in, train_brake_in, ind_brake_in):
    throttle_in = int(throttle_in)
    train_brake_in = int(train_brake_in)
    ind_brake_in = int(ind_brake_in)

    global previous_throttle
    global previous_train_brake
    global previous_ind_brake

    if throttle_in > previous_throttle:
        pyautogui.press('t', presses=throttle_in - previous_throttle)
    elif throttle_in < previous_throttle:
        pyautogui.press('g', presses=previous_throttle - throttle_in)

    if train_brake_in > previous_train_brake:
        pyautogui.press('u', presses=train_brake_in - previous_train_brake)
    elif train_brake_in < previous_train_brake:
        pyautogui.press('j', presses=previous_train_brake - train_brake_in +1)

    if ind_brake_in > previous_ind_brake:
        pyautogui.press('i', presses=ind_brake_in - previous_ind_brake)
    elif ind_brake_in < previous_ind_brake:
        pyautogui.press('k', presses=previous_ind_brake - ind_brake_in)

    previous_throttle = throttle_in
    previous_train_brake = train_brake_in
    previous_ind_brake = ind_brake_in




if __name__ == "__main__":
    device_name = "Arduino Mega 2560"  # Specify the device name
    try:
        read_usb_port(device_name)  # Try reading from USB port with the specified name
    except serial.SerialException:
        print(f"Error: Unable to read data from USB port with name '{device_name}'.")
