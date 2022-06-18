
/*
 * Sets up the serial port.
 */
void setup() {
  Serial.begin(9600);
}

/*
 * Writes "Hello World!" to the serial port.
 */
void loop() {
  Serial.write("Hello World");
}
