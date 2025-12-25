# Image Acquisition

## 成像原理

### 光照与阴影

* 光源
* 反射

### sensor type

## Image Acquisition

### 采样与量化

* 连续信号—（采样与量化）—>离散信号
* <img src="../../../../Users/eleev/AppData/Roaming/Typora/typora-user-images/image-20240221080949445.png" alt="image-20240221080949445" style="zoom:50%;" />
* <img src="../../../../Users/eleev/AppData/Roaming/Typora/typora-user-images/image-20240221081032509.png" alt="image-20240221081032509" style="zoom:50%;" />

___

# Image Representation



## Basic Elements We Can Use

* grayscale(灰度)/intensity
  * 0： 黑色
  * 255：白色
  * tech: grayscale conversion
* color
  * RGB
  * tech: color histogram
* Scale and Resolution
  * resolution:分辨率是指图像或显示器上可见的像素数量，通常以水平像素数乘以垂直像素数表示。在数字图像处理中，分辨率描述了图像的细节水平，以像素为单位。例如，一个分辨率为1920x1080的图像意味着它在水平方向有1920个像素，在垂直方向有1080个像素。分辨率越高，图像的细节就越丰富，清晰度就越高。

* texture

* shape
* motion

## image segment

* color region
* texture region
* line clusters

## representation

### image as a matrix

### image as a function

* 自变量是坐标

## image transformation

* Lightening the image
  * f(x,y)=f(x,y)+20
*  Flipping the image
  * f(x,y)=f(-x,y)

## image quality

### sampling

* 像素数(pixel)

### quantization

* 灰度级（Gray Level）
  * 指图像中每个像素的亮度级别。在灰度图像中，每个像素的亮度可以用数字来表示，通常在0到255之间，其中0表示黑色，255表示白色，其他数字则表示不同程度的灰度。这些数字代表了像素的强度或亮度，它们构成了图像的灰度级。
  * 例如，一个8位灰度图像具有256个灰度级，因为它的像素可以采用0到255之间的任何整数值来表示。更高位深度的图像可以具有更多的灰度级，从而提供更丰富的亮度信息。
* <img src="../../../../Users/eleev/AppData/Roaming/Typora/typora-user-images/image-20240221083029890.png" alt="image-20240221083029890" style="zoom: 50%;" />
* 表示的明暗度范围是一样的，但是分级不同

###  对比度

* contrast

  * **Contrast** = Highest / lowest

* 对比度（Contrast）是指图像或场景中不同元素之间亮度差异的程度。在图像处理中，对比度描述了图像中不同区域之间的亮度差异，即图像中相邻像素之间的灰度级别差异程度。

  高对比度意味着图像中相邻区域之间的亮度差异很大，而低对比度意味着这种差异较小。在一幅图像中，增加对比度会使图像中的亮部变得更亮，暗部变得更暗，使得图像更加清晰，而减少对比度则会使得亮度级别之间的差异减小，图像看起来更加柔和。

  调整对比度是图像处理中常见的一种操作，通过增加或减少图像的对比度，可以改善图像的视觉效果，使得图像更具有吸引力和清晰度。

### 亮度

* intensity

### 尺寸

### 饱和度

* Saturation

* 饱和度（Saturation）是指图像或颜色的鲜艳程度或**纯度**。在色彩模型中，饱和度描述了颜色的强度和纯度，即颜色是否倾向于是纯色还是混合了其他颜色。

  在RGB（红、绿、蓝）颜色模型中，饱和度表示着颜色相对于灰色的程度。具有高饱和度的颜色更加鲜艳和鲜明，而低饱和度的颜色则更加灰暗或灰白。**在HSL（色相、饱和度、亮度）颜色模型中，饱和度是指色彩的纯度或强度，取值范围通常在0到1之间，0表示灰色，1表示全彩**。增加饱和度会使颜色更加鲜艳，而减少饱和度则会使颜色变得更加灰暗或淡化。

  总之，饱和度是描述颜色鲜艳程度或纯度的量度，它对于图像处理和调整颜色效果非常重要。

### 灰度

* levels

___

# image format



___

# image processing operations

## point operations

### 一些规定

* 输入图像 f(x,y)
* 输出图像g(x,y)

