from nightlight import NightLight
import time
import screen_brightness_control as SBC
night_light = NightLight()
night_light.set_strength(100)

def toggleBrightness():
    max = 100
    min = 0
    brightness = SBC.get_brightness()
    if brightness[0] == 100:
        SBC.set_brightness(0)
    else:
        SBC.set_brightness(100)
    
for i in range(100):
    night_light.toggle()
    time.sleep(0.1)
    toggleBrightness()

