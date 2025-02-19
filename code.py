import time
import LED

led = LED(17)  # Change 17 to the correct GPIO pin if needed
blink_time = 1  # Initial blink time in seconds

while True:
    led.on()
    time.sleep(blink_time)
    led.off()
    time.sleep(1)
    
    blink_time += 1  # Increase blink time by 1 second
