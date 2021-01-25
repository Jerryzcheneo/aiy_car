let signal = 0
basic.forever(function () {
    signal = pins.digitalReadPin(DigitalPin.P0) * 4 + pins.digitalReadPin(DigitalPin.P10) * 2 + pins.digitalReadPin(DigitalPin.P15)
    if (signal == 1) {
        servos.P1.run(30)
        servos.P2.run(-30)
    }
    if (signal == 2) {
        servos.P1.run(50)
        servos.P2.run(-50)
    }
    if (signal == 3) {
        servos.P1.run(50)
        servos.P2.run(-50)
    }
})
