---
title: 算法整理
---

## 正文

### 排序算法与查找

#### 插排              
* theta(n2)
 
#### 归并排序          
* theta(n*lgn)
  
#### 堆排             
* O(n*lgn)                    

* 常用于调整进程优先队列
 
#### 快排             
* theta(nlgn)                 

* 最常用的大数列排序

#### 计数排序          
* theta(k+n)                  

* 用于取值范围紧凑的数列排序
 
#### 基数排序           
* theta(d(n+k))               

* 对多关键字域的记录排序
 
#### 桶排序            
* theta(n)                    

* 数据分布较均匀的数据

#### 线性查找　　　　　　

* theta(n)            

#### 优化的线性查找     

* 最坏theta(n)                

* 利用子区间中位数进行分割



### 散列表

#### 链接法散列表         
* theta(1+alpha)              

* 不错的查找速度，较灵活的插入和删除

#### 开放寻址法散列表      
* theta(1/(1-alpha))          

* 优秀的查找速度，对删除操作支持不好

#### 完全散列            
* theta(1)                    

* 极好的查找速度，建表慢，一旦建好，不支持对表结构改变


### 树

#### 普通二叉树
* search, minimum, maximum, successor, predecessor, insert, delete的运行时间位O(h)，　h为树高。

* 随机构建的二叉树，树高h期望为O(lgn)


####　红黑树

* 红黑树是平衡树，树高为O(lgn)

* search, minimum, maximum, successor, predecessor操作同普通二叉树

* insert和delete教复杂，但时间度也仅为O(lgn)



