LED clignoter en alternance:
// Déclaration des broches pour les LEDs
const int led1 = 9; // LED 1 connectée à la broche 9
const int led2 = 10; // LED 2 connectée à la broche 10

// Durée d'allumage/extinction (en millisecondes)
const int delayTime = 500; // Temps de 500 ms

void setup() {
  // Configurer les broches comme sorties
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  // Allumer LED 1 et éteindre LED 2
  digitalWrite(led1, HIGH);
  digitalWrite(led2, LOW);
  delay(delayTime); // Attendre 500 ms

  // Éteindre LED 1 et allumer LED 2
  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);
  delay(delayTime); // Attendre 500 ms
}


Chenillard:
// Déclaration des broches pour les LEDs
const int ledPins[] = {9, 10, 11, 12, 13}; // LEDs connectées aux broches 9 à 13
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]); // Nombre de LEDs

// Durée d'allumage/extinction (en millisecondes)
const int delayTime = 200; // Temps de 200 ms

void setup() {
  // Configurer toutes les broches comme sorties
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW); // Assurez-vous que toutes les LEDs sont éteintes au démarrage
  }
}

void loop() {
  // Allumer les LEDs une par une dans un sens
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(ledPins[i], HIGH);
    delay(delayTime);
    digitalWrite(ledPins[i], LOW);
  }

  // Allumer les LEDs une par une dans l'autre sens
  for (int i = numLeds - 1; i >= 0; i--) {
    digitalWrite(ledPins[i], HIGH);
    delay(delayTime);
    digitalWrite(ledPins[i], LOW);
  }
}




LED qui reste allumee 1 seconde:
// Déclaration des broches
const int ledPin = 10; // LED connectée à la broche 10
const int buttonPin = A1; // Bouton connecté à la broche A1

// Variables pour stocker l'état du bouton
int buttonState = 0; // État actuel du bouton

void setup() {
  pinMode(ledPin, OUTPUT); // Configurer la broche LED comme sortie
  pinMode(buttonPin, INPUT); // Configurer la broche du bouton comme entrée
  digitalWrite(ledPin, LOW); // Assurez-vous que la LED est éteinte au démarrage
}

void loop() {
  // Lire l'état du bouton
  buttonState = digitalRead(buttonPin);

  // Vérifier si le bouton est pressé
  if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH); // Allumer la LED
    delay(3000); // Attendre 3 secondes
    digitalWrite(ledPin, LOW); // Éteindre la LED
  }
}




Chenillard dans tout les sens:
// Déclaration des broches pour les LEDs et le bouton
const int ledPins[] = {9, 10, 11, 12}; // LEDs connectées aux broches 9 à 12
const int buttonPin = A1; // Bouton connecté à la broche A1
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]); // Nombre de LEDs

void setup() {
  // Configurer toutes les broches LED comme sorties
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW); // Éteindre toutes les LEDs au démarrage
  }

  // Configurer la broche du bouton comme entrée
  pinMode(buttonPin, INPUT);
}

void loop() {
  // Lire l'état du bouton
  int buttonState = digitalRead(buttonPin);

  if (buttonState == LOW) {
    // Chenillard de D1 vers D4
    for (int i = 0; i < numLeds; i++) {
      digitalWrite(ledPins[i], HIGH);
      delay(200); // Attendre 200 ms
      digitalWrite(ledPins[i], LOW);
    }
  } else {
    // Chenillard de D4 vers D1
    for (int i = numLeds - 1; i >= 0; i--) {
      digitalWrite(ledPins[i], HIGH);
      delay(200); // Attendre 200 ms
      digitalWrite(ledPins[i], LOW);
    }
  }
}




Chenillard et clignoter de 4 LED boutons:
// Déclaration des broches pour les LEDs et les boutons
const int ledPins[] = {9, 10, 11, 12}; // LEDs connectées aux broches 9 à 12
const int buttonA1 = A1; // Bouton A1 pour chenillard dans un sens
const int buttonA2 = A2; // Bouton A2 pour clignotement
const int buttonA3 = A3; // Bouton A3 pour chenillard dans l'autre sens
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]); // Nombre de LEDs

void setup() {
  // Configurer toutes les broches LED comme sorties
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW); // Éteindre toutes les LEDs au démarrage
  }

  // Configurer les broches des boutons comme entrées
  pinMode(buttonA1, INPUT);
  pinMode(buttonA2, INPUT);
  pinMode(buttonA3, INPUT);
}

