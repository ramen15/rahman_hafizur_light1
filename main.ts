while (true) {
    console.log("Light Level:" + input.lightLevel())
    if (input.lightLevel() > 5) {
        light.setAll(light.rgb(0, 0, 0))
    } else {
        light.setAll(light.rgb(255, 255, 255))
    }
    
}
while (true) {
    console.log("Light Level: " + input.lightLevel())
    if (input.lightLevel() > 15) {
        light.clear()
    } else if (input.lightLevel() >= 6) {
        light.clear()
    } else {
        light.setAll(color.rgb(255, 165, 0))
    }
    
}
