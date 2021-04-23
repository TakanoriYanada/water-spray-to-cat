# 猫に水スプレー発射装置

Raspberry piで、猫を検知し、近づいてきたら水スプレーを発射する装置です。  
猫には入ってほしくないエリアの入り口に設置して、侵入を防ぎます。

# デモ
![demo-1](https://user-images.githubusercontent.com/17726777/115885175-a3792600-a48a-11eb-8c8d-9c7f01e54077.gif)


### 実践映像
![demo-2](https://user-images.githubusercontent.com/17726777/115889918-5e0b2780-a48f-11eb-82b9-3822a14c8fe9.gif)


# 機能別デモ

- カメラ起動デモ  
  `/demo/camera_demo.py`
- カメラで猫検知デモ  
  `/demo/recognize_cat_demo.py`
- サーボモータ起動デモ  
  `/demo/camera_demo.py`

# RaspberryPi

<img src="https://user-images.githubusercontent.com/17726777/115890785-44b6ab00-a490-11eb-82fc-a6e250a0b804.jpg" width="250" />

<img src="https://user-images.githubusercontent.com/17726777/115890801-48e2c880-a490-11eb-937e-df900d5354bb.jpg" width="300" />

# 備考

- スプレーの噴射はマイクロサーボモータでは、力不足だったためスタンダードサイズのサーボモータを利用しています
- モバイルバッテリーでRaspberryPiを起動し、電源いらずで起動することもできます
