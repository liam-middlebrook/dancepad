// pins for the LEDs:
const int redPin = 13;
const int buttonOnePin = 2;
const int buttonTwoPin = 3;
const int buttonThreePin = 4;
const int buttonFourPin = 5;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(redPin, OUTPUT); 
  pinMode(buttonOnePin, INPUT); 
  pinMode(buttonTwoPin, INPUT); 
  pinMode(buttonThreePin, INPUT); 
  pinMode(buttonFourPin, INPUT); 
}

void loop(){}
void serialEvent()
{
    char charX= Serial.read();
    digitalWrite(redPin, charX == '1' ? HIGH : LOW);
    int buttonID = 0;
    buttonID += (digitalRead(buttonOnePin) == HIGH) ? 1 : 0;
    buttonID += (digitalRead(buttonTwoPin) == HIGH) ? 2 : 0;
    buttonID += (digitalRead(buttonThreePin) == HIGH) ? 4 : 0;
    buttonID += (digitalRead(buttonFourPin) == HIGH) ? 8 : 0;
    Serial.write( buttonID + '0');
}

