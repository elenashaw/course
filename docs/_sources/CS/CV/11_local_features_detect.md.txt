## review

* 角点的检测
  * 
* 描述子：descriptor
* 检测的特点
  * 不变性：仿射变换后依然能检测
  * SIFT:scale invariant feature tranform
    * 尺度不变性

* 找兴趣点->找描述子
  * 描述子：特征点周围像素的信息

## harris 角点检测

### 基本处理

* 窗口检测
  * flat 
  * edge（两条线的交点）
  * corner
* 高斯平滑去除噪点
* 非极大值抑制
* 阈值选择
* 

### 算法特性

* 不变性：平移，旋转不变性（特征值不变）
* 尺度会影响角点的检测



## MOPS



## SIFT

* local features
* 特点
  * 对遮挡具有鲁棒性

### 步骤

- **Scale-space peak selection:** Potential location for finding features.
  尺度空间峰值选择：寻找特征的潜在位置。
- **Keypoint Localization:** Accurately locating the feature keypoints.
  关键点定位：准确定位特征关键点。
- **Orientation Assignment:** Assigning orientation to keypoints.
  方向分配：为关键点分配方向。
- **Keypoint descriptor:** Describing the keypoints as a high dimensional vector.
  关键点描述符：将关键点描述为高维向量。
- **Keypoint Matching 关键点匹配**

### 细节

* LoG: 稳定性
* 高斯金字塔：
  * 降采样的多个金子塔
  * 每一层有不同的方差高斯模糊图片
  * DOG：进行差分
  * ![img](https://miro.medium.com/v2/resize:fit:607/0*DlULvyAuyXb1mSWb.jpg)



### 缺陷：

* 光滑边缘难以提取特征点
* 实时性差





## SURF

* speeded up robust features
* 