void loop() {
  // Lire l'état des boutons
  int stateA1 = digitalRead(buttonA1);
  int stateA2 = digitalRead(buttonA2);
  int stateA3 = digitalRead(buttonA3);

  if (stateA1 == HIGH) {
    // Chenillard de D1 vers D4
    for (int i = 0; i < numLeds; i++) {
      digitalWrite(ledPins[i], HIGH);
      delay(200); // Attendre 200 ms
      digitalWrite(ledPins[i], LOW);
    }
  } else if (stateA2 == HIGH) {
    // Clignotement des 4 LEDs
    for (int i = 0; i < 4; i++) { // Faire clignoter 4 fois
      for (int j = 0; j < numLeds; j++) {
        digitalWrite(ledPins[j], HIGH);
      }
      delay(300); // LEDs allumées 300 ms
      for (int j = 0; j < numLeds; j++) {
        digitalWrite(ledPins[j], LOW);
      }
      delay(300); // LEDs éteintes 300 ms
    }
  } else if (stateA3 == HIGH) {
    // Chenillard de D4 vers D1
    for (int i = numLeds - 1; i >= 0; i--) {
      digitalWrite(ledPins[i], HIGH);
      delay(200); // Attendre 200 ms
      digitalWrite(ledPins[i], LOW);
    }
  }
}




Instatement changement d'état:
// Déclaration des broches pour les LEDs et les boutons
const int ledPins[] = {9, 10, 11, 12}; // LEDs connectées aux broches 9 à 12
const int buttonA1 = A1; // Bouton A1 pour changer de direction du chenillard
const int buttonA2 = A2; // Bouton A2 pour clignotement
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]); // Nombre de LEDs

// Variables pour le chenillard
int direction = 1; // 1 pour D1 -> D4, -1 pour D4 -> D1
int currentLed = 0;

void setup() {
  // Configurer toutes les broches LED comme sorties
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW); // Éteindre toutes les LEDs au démarrage
  }

  // Configurer les broches des boutons comme entrées
  pinMode(buttonA1, INPUT);
  pinMode(buttonA2, INPUT);
}

void loop() {
  // Lire l'état des boutons
  int stateA1 = digitalRead(buttonA1);
  int stateA2 = digitalRead(buttonA2);

  if (stateA1 == HIGH) {
    // Inverser la direction du chenillard si le bouton A1 est appuyé
    direction = -direction;
    delay(300); // Anti-rebond pour éviter les changements multiples
  }

  if (stateA2 == HIGH) {
    // Clignotement des 4 LEDs
    for (int i = 0; i < 4; i++) { // Faire clignoter 4 fois
      for (int j = 0; j < numLeds; j++) {
        digitalWrite(ledPins[j], HIGH);
      }
      delay(300); // LEDs allumées 300 ms
      for (int j = 0; j < numLeds; j++) {
        digitalWrite(ledPins[j], LOW);
      }
      delay(300); // LEDs éteintes 300 ms
    }
  } else {
    // Chenillard avec changement instantané de direction
    digitalWrite(ledPins[currentLed], HIGH);
    delay(200); // Attendre 200 ms
    digitalWrite(ledPins[currentLed], LOW);

    // Calculer la prochaine LED en fonction de la direction
    currentLed += direction;

    // Gérer les limites du chenillard
    if (currentLed >= numLeds) {
      currentLed = numLeds - 2;
      direction = -1;
    } else if (currentLed < 0) {
      currentLed = 1;
      direction = 1;
    }
  }
}



Affichage de LED suivant un seuil:
// Déclaration des broches pour la LED et le potentiomètre
const int ledPin = 10; // LED connectée à la broche 10
const int potPin = A0; // Potentiomètre connecté à la broche A0

void setup() {
  // Configurer la broche LED comme sortie
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW); // Assurez-vous que la LED est éteinte au démarrage
}

void loop() {
  // Lire la valeur analogique du potentiomètre
  int potValue = analogRead(potPin);

  // Allumer la LED si la valeur est supérieure à 500
  if (potValue > 500) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
}





Chenillard a Vitesse variable:
// Déclaration des broches pour les LEDs et le potentiomètre
const int led1 = 9; // LED 1 connectée à la broche 9
const int led2 = 10; // LED 2 connectée à la broche 10
const int led3 = 11; // LED 3 connectée à la broche 11
const int led4 = 12; // LED 4 connectée à la broche 12
const int potPin = A0; // Potentiomètre connecté à la broche A0

