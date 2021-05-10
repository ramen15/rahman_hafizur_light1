let soil_reading = 0
let dry_value = 1500
while (true) {
    console.log("Light Level: " + input.lightLevel())
    if (input.lightLevel() > 10) {
        light.setPixelColor(0, light.rgb(0, 255, 0))
        light.setPixelColor(1, light.rgb(0, 255, 0))
        light.setPixelColor(2, light.rgb(0, 255, 0))
        light.setPixelColor(3, light.rgb(0, 255, 0))
        light.setPixelColor(4, light.rgb(0, 255, 0))
    } else {
        light.setPixelColor(0, light.rgb(255, 0, 0))
        light.setPixelColor(1, light.rgb(255, 0, 0))
        light.setPixelColor(2, light.rgb(255, 0, 0))
        light.setPixelColor(3, light.rgb(255, 0, 0))
        light.setPixelColor(4, light.rgb(255, 0, 0))
    }
    
}
