input.onPinPressed(TouchPin.P0, function () {
    radio.sendNumber(3)
    basic.showString("HELLLO!!")
})
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        basic.showIcon(IconNames.Happy)
    } else if (receivedNumber == 1) {
        basic.showIcon(IconNames.Sad)
    } else if (receivedNumber == 2) {
        basic.showIcon(IconNames.Asleep)
    } else if (receivedNumber == 3) {
        basic.showString("HELLO!!")
    } else if (receivedNumber == 4) {
        basic.showString("BYE!!")
    } else {
        basic.showString("SUS")
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(0)
    basic.showIcon(IconNames.Happy)
})
input.onPinPressed(TouchPin.P2, function () {
    radio.sendNumber(5)
    basic.showString("SUS")
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(2)
    basic.showIcon(IconNames.Asleep)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(1)
    basic.showIcon(IconNames.Sad)
})
input.onPinPressed(TouchPin.P1, function () {
    radio.sendNumber(4)
    basic.showString("BYE!!")
})
radio.setGroup(12)
