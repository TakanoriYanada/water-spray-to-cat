# 猫に水スプレー発射装置

RaspberryPiで、猫を検知し、近づいてきたら水スプレーを発射する装置です。  
猫には入ってほしくないエリアの入り口に設置して、侵入を防ぎます。

# デモ
<img src="https://user-images.githubusercontent.com/17726777/115885175-a3792600-a48a-11eb-8c8d-9c7f01e54077.gif" width="600" />


### 実践映像
<img src="https://user-images.githubusercontent.com/17726777/115889918-5e0b2780-a48f-11eb-82b9-3822a14c8fe9.gif" width="300" />

# 機能別デモ

- カメラ起動デモ  
  `/demo/camera_demo.py`
- カメラで猫検知デモ  
  `/demo/recognize_cat_demo.py`
- サーボモータ起動デモ  
  `/demo/camera_demo.py`

# 技術
- OpenCVの`lbpcascade_frontalcatface`という猫の顔検出する分類器を利用し実装  
  分類器： https://github.com/opencv/opencv/blob/master/data/lbpcascades/lbpcascade_frontalcatface.xml

# RaspberryPi

- RaspberryPi 4B
- カメラモジュール
- サーボモータ

<img src="https://user-images.githubusercontent.com/17726777/115890785-44b6ab00-a490-11eb-82fc-a6e250a0b804.jpg" width="250" />

<img src="https://user-images.githubusercontent.com/17726777/115890801-48e2c880-a490-11eb-937e-df900d5354bb.jpg" width="300" />

# 水スプレー装置

- 100円均一にあるハンドスプレーに水を入れて利用しています
- ナイロン製のワイヤーを利用し、ハンドスプレーのプッシュするところを経由してサーボモータに取り付けています  
  サーボモータが動くとナイロン製ワイヤーが引っ張られ、ハンドスプレーを自動でプッシュされます  
  ハンドスプレーにサーボモータも固定しています

# 備考

- スプレーの噴射はマイクロサーボモータでは、力不足だったためスタンダードサイズのサーボモータを利用しています
- モバイルバッテリーでRaspberryPiを起動し、電源いらずで起動することもできます
- 当初はRaspberryPi Zero を使用していましたが、猫認識が遅くハンドスプレーが5秒程度遅れていたためPaspberryPi4で運用しています
