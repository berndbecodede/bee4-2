def on_pin_pressed_p0():
    basic.show_leds("""
        . # # . .
        # . . # .
        # . . # .
        # . . # .
        . # # . .
        """)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p3():
    images.create_image("""
        . . . . #
        . . . . .
        . . # . .
        . . . . .
        # . . . .
        """).show_image(0)
    basic.show_string("A or  B")
    while input.button_is_pressed(Button.A):
        music.play_melody("C D E F G E D C ", 240)
        basic.show_string("Hey Mathias :D")
        basic.pause(100)
        basic.set_led_color(0xff0080)
        basic.show_icon(IconNames.HEART)
        basic.turn_rgb_led_off()
        basic.show_icon(IconNames.YES)
        basic.clear_screen()
    while input.button_is_pressed(Button.B):
        basic.set_led_color(0x00ffff)
        basic.show_string("B...")
        basic.turn_rgb_led_off()
        basic.pause(100)
        basic.show_icon(IconNames.HAPPY)
        basic.clear_screen()
input.on_pin_pressed(TouchPin.P3, on_pin_pressed_p3)

def on_button_pressed_a():
    basic.show_string("A... P1")
    while input.button_is_pressed(Button.B):
        while input.pin_is_pressed(TouchPin.P1):
            basic.show_compass(5000)
            basic.clear_screen()
        break
        while input.pin_is_pressed(TouchPin.P0):
            input.calibrate_compass()
            basic.clear_screen()
            basic.show_compass(5000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    images.create_image("""
        . . . # #
        . . . # #
        . . . . .
        # # . . .
        # # . . .
        """).show_image(0)
    basic.show_string("A or  B")
    while input.button_is_pressed(Button.A):
        basic.show_string("beweg mich")
        while input.is_gesture(Gesture.SCREEN_DOWN):
            basic.set_led_color(0xff0080)
            basic.show_icon(IconNames.YES)
            basic.turn_rgb_led_off()
            basic.clear_screen()
    while input.button_is_pressed(Button.B):
        basic.set_led_color(0x00ff00)
        basic.show_string("B...")
        basic.turn_rgb_led_off()
        basic.pause(100)
        basic.show_icon(IconNames.HAPPY)
        basic.clear_screen()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_gesture_shake():
    basic.set_led_color(Colors.GREEN)
    basic.pause(100)
    basic.clear_screen()
    basic.turn_rgb_led_off()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_string("A+B")
    while input.pin_is_pressed(TouchPin.P0):
        music.play_tone(262, music.beat(BeatFraction.SIXTEENTH))
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . # . . .
            . # . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . # # . .
            . # . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . # # . .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . # # .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . # .
            . . # # .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . # .
            . . . # .
            . . . # .
            """)
        basic.show_leds("""
            . . . . .
            . . . # .
            . . . # .
            . . . # .
            . . . . .
            """)
        basic.show_leds("""
            . . . # .
            . . . # .
            . . . # .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . # #
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . #
            . . . . #
            . . . . #
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . . #
            . . . . #
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . . . . #
            . . . . #
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            . . . # #
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # # #
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . # . . .
            # # . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . # . . .
            # . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            """)
        basic.show_leds("""
            . . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            """)
        basic.show_leds("""
            # . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            """)
        basic.show_leds("""
            # . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . #
            """)
        basic.show_leds("""
            # . . . #
            . . . # .
            . . . . .
            . # . . .
            # . . . #
            """)
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        basic.set_led_color(0xff0000)
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            """)
        basic.show_leds("""
            . . # # #
            . . . # #
            . . # . #
            . # . . .
            # . . . .
            """)
        basic.turn_rgb_led_off()
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            """)
        basic.show_leds("""
            # . . . .
            . # . . .
            . . # . #
            . . . # #
            . . # # #
            """)
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            """)
        basic.clear_screen()
    while input.pin_is_pressed(TouchPin.P3):
        music.play_tone(523, music.beat(BeatFraction.SIXTEENTH))
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . # . . .
            # # . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . # # . .
            . # . . .
            # # . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . # # . .
            . # # . .
            # # . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . # # . .
            . # # . .
            # # # . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . # # . .
            . # # . .
            # # # . .
            . . # . .
            . . . . .
            """)
        basic.show_leds("""
            . # # . .
            . # # . .
            # # # . .
            . . # . .
            . . # . .
            """)
        basic.show_leds("""
            . # # . .
            . # # . .
            # # # . .
            . . # . .
            . . # # .
            """)
        basic.show_leds("""
            . # # . .
            . # # . .
            # # # . .
            . . # # .
            . . # # .
            """)
        basic.show_leds("""
            . # # . .
            . # # . .
            # # # # .
            . . # # .
            . . # # .
            """)
        basic.show_leds("""
            . # # . .
            . # # # .
            # # # # .
            . . # # .
            . . # # .
            """)
        basic.show_leds("""
            . # # # .
            . # # # .
            # # # # .
            . . # # .
            . . # # .
            """)
        basic.show_leds("""
            . # # # #
            . # # # .
            # # # # .
            . . # # .
            . . # # .
            """)
        basic.show_leds("""
            . # # # #
            . # # # #
            # # # # .
            . . # # .
            . . # # .
            """)
        basic.show_leds("""
            . # # # #
            . # # # #
            # # # # #
            . . # # .
            . . # # .
            """)
        basic.show_leds("""
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . . # # .
            """)
        basic.show_leds("""
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . . # . #
            """)
        basic.show_leds("""
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . . . # #
            """)
        basic.show_leds("""
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . . # # #
            """)
        basic.show_leds("""
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . # # # #
            """)
        basic.show_leds("""
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . # # # #
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            # # . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . # . . .
            # # . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . # . . .
            # . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            """)
        basic.show_leds("""
            . . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            """)
        basic.show_leds("""
            . . . . #
            . # . # .
            . . # . .
            . # . . .
            # . . . .
            """)
        basic.show_leds("""
            . . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . .
            """)
        basic.show_leds("""
            . . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        basic.show_leds("""
            # . . . #
            . # . # .
            . . . . .
            . # . # .
            # . . . #
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            # . . . #
            . # . # .
            . . . . .
            . # . # .
            # . . . #
            """)
        basic.show_string("ENDE")
        basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_pin_pressed_p1():
    basic.show_string("1")
    while input.button_is_pressed(Button.A):
        basic.set_led_color(Colors.RED)
        images.create_image("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            """).show_image(0)
        basic.set_led_color(Colors.GREEN)
        basic.set_led_color(Colors.OFF)
        images.create_image("""
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . # . .
            """).show_image(0)
        images.create_image("""
            . . . . .
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            """).show_image(0)
        images.create_image("""
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            . # . # .
            """).show_image(0)
        images.create_image("""
            . . # . .
            . . # . .
            . . # . .
            . # . # .
            # . . . #
            """).show_image(0)
        images.create_image("""
            . . # . .
            . . # . .
            . # . # .
            # . . . #
            . . . . .
            """).show_image(0)
        images.create_image("""
            . . # . .
            . # . # .
            # . . . #
            . . . . .
            . . . . .
            """).show_image(0)
        images.create_image("""
            . # . # .
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            """).show_image(0)
        images.create_image("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """).show_image(0)
        images.create_image("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """).show_image(0)
        images.create_image("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """).show_image(0)
    while input.button_is_pressed(Button.B):
        basic.set_led_color(Colors.GREEN)
        images.create_image("""
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            """).show_image(0)
        basic.set_led_color(Colors.OFF)
        images.create_image("""
            # . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . #
            """).show_image(0)
        images.create_image("""
            # . . . .
            . # . . .
            . . # . .
            . . . # .
            . . . . #
            """).show_image(0)
        images.create_image("""
            # . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . #
            """).show_image(0)
        images.create_image("""
            # . . . .
            . . . . .
            . . . . .
            . . . # .
            . . . . #
            """).show_image(0)
        images.create_image("""
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            """).show_image(0)
        images.create_image("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            """).show_image(0)
        images.create_image("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """).show_image(0)
        music.play_tone(392, music.beat(BeatFraction.QUARTER))
        images.create_image("""
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """).show_image(0)
        basic.clear_screen()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

basic.show_string("oN")
music.play_tone(277, music.beat(BeatFraction.HALF))
basic.set_led_color(Colors.RED)
basic.pause(500)
basic.set_led_color(Colors.ORANGE)
basic.pause(500)
basic.set_led_color(Colors.YELLOW)
basic.pause(500)
basic.set_led_color(Colors.GREEN)
basic.pause(500)
basic.set_led_color(Colors.BLUE)
basic.pause(500)
basic.set_led_color(Colors.INDIGO)
basic.pause(500)
basic.set_led_color(Colors.VIOLET)
basic.pause(500)
basic.set_led_color(Colors.PURPLE)
basic.pause(500)
basic.set_led_color(Colors.WHITE)
basic.turn_rgb_led_off()
basic.set_led_color(Colors.OFF)