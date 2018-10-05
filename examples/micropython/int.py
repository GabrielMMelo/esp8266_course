from machine import Pin
# Should be simple and short as possible. Cannot allocate memory here.
def callback(p):
    print('pin changed', p)
# Pull up resistor
p5 = Pin(5, Pin.IN, Pin.PULL_UP)
p5.irq(trigger=Pin.IRQ_FALLING, handler=callback)
