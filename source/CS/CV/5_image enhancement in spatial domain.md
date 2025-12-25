## contrast enhancement

[:sun_with_face:](https://medium.com/@gokcenazakyol/what-is-image-enhancement-image-processing-3-32a813087e0a)

### gray scale transformation

#### [logarithmic transformation](https://medium.com/@gokcenazakyol/what-is-image-enhancement-image-processing-3-32a813087e0a)

* rules

  <img src="../../../../Users/eleev/AppData/Roaming/Typora/typora-user-images/image-20240306080232830.png" alt="image-20240306080232830" style="zoom:67%;" />

* role
  * 调整曝光
  * The general form of the log transformation is *s = c \* log(1 + r)*
    对数变换的一般形式是 s = c * log（1 + r）
  * The log transformation maps a narrow range of low input grey level values into a wider range of output values.
    对数转换将狭窄范围的低输入灰度级别值映射到范围更广的输出值。
  * The inverse log transformation performs the opposite transformation.
    逆对数转换执行相反的转换。
  * Log functions are particularly useful when the input grey level values may have an extremely large range of values
    当输入灰度级别值可能具有非常大的值范围时，log 函数特别有用

#### exponential transformation

* 注意：
  * 对数：
    * 高值压缩
    * 低值膨胀
  * 指数
    * 高值膨胀
    * 低值压缩

#### linear gray scale transformation

* 基本线性拉伸

* 分段拉伸

<img src="https://miro.medium.com/v2/resize:fit:1050/1*Gn7OR0H61fzDH8Y6otzTEg.png" alt="img" style="zoom:50%;" />

* Gray Level Slicing 灰度水平切片

  ![img](https://miro.medium.com/v2/resize:fit:1050/1*aniZdSvZA9kZLcyvBqSZCg.png)

### histogram adjustment

#### def of histogram

* intensity的分布

#### 信息缺失

保存了f(x,y)的值，失去了(x,y)的信息

#### 直方图均衡（histogram equalization）

##### 直方图的均衡性

##### 全局直方图均衡化

* 正变换

  * gray level:灰度级

  * 

* 逆变换

* 缺点
  * 会缺失图像细节



##### 局部直方图

* 原理
  * 使用邻域kernel，对每个邻域方块内的的直方图进行处理
* 作用
  * 挖掘图像细节

##### 注意

* 直方图均衡可以增加图像的全局对比度
* 直方图均衡不能单独应用于图像的红色、绿色和蓝色分量，因为它会导致图像的色彩平衡发生巨大变化



#### 直方图匹配

##### 直方图均衡化

___

## Noise reduction

### 卷积/均值/box

* filter
  * 单数
  * 全是1
  * 

### 高斯平滑

* filter

  * 基本盒

    1 2 1  (/16)

    2 4 2

    1 2 1

  * 窗宽：n*n

  * 标准差

* 滤波器的参数选择
  * 盒子的边缘应该是接近0
    * 3$\sigma$原则
      * 那么窗宽应该是6$\sigma$​

* 这是个低通滤波器，去除高频成分

* **高斯滤波器在downsize中的作用**（尺寸缩小）

  * 直接下采样会造成图像严重失真
  * 可以预先用高斯滤波器滤波，再进行下采样


> [!note]
>
> * 二维图像里的高频成分： 就是变化比较大的，比如噪声
> * 高斯滤波器和高斯滤波器还是卷积

### 中值滤波

* filter取中值
* **对于椒盐噪声有很好的去噪效果**

> [!caution]
>
> * 这不是均值，是中值

### 形态学滤波



> [!Note]
>
> 互相关&卷积
>
> * 卷积是互相关在水平和竖直方向上的翻转