* ![img](https://miro.medium.com/v2/resize:fit:626/1*60G8Mg4pukPzqC56HvFywA.png)

### e.g.

* 反转对比度
* ![img](https://miro.medium.com/v2/resize:fit:618/1*ef3QB7zWuAgzm_PVh-mXrQ.png)
  * 这里，I（x，y） 代表图像 I 坐标 （x，y） 处的强度值。Imₐₓ 和 Imin 是指图像 I 的最大和最小强度值。例如，假设图像 I 的强度介于 0 和 255 之间。因此，Imₐₓ 和 Imin 分别变为 255 和 0。您希望在坐标处翻转强度值，例如 （x，y），其中当前强度值为 5。通过使用上述操作，您可以得到以下输出：（255） — 5 + 0 = 250，这将是坐标 （x，y） 处强度的新值。
* 线性操作
  * D2=aD1+b
* 非线性操作

### 常见操作

* 对比度调整
* 阈值操作
* 剪裁
* 光度校准

### algebraic operation

* 像素的加减乘除

* 加法

  * 去噪

    <img src="../../../../Users/eleev/AppData/Roaming/Typora/typora-user-images/image-20240226162659105.png" alt="image-20240226162659105" style="zoom:50%;" />

  * 双重曝光

* 减法

  * 移动物体的检测

  * 去背景/分割

    * 方法1(background substraction)

      * 再拍一张只有背景的
      * <img src="../../../../Users/eleev/AppData/Roaming/Typora/typora-user-images/image-20240226163303492.png" alt="image-20240226163303492" style="zoom:50%;" />
      * 缺点：
        * 有阴影变化
        * 必须要求相机是静止的

      

    * 方法2：背景估计
      * 把图像分块
      * 取强度最小值
      * 估计背景
      * 减去背景
      * 调整对比度

* 乘法

  * 二值图像蒙版（mask

* 除法

  * 图像增强

### geometric operation

* 缩放
  * 坐标操作
    * 缩放
* 平移与旋转
  * 坐标操作
    * 数学操作
      * 矩阵的坐标变换
* 镜像处理

## local operations

* ![img](https://miro.medium.com/v2/resize:fit:686/1*NlSMHrken_n4vlomP3Gikg.png)
* e.g.
  * 去除噪点（窗口平滑操作）

## global operations

* ![img](https://miro.medium.com/v2/resize:fit:753/1*dzqD1QG8VMb6-kvBZtYjNw.png)
* e.g.
  * 傅里叶变换
  * ![img](https://miro.medium.com/v2/resize:fit:777/1*TkDhNN4lFmeAwuoZZvHx_w.png)



## basic operations

### Binary image analysis

* 颜色通道提取
* binary image analysis
  * 0： 背景
  * 1： 前景
  * 可以用于简单的字符识别，齿轮检测识别，医学图像
  * 失去了色彩信息，能够反映物体的**轮廓结构**

* 阈值分析（图像分割）
  * 灰度图像------>二值图像
  * 阈值不仅仅是颜色通道，也可以是纹理信息，亮度信息
    * 用于简单的图像分析
  * method
    * fixed/global threshold
      * 正向
      * 反向
      * 单阈值
      * 双阈值
    * 最优化阈值算法
    * 自动阈值法
      * automatic thresholding
  * 需要根据图像特征（直方图），选择阈值
    * 选择两个明显的峰之间，有一个明显的谷
    * ![null](https://images.prismic.io/encord/bad5e8ba-67b4-48a3-b800-b0c9097756f9_image2.png?auto=compress,format)

* 具体步骤（brain storming)
  * 1. 灰度图像
    2. 提取每个像素的灰度值（0，255）
    3. 直方图统计（横坐标0-255）
    4. 找到明显的峰和谷
    5. 如果谷有一个
       1. 那么就是谷附近的值作为阈值
    6. 如果谷有多个，
       1. 那么进行多个谷进行迭代
    7. 进行二值化处理
    8. 进行二值图比较
       1. 选择最好的那个结构图
  * 或者进行255取步长为n的迭代
  * 进行局部的灰度降维，再进行迭代
* 缺点
  * 适用于结构按照强度/灰度差别大的图片

#### Isodata Algorithm

#### optimal thresholding

### interpolation algorithm

#### 最近邻插值（Nearest Neighbor Interpolation)

* 算法
  * 取最近的点的值
  * 在中间的，取左上角
* 缺陷
  * 有锯齿

#### 双线性插值(Bilinear/Square Interpolation)

* 算法
  * 考虑了两个方向的插值
    * 先算一个方向
    * 用算出来的作为待算值计算另一个方向
  * 杠杆lever计算
* 缺点
  * 边缘模糊（低通滤波）

#### 最近邻与双线性的比较

* 最近邻适合原图就有像素分明的（比如像素图）
* 双线性具有平滑模糊作用

#### 高阶插值(Higher Order)

* B样条
* 多项式



### 形变

#### 形变效果

* 球面
* 水波

