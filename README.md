# ROS_ServoDriverHAT

PCA9685HAT基盤をRaspberry pi で使うためのROSパッケージ.  
最大で16台のサーボモータを同時に指定した角度に動かすことができます.

---

## 動作環境
- Raspberry pi 3 b+
- ubuntu 20.04 server
- ROS Noetic

---

## 前提条件
- 本パッケージは[千葉工業大学ロボットシステム学の講義](https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md)内で作成したパッケージに変更を加えたものです.また,それに合わせて[講義内の環境構築方法](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server)に沿って進めております.
- [PCA9685 ServoDriverHATデータシート](https://www.waveshare.com/wiki/Servo_Driver_HAT)

---

## 使うもの
- Raspberry pi 3b+
- PCA9685 ServoDriverHAT
- Futaba s3003 (同シリーズs3010でも動作確認をしております)
- 12V 直流電源 (RAspberry piの電源も兼ねます)

---

## 取り付け方法
1. Raspberry piのgpioピンにHAT基盤を取り付ける.
2. 信号線,電源,GNDの向きに注意してサーボのケーブルをHAT基板に取り付ける.
3. 12Vの出力端子をHAT基板に注意して取り付ける.
4. 配線を確認し , 12V電源をオンにする.
![配線図](https://user-images.githubusercontent.com/53966307/104864030-2b76fd80-597b-11eb-9f30-befaafae9031.PNG)

---

## インストール方法
### このパッケージ
```bash
cd ~/catkin_ws/src  
```
```bash
git clone https://github.com/mibuchiyuta/ROS_ServoDriverHAT  
```
```bash
cd ~/catkin_ws  
```
```bash
catkin_make  
```
```bash
source ~/.bashrc
```
### I2Cの有効化
ファイルの編集をする
```bash
sudo vi /boot/firmware/config.txt
```
```txt
...
include syscfg.txt
include usercfg.txt

dtparam=i2c_arm=on #末尾にこの行を追加
```
```bash
sudo vi /etc/modules
```
```
...
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.

i2c-dev
i2c-bcm2708 #末尾にこの2行を追加
```
その後再起動してツールのインストールを行う
```bash
sudo reboot  
```
```bash
sudo apt install i2c-tools  
```
```bash
sudo apt install python3-smbus
```

### [Adafruit Python PCA9685](https://github.com/adafruit/Adafruit_Python_PCA9685) のインストール
```bash
sudo apt install python-pip python3-pip  
```
```bash
sudo apt-get install git build-essential python-dev  
```
```bash
cd ~
```
```bash
git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
```
```bash
cd Adafruit_Python_PCA9685
```
```bash
sudo python3 setup.py install
```
```bash
sudo pip install adafruit-pca9685
```

---

## 使用方法1
roslaunch を使う方法
```bash
cd ~/catkin_ws/
```
```bash
roslaunch servo_hat servo_hat.launch
```
```bash
...
process[deg_change-2]: started with pid [9555]
process[pulse_out-3]: started with pid [9560]

#0〜180の数字を入力
```

---

## 使用方法2
端末を2画面にし,rosrunを使う方法.
### 端末１
```bash 
cd ~/catkin_ws/
```
```bash
rosrun servo_hat servo_hat.py 
```
### 端末2
```bash 
cd ~/catkin_ws/
```
```bash
rosrun servo_hat input_deg.py
```
```
deg = #0〜180の数字を入力
```

---

## パルス変換の計算式
計測を行ったところ,s3003を0度から180度動かすときのパルス幅は100から570であることがわかった.従って以下の計算式をプログラムに用いている.
また他の利用できるサーボモータを使用する場合,パルス幅の値を変えれば使用可能である.
```
deg * (570-100) / 180 + 100 = pulse
```

---

## 動作動画
[![動画](https://user-images.githubusercontent.com/53966307/104864086-5c573280-597b-11eb-9c5f-06ec9a1f227c.jpg)](https://youtu.be/FvdAG-TJGng)

---

## ライセンス
- ROS : [BSD 3-Clause License](https://github.com/MibuchiYuta/ROS_ServoDriverHAT/blob/master/LICENSE)
- Adafruit Python PCA9685 : [MIT License](https://github.com/adafruit/Adafruit_Python_PCA9685/blob/master/LICENSE)
