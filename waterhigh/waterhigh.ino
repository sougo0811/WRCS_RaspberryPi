//Lesson 58 水位センサ モジュール
//水があるかないかを検出する
//https://omoroya.com/

float val = 0;

void setup() {
  Serial.begin(9600); //シリアル通信のデータ転送レートを9600bpsで指定
}

void loop() {
  delay(10);
  val = analogRead(A0);           //水位センサモジュールの出力電圧の読み取り
  delay(1000);
}