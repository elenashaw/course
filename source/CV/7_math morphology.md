# Structure Element

> 其实就是kernel

## INTRO

* origin
  * this is where the definition is based on
* size
* shape
  * 通过1，0可以定义kernel的形状 

## binary dilation

### def

* also called 闵可夫斯基和
* 被一个SE（B）膨胀的图像A，表示成

### 操作结果

* padded image
* dilated image

### role

* 填补空洞
* OCR填补



## binary erosion

### def



### role

* 分离联通的不同物体
* 去噪
  * 复合操作
    * 先腐蚀，后膨胀
    * SE的size选择，基于噪声的size



## 复合操作

### fast operation

两个小的结构元连续去操作，会比一个大的结构元一次性操作更快

### 开操作（binary opening

* 操作：A用B腐蚀之后再用B膨胀
* 符号：空心圆

* 结果：剩下的元素都可以包裹kernel
  * 等于把kernel放进去到处滚，生成的被约束的轨迹
  * 修边，形成内边界

### 闭操作

* 操作：A用B膨胀之后再用B腐蚀

* 符号：实心圆
* 结果
  * 等于把kernel放在外面滚动，补上空缺的
  * 包括所有的像素，包括小的边幅。
  * 形成外边界

## hit or miss

* 用于匹配结构元和neigor
* 







## pattern spectrum

### parameters

* rik

### process（二值图像）

* 选择合适的se
  * 圆盘，矩形
* 开操作
* 从原始图像减去经过开操作的图像
* 得到减的图像，再进行上述的开操作（SE的size是nSE: SE逐渐膨胀），减图像
  * **recursive dilation**
  * nSE:可以得到不同尺寸的、相同形状的SE
  * **recursive erosion**
  * 作用：距离变换，分割图像（比如粘连的细胞）

### 作用

* 模式识别
* 分类
  * 根据谱的差异性，可以作为一个分类的标准





# distance transform

## intro

* 只用于二值图像
* 变换结果：灰度图像
* 实现方法：腐蚀1圈，被腐蚀的记为1.迭代，在第几次腐蚀消失的，记为n

## method

## skeletonization

## region filling



## thinning & thickening



# application

## 圆盘与长条的分割

* SE:大于长条宽度，小于圆盘的直径
* 对二值化图像进行一个开操作

## 齿轮的缺齿检测

* 开操作，提取大圆盘
* 减去原图像
* 进行label



## 胸骨肋骨分割



## 指纹图像去噪

* 先开操作去噪
* 再闭操作连接断开的

