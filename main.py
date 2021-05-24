while True:
    print("Light Level: " + input.light_level())
    if input.light_level() > 10:
        light.set_pixel_color(0, light.rgb(0,255,0))
        light.set_pixel_color(1, light.rgb(0,255,0))
        light.set_pixel_color(2, light.rgb(0,255,0))
        light.set_pixel_color(3, light.rgb(0,255,0))
        light.set_pixel_color(4, light.rgb(0,255,0))
    else:
        light.set_pixel_color(0, light.rgb(255,0,0))
        light.set_pixel_color(1, light.rgb(255,0,0))
        light.set_pixel_color(2, light.rgb(255,0,0))
        light.set_pixel_color(3, light.rgb(255,0,0))
        light.set_pixel_color(4, light.rgb(255,0,0))

soil_reading = 0
dry_value = 1500

def on_forever():
    pass
    soil_reading = input.pinA1.value()
    print("Soil Reading: " + soil_reading)
    if (soil_reading <= dry_value):
        light.set_pixel_color(5, light.rgb(0,0,255))
        light.set_pixel_color(6, light.rgb(0,0,255))
        light.set_pixel_color(7, light.rgb(0,0,255))
        light.set_pixel_color(8, light.rgb(0,0,255))
        light.set_pixel_color(9, light.rgb(0,0,255))
    else:
        light.set_pixel_color(5, light.rgb(0,255,255))
        light.set_pixel_color(6, light.rgb(0,255,255))
        light.set_pixel_color(7, light.rgb(0,255,255))
        light.set_pixel_color(8, light.rgb(0,255,255))
        light.set_pixel_color(9, light.rgb(0,255,255))
        pause(2000)
    forever(on_forever)