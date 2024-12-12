input.onButtonPressed(Button.A, function () {
    I2C_LCD1602.clear()
    serial.writeLine("" + ("\r\n"))
})
let y = 0
let x = 0
I2C_LCD1602.LcdInit(0)
serial.redirectToUSB()
I2C_LCD1602.on()
basic.showIcon(IconNames.Heart)
music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.InBackground)
basic.pause(1000)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
I2C_LCD1602.ShowString("Micro:bit-", 0, 0)
I2C_LCD1602.ShowString(control.deviceName(), 0, 1)
basic.pause(2000)
I2C_LCD1602.clear()
I2C_LCD1602.ShowString("Serial-", 0, 0)
I2C_LCD1602.ShowNumber(control.deviceSerialNumber(), 0, 1)
basic.pause(2000)
I2C_LCD1602.clear()
I2C_LCD1602.on()
I2C_LCD1602.BacklightOn()
I2C_LCD1602.clear()
basic.forever(function () {
    x = smarttools.stringToDecimal(serial.readUntil(serial.delimiters(Delimiters.Space)))
    serial.writeString("" + ("\r\n"))
    serial.writeNumber(x)
    basic.pause(100)
    y = smarttools.stringToDecimal(serial.readUntil(serial.delimiters(Delimiters.Space)))
    serial.writeString(" and ")
    serial.writeNumber(y)
    if (x % y == 0) {
        serial.writeString("" + ("\r\n"))
        basic.showIcon(IconNames.Yes)
        music.play(music.builtinPlayableSoundEffect(soundExpression.happy), music.PlaybackMode.InBackground)
        I2C_LCD1602.ShowNumber(x, 0, 0)
        basic.pause(1000)
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("is divisible by", 0, 0)
        basic.pause(1000)
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowNumber(y, 0, 0)
        basic.pause(2000)
        I2C_LCD1602.clear()
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else {
        serial.writeString("" + ("\r\n"))
        basic.showIcon(IconNames.No)
        music.play(music.builtinPlayableSoundEffect(soundExpression.sad), music.PlaybackMode.InBackground)
        I2C_LCD1602.ShowNumber(x, 0, 0)
        basic.pause(1000)
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("is not divisible", 0, 0)
        I2C_LCD1602.ShowString("by", 0, 1)
        basic.pause(1000)
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowNumber(y, 0, 0)
        basic.pause(2000)
        I2C_LCD1602.clear()
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