// Variables pour le chenillard
int currentLed = 9; // LED active actuelle
int direction = 1; // Direction du chenillard (1 ou -1)

void setup() {
  // Configurer les broches LED comme sorties
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);

  // Éteindre toutes les LEDs au démarrage
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);
}

void loop() {
  // Lire la valeur analogique du potentiomètre
  int potValue = analogRead(potPin);

  // Calculer la pause en fonction de la valeur du potentiomètre
  int delayTime = map(potValue, 0, 1023, 50, 1000); // Pause entre 50 ms et 1000 ms

  // Allumer la LED actuelle
  digitalWrite(currentLed, HIGH);
  delay(delayTime); // Pause définie par le potentiomètre
  digitalWrite(currentLed, LOW);

  // Passer à la LED suivante
  currentLed += direction;

  // Gérer les limites du chenillard
  if (currentLed > 12) { // Si on dépasse la LED 4
    currentLed = 11;
    direction = -1;
  } else if (currentLed < 9) { // Si on dépasse la LED 1
    currentLed = 10;
    direction = 1;
  }
}



Utilisation de map:
// Déclaration des broches pour les LEDs et le potentiomètre
const int led1 = 9; // LED 1 connectée à la broche 9
const int led2 = 10; // LED 2 connectée à la broche 10
const int led3 = 11; // LED 3 connectée à la broche 11
const int led4 = 12; // LED 4 connectée à la broche 12
const int potPin = A0; // Potentiomètre connecté à la broche A0

void setup() {
  // Configurer les broches LED comme sorties
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);

  // Éteindre toutes les LEDs au démarrage
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);
}

void loop() {
  // Lire la valeur analogique du potentiomètre
  int potValue = analogRead(potPin);

  // Convertir la valeur en millivolts (valeur max ADC = 5V = 5000mV)
  int voltage = map(potValue, 0, 1023, 0, 5000);

  // Allumer ou éteindre LED 4
  if (voltage > 500) {
    digitalWrite(led4, HIGH);
  } else {
    digitalWrite(led4, LOW);
  }

  // Allumer ou éteindre LED 3
  if (voltage > 1000) {
    digitalWrite(led3, HIGH);
  } else {
    digitalWrite(led3, LOW);
  }

  // Allumer ou éteindre LED 2
  if (voltage > 1500) {
    digitalWrite(led2, HIGH);
  } else {
    digitalWrite(led2, LOW);
  }

  // Allumer ou éteindre LED 1
  if (voltage > 2000) {
    digitalWrite(led1, HIGH);
  } else {
    digitalWrite(led1, LOW);
  }
}



PWM test, frequence de 0.5Hz
// Déclaration des broches pour les LEDs et le potentiomètre
const int led1 = 9; // LED 1 connectée à la broche 9
const int led2 = 10; // LED 2 connectée à la broche 10
const int potPin = A0; // Potentiomètre connecté à la broche A0

void setup() {
  // Configurer les broches LED comme sorties
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

  // Éteindre toutes les LEDs au démarrage
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
}

void loop() {
  // Lire la valeur analogique du potentiomètre
  int potValue = analogRead(potPin);

  // Convertir la valeur pour déterminer la période (en ms) de clignotement
  int period = map(potValue, 0, 1023, 2, 1000); // Période entre 2 ms (500 Hz) et 1000 ms (0.5 Hz)

  // Faire clignoter LED 1
  digitalWrite(led1, HIGH);
  delay(period / 2); // Temps d'allumage (50% du cycle)
  digitalWrite(led1, LOW);
  delay(period / 2); // Temps d'extinction (50% du cycle)

  // Garder LED 2 allumée en continu
  digitalWrite(led2, HIGH);
}




Luminosite en function de potentiometer
// Déclaration des broches pour les LEDs et le potentiomètre
const int led1 = 9; // LED 1 connectée à la broche 9
const int potPin = A0; // Potentiomètre connecté à la broche A0

void setup() {
  // Configurer les broches LED comme sorties
  pinMode(led1, OUTPUT);
}

void loop() {
  // Lire la valeur analogique du potentiomètre
  int potValue = analogRead(potPin);

  // Convertir la valeur pour PWM (0 à 255)
  int pwmValue = map(potValue, 0, 1023, 0, 255);

  // Régler la luminosité de la LED
  analogWrite(led1, pwmValue);
}



Sirene en buzzer:
// Déclaration des broches pour les LEDs, potentiomètre et buzzer
const int led1 = 9; // LED 1 connectée à la broche 9
const int potPin = A0; // Potentiomètre connecté à la broche A0
const int buzzerPin = 3; // Buzzer connecté à la broche 3

