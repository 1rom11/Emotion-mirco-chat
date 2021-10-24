def on_pin_pressed_p0():
    radio.send_number(3)
    basic.show_string("HELLLO!!")
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    radio.send_number(0)
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    radio.send_number(5)
    basic.show_string("SUS")
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    radio.send_number(2)
    basic.show_icon(IconNames.ASLEEP)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(1)
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    radio.send_number(4)
    basic.show_string("BYE!!")
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_icon(IconNames.HAPPY)
    elif receivedNumber == 1:
        basic.show_icon(IconNames.SAD)
    elif receivedNumber == 2:
        basic.show_icon(IconNames.ASLEEP)
    elif receivedNumber == 3:
        basic.show_string("HELLO!!")
    elif receivedNumber == 4:
        basic.show_string("BYE!!")
    else:
        basic.show_string("SUS")
radio.on_received_number(on_received_number)

radio.set_group(12)