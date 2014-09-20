// pins for the LEDs:
const int redPin = 13;
const int buttonPin = 2;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(redPin, OUTPUT); 
  pinMode(buttonPin, INPUT); 
}

void loop(){}
void serialEvent()
{
    char charX= Serial.read();
    digitalWrite(redPin, charX == '1' ? HIGH : LOW);
    
    Serial.write(digitalRead(buttonPin) == HIGH ? 'A' : 'B');
}