void setup() {
  // Configurer les broches LED et buzzer comme sorties
  pinMode(led1, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // Lire la valeur analogique du potentiomètre
  int potValue = analogRead(potPin);

  // Convertir la valeur pour PWM (0 à 255)
  int pwmValue = map(potValue, 0, 1023, 0, 255);

  // Régler la luminosité de la LED
  analogWrite(led1, pwmValue);

  // Générer une sirène avec le buzzer
  for (int freq = 500; freq <= 1000; freq += 10) { // Monter en fréquence
    tone(buzzerPin, freq);
    delay(10);
  }
  for (int freq = 1000; freq >= 500; freq -= 10) { // Descendre en fréquence
    tone(buzzerPin, freq);
    delay(10);
  }
}





Serial monitor.
Envoyer lettres par appuie les boutons
// Déclaration des broches pour les LEDs, potentiomètre, buzzer et boutons
const int led1 = 9; // LED 1 connectée à la broche 9
const int potPin = A0; // Potentiomètre connecté à la broche A0
const int buzzerPin = 3; // Buzzer connecté à la broche 3
const int buttonLeft = 4; // Bouton gauche connecté à la broche 4
const int buttonCenter = 5; // Bouton centre connecté à la broche 5
const int buttonRight = 6; // Bouton droit connecté à la broche 6

// Variables pour l'état des boutons
bool lastStateLeft = LOW;
bool lastStateCenter = LOW;
bool lastStateRight = LOW;

void setup() {
  // Configurer les broches LED, buzzer et boutons comme entrées/sorties
  pinMode(led1, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(buttonLeft, INPUT);
  pinMode(buttonCenter, INPUT);
  pinMode(buttonRight, INPUT);

  // Initialiser la communication série
  Serial.begin(9600);
}

void loop() {
  // Lire l'état des boutons
  bool currentStateLeft = digitalRead(buttonLeft);
  bool currentStateCenter = digitalRead(buttonCenter);
  bool currentStateRight = digitalRead(buttonRight);

  // Vérifier les changements d'état et envoyer les lettres correspondantes
  if (currentStateLeft == HIGH && lastStateLeft == LOW) {
    Serial.println("A");
  }
  if (currentStateCenter == HIGH && lastStateCenter == LOW) {
    Serial.println("B");
  }
  if (currentStateRight == HIGH && lastStateRight == LOW) {
    Serial.println("C");
  }

  // Mettre à jour les derniers états des boutons
  lastStateLeft = currentStateLeft;
  lastStateCenter = currentStateCenter;
  lastStateRight = currentStateRight;

  // Petit délai pour éviter les rebonds
  delay(50);
}




Allumer led si donne arrive
// Configuration pour une carte Arduino

// Définir la broche de la LED
#define LED_PIN 2  // D1 correspond à la broche numérique 2

void setup() {
  // Configurer la broche LED comme sortie
  pinMode(LED_PIN, OUTPUT);

  // Initialiser la communication série
  Serial.begin(9600);
}

void loop() {
  // Vérifier si des données sont disponibles sur le port série
  if (Serial.available() > 0) {
    // Lire les données reçues (même si elles ne sont pas utilisées ici)
    char data = Serial.read();

    // Allumer la LED
    digitalWrite(LED_PIN, HIGH);

    // Attendre 200 ms
    delay(200);

    // Éteindre la LED
    digitalWrite(LED_PIN, LOW);
  }
}



Caractere recu
// Configuration pour une carte Arduino

// Définir la broche de la LED
#define LED_PIN 2  // D1 correspond à la broche numérique 2

void setup() {
  // Configurer la broche LED comme sortie
  pinMode(LED_PIN, OUTPUT);

  // Initialiser la communication série
  Serial.begin(9600);
}

void loop() {
  // Vérifier si des données sont disponibles sur le port série
  if (Serial.available() > 0) {
    // Lire les données reçues
    char data = Serial.read();

    // Afficher "caractere recu"
    Serial.println("Caractere recu");

    // Afficher le caractère et sa valeur ASCII
    Serial.print("Caractere: ");
    Serial.print(data);
    Serial.print(" | ASCII: ");
    Serial.println((int)data);

    // Allumer la LED
    digitalWrite(LED_PIN, HIGH);

    // Attendre 200 ms
    delay(200);

    // Éteindre la LED
    digitalWrite(LED_PIN, LOW);
  }
}

