# texture introduction

* > texture features vary with scale

## subtopics

* texture synthesis
* texture analysis

* 

## texture spectrum

* structural texture
* stochastic texture

## application based on texture

* image segmentation
* image generation
* image replacement

## texture analysis methods

* structural
  * based on highly repeated texture
* statistical
  * based on 

# structural method

## texture elements(texels)

* texture primitives/textons

* textons+spatial relationship(lattice/grid layout)
* 



## groups

### Frieze

* repeated in one direction

### Wallpaper

* classification is based on symmetries
* details are not taken into considerations

### space 



## representing textures

### finding textons

> [!note]
>
> * 相关性
> * 统计学特征
> * 滤波器
>   * spots 
>   * oriented bars
>   * scales
> * 滤波器的设定
>   * Perona
>   * 一般六个方向就够用了
> * Gabor:
>   * 同时作用于频域和空间域
>   * 基于人类视觉系统

### multi-scale analysis(pyramid method)

* Gaussian pyramid
  * 没有方向性
  * 高度蕊？？？？？？余
* Laplacian Pyramid
  * this is a band width filter
  * oriented pyramid
    * 带有方向性





## final texture representation

### process

* filter
* square
* statistic







# texture synthesis

## methods

* image as a probability model
* pixel+matching neighborhood, then fill in
* matching process
  * pixel difference
  * count only synthesized pixels

## analysis



### co-occurrence matrix

* 在某个方向上，某个距离的某种像素对
* P（property i, property j, distance d, angle \theta)
* ![image-20240403084011167](../../../../Users/eleev/AppData/Roaming/Typora/typora-user-images/image-20240403084011167.png) 

* 可以提取的信息
  * d能够摸索纹理元素的大小
    * 对于元素比d大的，主对角线上比较多的值
  * 重复性：在对角线上的值很高





### LBP

### non-parameter sampling

* markov chain
* neighborhood
* 

### chaos mosaic

* not suitable for highly structural texture
* suitable for highly random texture



### image quilting

