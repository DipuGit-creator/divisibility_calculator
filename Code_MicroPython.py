def on_button_pressed_a():
    I2C_LCD1602.clear()
    serial.write_line("" + ("\r\n"))
input.on_button_pressed(Button.A, on_button_pressed_a)

y = 0
x = 0
I2C_LCD1602.lcd_init(0)
serial.redirect_to_usb()
I2C_LCD1602.on()
basic.show_icon(IconNames.HEART)
music.play(music.builtin_playable_sound_effect(soundExpression.hello),
    music.PlaybackMode.IN_BACKGROUND)
basic.pause(1000)
basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)
I2C_LCD1602.show_string("Micro:bit-", 0, 0)
I2C_LCD1602.show_string(control.device_name(), 0, 1)
basic.pause(2000)
I2C_LCD1602.clear()
I2C_LCD1602.show_string("Serial-", 0, 0)
I2C_LCD1602.show_number(control.device_serial_number(), 0, 1)
basic.pause(2000)
I2C_LCD1602.clear()
I2C_LCD1602.on()
I2C_LCD1602.backlight_on()
I2C_LCD1602.clear()

def on_forever():
    global x, y
    x = smarttools.string_to_decimal(serial.read_until(serial.delimiters(Delimiters.SPACE)))
    serial.write_string("" + ("\r\n"))
    serial.write_number(x)
    basic.pause(100)
    y = smarttools.string_to_decimal(serial.read_until(serial.delimiters(Delimiters.SPACE)))
    serial.write_string(" and ")
    serial.write_number(y)
    if x % y == 0:
        serial.write_string("" + ("\r\n"))
        basic.show_icon(IconNames.YES)
        music.play(music.builtin_playable_sound_effect(soundExpression.happy),
            music.PlaybackMode.IN_BACKGROUND)
        I2C_LCD1602.show_number(x, 0, 0)
        basic.pause(1000)
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("is divisible by", 0, 0)
        basic.pause(1000)
        I2C_LCD1602.clear()
        I2C_LCD1602.show_number(y, 0, 0)
        basic.pause(2000)
        I2C_LCD1602.clear()
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    else:
        serial.write_string("" + ("\r\n"))
        basic.show_icon(IconNames.NO)
        music.play(music.builtin_playable_sound_effect(soundExpression.sad),
            music.PlaybackMode.IN_BACKGROUND)
        I2C_LCD1602.show_number(x, 0, 0)
        basic.pause(1000)
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("is not divisible", 0, 0)
        I2C_LCD1602.show_string("by", 0, 1)
        basic.pause(1000)
        I2C_LCD1602.clear()
        I2C_LCD1602.show_number(y, 0, 0)
        basic.pause(2000)
        I2C_LCD1602.clear()
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
basic.forever(on_forever)
