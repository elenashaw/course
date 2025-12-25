# edge

> :japanese_ogre:Overview 



## 边缘检测

### 边缘的产生

* 亮度不连续

### 边缘类型

* step edge
* ramp edge
* peak edge

### 边缘检测

#### [differential operator](https://vincmazet.github.io/bip/detection/edges.html)

* 算子类型

  * 1阶

  * 2阶

    * 常用的算子

      <img src="../../../../Users/eleev/AppData/Roaming/Typora/typora-user-images/image-20240311172943767.png" alt="image-20240311172943767" style="zoom:67%;" />

* 阈值+edge
  * 在有噪声的样本中，需要处理阈值
  * 或者预先进行去噪处理