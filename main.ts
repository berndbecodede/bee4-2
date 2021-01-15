input.onPinPressed(TouchPin.P0, function () {
    basic.showLeds(`
        . # # . .
        # . . # .
        # . . # .
        # . . # .
        . # # . .
        `)
    basic.setLedColor(Colors.Red)
    basic.pause(500)
    basic.setLedColor(Colors.Orange)
    basic.pause(500)
    basic.setLedColor(Colors.Yellow)
    basic.pause(500)
    basic.setLedColor(Colors.Green)
    basic.pause(500)
    basic.setLedColor(Colors.Blue)
    basic.pause(500)
    basic.setLedColor(Colors.Indigo)
    basic.pause(500)
    basic.setLedColor(Colors.Violet)
    basic.pause(500)
    basic.setLedColor(Colors.Purple)
    basic.pause(500)
    basic.setLedColor(Colors.White)
    basic.turnRgbLedOff()
    basic.setLedColor(Colors.Off)
})
input.onPinPressed(TouchPin.P3, function () {
    images.createImage(`
        . . . . #
        . . . . .
        . . # . .
        . . . . .
        # . . . .
        `).showImage(0)
    basic.showString("A or  B")
    while (input.buttonIsPressed(Button.A)) {
        music.playMelody("C D E F G E D C ", 240)
        basic.showString("Hey Mathias :D")
        basic.pause(100)
        basic.setLedColor(0xff0080)
        basic.showIcon(IconNames.Heart)
        basic.turnRgbLedOff()
        basic.showIcon(IconNames.Yes)
        basic.clearScreen()
    }
    while (input.buttonIsPressed(Button.B)) {
        basic.setLedColor(0x00ffff)
        basic.showString("B...")
        basic.turnRgbLedOff()
        basic.pause(100)
        basic.showIcon(IconNames.Happy)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.A, function () {
    basic.showString("A... P1")
    while (input.buttonIsPressed(Button.B)) {
        while (input.pinIsPressed(TouchPin.P1)) {
            basic.showCompass(5000)
            basic.clearScreen()
        }
        break;
while (input.pinIsPressed(TouchPin.P0)) {
            input.calibrateCompass()
            basic.clearScreen()
            basic.showCompass(5000)
        }
    }
})
input.onPinPressed(TouchPin.P2, function () {
    images.createImage(`
        . . . # #
        . . . # #
        . . . . .
        # # . . .
        # # . . .
        `).showImage(0)
    basic.showString("A or  B")
    while (input.buttonIsPressed(Button.A)) {
        basic.showString("beweg mich")
        while (input.isGesture(Gesture.ScreenDown)) {
            basic.setLedColor(0xff0080)
            basic.showIcon(IconNames.Yes)
            basic.turnRgbLedOff()
            basic.clearScreen()
        }
    }
    while (input.buttonIsPressed(Button.B)) {
        basic.setLedColor(0x00ff00)
        basic.showString("B...")
        basic.turnRgbLedOff()
        basic.pause(100)
        basic.showIcon(IconNames.Happy)
        basic.clearScreen()
    }
})
input.onGesture(Gesture.Shake, function () {
    basic.setLedColor(Colors.Green)
    basic.pause(100)
    basic.clearScreen()
    basic.turnRgbLedOff()
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("A+B")
    while (input.pinIsPressed(TouchPin.P0)) {
        music.playTone(262, music.beat(BeatFraction.Sixteenth))
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . # . . .
            . # . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . # # . .
            . # . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . # # . .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . # # .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . # .
            . . # # .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . # .
            . . . # .
            . . . # .
            `)
        basic.showLeds(`
            . . . . .
            . . . # .
            . . . # .
            . . . # .
            . . . . .
            `)
        basic.showLeds(`
            . . . # .
            . . . # .
            . . . # .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . # #
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . #
            . . . . #
            . . . . #
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . . #
            . . . . #
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . #
            . . . . #
            . . . . #
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            . . . # #
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # # #
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # . . .
            # # . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . # . . .
            # . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            `)
        basic.showLeds(`
            . . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            `)
        basic.showLeds(`
            # . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            `)
        basic.showLeds(`
            # . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . #
            `)
        basic.showLeds(`
            # . . . #
            . . . # .
            . . . . .
            . # . . .
            # . . . #
            `)
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        basic.setLedColor(0xff0000)
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
        basic.showLeds(`
            . . # # #
            . . . # #
            . . # . #
            . # . . .
            # . . . .
            `)
        basic.turnRgbLedOff()
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
        basic.showLeds(`
            # . . . .
            . # . . .
            . . # . #
            . . . # #
            . . # # #
            `)
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
        basic.clearScreen()
    }
    while (input.pinIsPressed(TouchPin.P3)) {
        music.playTone(523, music.beat(BeatFraction.Sixteenth))
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . # . . .
            # # . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . # # . .
            . # . . .
            # # . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . # # . .
            . # # . .
            # # . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . # # . .
            . # # . .
            # # # . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . # # . .
            . # # . .
            # # # . .
            . . # . .
            . . . . .
            `)
        basic.showLeds(`
            . # # . .
            . # # . .
            # # # . .
            . . # . .
            . . # . .
            `)
        basic.showLeds(`
            . # # . .
            . # # . .
            # # # . .
            . . # . .
            . . # # .
            `)
        basic.showLeds(`
            . # # . .
            . # # . .
            # # # . .
            . . # # .
            . . # # .
            `)
        basic.showLeds(`
            . # # . .
            . # # . .
            # # # # .
            . . # # .
            . . # # .
            `)
        basic.showLeds(`
            . # # . .
            . # # # .
            # # # # .
            . . # # .
            . . # # .
            `)
        basic.showLeds(`
            . # # # .
            . # # # .
            # # # # .
            . . # # .
            . . # # .
            `)
        basic.showLeds(`
            . # # # #
            . # # # .
            # # # # .
            . . # # .
            . . # # .
            `)
        basic.showLeds(`
            . # # # #
            . # # # #
            # # # # .
            . . # # .
            . . # # .
            `)
        basic.showLeds(`
            . # # # #
            . # # # #
            # # # # #
            . . # # .
            . . # # .
            `)
        basic.showLeds(`
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . . # # .
            `)
        basic.showLeds(`
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . . # . #
            `)
        basic.showLeds(`
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . . . # #
            `)
        basic.showLeds(`
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . . # # #
            `)
        basic.showLeds(`
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . # # # #
            `)
        basic.showLeds(`
            . # # # #
            . # # # #
            # # # # #
            . . # # #
            . # # # #
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            # # . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # . . .
            # # . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . # . . .
            # . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            `)
        basic.showLeds(`
            . . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            `)
        basic.showLeds(`
            . . . . #
            . # . # .
            . . # . .
            . # . . .
            # . . . .
            `)
        basic.showLeds(`
            . . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . .
            `)
        basic.showLeds(`
            . . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        basic.showLeds(`
            # . . . #
            . # . # .
            . . . . .
            . # . # .
            # . . . #
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            # . . . #
            . # . # .
            . . . . .
            . # . # .
            # . . . #
            `)
        basic.showString("ENDE")
        basic.clearScreen()
    }
})
input.onPinPressed(TouchPin.P1, function () {
    basic.showString("1")
    while (input.buttonIsPressed(Button.A)) {
        basic.setLedColor(Colors.Red)
        images.createImage(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            `).showImage(0)
        basic.setLedColor(Colors.Green)
        basic.setLedColor(Colors.Off)
        images.createImage(`
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . # . .
            `).showImage(0)
        images.createImage(`
            . . . . .
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            `).showImage(0)
        images.createImage(`
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            . # . # .
            `).showImage(0)
        images.createImage(`
            . . # . .
            . . # . .
            . . # . .
            . # . # .
            # . . . #
            `).showImage(0)
        images.createImage(`
            . . # . .
            . . # . .
            . # . # .
            # . . . #
            . . . . .
            `).showImage(0)
        images.createImage(`
            . . # . .
            . # . # .
            # . . . #
            . . . . .
            . . . . .
            `).showImage(0)
        images.createImage(`
            . # . # .
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            `).showImage(0)
        images.createImage(`
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `).showImage(0)
        images.createImage(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `).showImage(0)
        images.createImage(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `).showImage(0)
    }
    while (input.buttonIsPressed(Button.B)) {
        basic.setLedColor(Colors.Green)
        images.createImage(`
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            `).showImage(0)
        basic.setLedColor(Colors.Off)
        images.createImage(`
            # . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . #
            `).showImage(0)
        images.createImage(`
            # . . . .
            . # . . .
            . . # . .
            . . . # .
            . . . . #
            `).showImage(0)
        images.createImage(`
            # . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . #
            `).showImage(0)
        images.createImage(`
            # . . . .
            . . . . .
            . . . . .
            . . . # .
            . . . . #
            `).showImage(0)
        images.createImage(`
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            `).showImage(0)
        images.createImage(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            `).showImage(0)
        images.createImage(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `).showImage(0)
        music.playTone(392, music.beat(BeatFraction.Quarter))
        images.createImage(`
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `).showImage(0)
        basic.clearScreen()
    }
})
basic.showString("oN")
music.playTone(277, music.beat(BeatFraction.Half))
