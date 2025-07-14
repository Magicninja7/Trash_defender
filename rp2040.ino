#include <Adafruit_NeoPixel.h>

#define MOTION_PIN 1     
#define LED_PIN    2    
#define NUM_LEDS   34     

Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pinMode(MOTION_PIN, INPUT);
  strip.begin();
  strip.show();  
}

void loop() {
  if (digitalRead(MOTION_PIN) == HIGH) {
    for (int i = 0; i < NUM_LEDS; i++) {
      strip.setPixelColor(i, strip.Color(255, 100, 0)); 
    }
    strip.show();
  } else {
    for (int i = 0; i < NUM_LEDS; i++) {
      strip.setPixelColor(i, 0);
    }
    strip.show();
  }

  delay(100);
}


