while True:
    print("Light Level:" + input.light_level())
    if input.light_level() > 5:
        light.set_all(light.rgb(0,0,0))
    else:
        light.set_all(light.rgb(255,255,255))


while True:
    print("Light Level: " + input.light_level())
    if input.light_level() > 15:
        light.clear()
    elif input.light_level() >= 6:
        light.clear()
    else:
        light.set_all(color.rgb(255,165,0))
#thresholds can change from person to person