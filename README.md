---
title: clrs算法整理
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
* search, minimum, maximum, successor, predecessor, insert, delete的运行时间位O(h)，h为树高。
* 随机构建的二叉树，树高h期望为O(lgn)

#### 红黑树
* 红黑树是平衡树，树高为O(lgn)
* search, minimum, maximum, successor, predecessor操作同普通二叉树
* insert和delete较复杂，但时间度也仅为O(lgn)



###  数据结构的扩张
#### 例子：　order-statistic red and black tree
#### 例子：　interval red and black tree
#### 扩张数据结构的一般步骤:
 * 选择一种基础数据结构
 * 确定基础数据结构中要维护的附加信息
 * 检验基础数据结构上的基本修改操作能否维护附加信息
 * 设计一些新的操作


###  高级设计与分析
#### 动态规划的一般步骤
* 刻画一个最优解的结构特征
* 递归地定义最优解的值
* 计算最优解的值，通常采用自底向上的方法
* 利用计算出的信息构造一个最优解
#### 发掘最优子结构
* 证明问题最优解的第一个做出一个选择。做出这次选择会产生一个或多个待解的子问题
* 对于一个给定问题，在其可能的第一步选择中，你假定已经知道哪种选择会得到最优解。
* 给定可选择最优解的选择后，你确定这次选择会产生哪些子问题，遗迹如何更好地刻画子问题空间。
* 利用“cut-and-paste”技术证明:作为构成原问题最优解的组成部分，每个子问题的解就是它本身的最优解。
#### 重叠子问题
* 这是适合动态规划方法求解的最优化问题的第二个性质。
* 子问题空间必须足够"小"，即问题的递归算法会反复地求解相同的自问题，而不是一直生成新的子问题。
#### 例子
* 钢条切割　r[n] = p[i] + r[n-i]
* 矩阵链乘法 m[i, j] = m[i, k] + m[k + 1, j] + p[i-1] * p[k] * p[j])
* 最长公共子序列 c[i,j]={c[i-1, j-1] + 1 if: i,j>0 and x[i]==y[j]} 
or {max(c[i,j-1], c[i-1,j]) if: i,j>0 and x[i] != y[i]}
* 最长二叉搜索树 e[i, j] = e[i, r-1] + e[r + 1, j] + w(i, j)

#### 贪心算法的一般步骤
* 确定问题的最优子结构
* 设计一个递归算法
* 证明如果我们做出一个贪心选择，则只剩下一个子问题
* 证明贪心选择总是安全的
* 设计一个递归算法实现贪心策略
* 将递归算法转换为迭代算法

#### 例子
* 活动选择问题 c[i, j] = max{c[i, k] + c[k, j] + 1}
* hoffman编码:　每步策略:将频率最低的两个字符合成为一个字符求解新的hoffman树

#### 怎样分辨一个问题适用贪心算法还是动态规划算法
* 这个问题是否可以在不进行后续决策的情况下判断出当前的最优决策?

#### 拟阵的三条性质(拟阵M=(S, I)的判定)
* S是一个有限集
* I是S子集的非空族，这些子集称为S的独立子集，使得如果B∈I且A⊆B，则A∈I。称I为遗传的。
* 若A∈I, B∈I且|A|<|B|,那么存在某个元素x∈B-A，使得A∪{x}∈I，称M满足交换性质。

#### 拟阵的两个例子
* 图拟阵
* 矩阵拟阵

#### 具体应用例子
* 最小生成树问题转化为加权拟阵最大权重独立子集问题，用贪心算法求解。
* 单位时间任务调度问题(最小化延迟任务惩罚=最大化提前任务惩罚值和)


#### 摊还分析
##### amortized analysis
* 循环部分的复杂度并非每步复杂度的简单加和，聚合分析可以给出更紧密的上界。
##### accounting method
* 赋予某些操作(栈操作中的push, 二进制计数器中的置位操作)多于其实际代价的费用，以支付后续操作的费用。
* 初始积累费用可能不为零(栈中初始有元素/计数器初始不为0)，　这些仅仅是常数项，不影响复杂度分析。
* 总的摊还代价(加上初始的费用积累(这是常数项，可略去))是总的实际代价的一个上界。
##### potential method
* 引入势能的概念，每个操作的摊还代价=实际代价+势能变化
* 只要保证整个过程势能变化为正值，总的摊还代价是总的实际代价的一个上界
* 势能的例子:(栈操作中的元素数量，计数器中1的数量)
* 势能法可以用于计算初始状态势能不为0的情况。在这种情况下，我们不能保证“整个过程势能变化为正值”，但是，由于我们已经建立起总的实际代价、总的势能变化和总的摊还代价(引入势能变化，可以将每步摊还代价设为常数值)的关系，我们可以通过作为已知量总的势能变化和总的摊还代价来求出总的实际代价。
##### 例子:动态表
* 注意书中的分析过程，是以基本insert操作为1代价的(意味着allocate, free作为低阶复杂度的操作，其代价被忽略了)
* 可以再仔细看看动态表的势能模型，和insert, delete操作的摊还分析的计算过程。



### 高级数据结构
#### B树
* 用于管理磁盘内容。
#### 斐波那契堆
* 良好的摊还时间复杂度
* extract_min 和 delete: O(lgn)
* make_heap, insert, minimum, extract_min, union, decrease_key, delete: O(1)复杂度
* 一些图问题算法可能频繁调用decrease_key。一些问题(如最小生成树和寻找单源最短路径)的快速算法必不可少地要用到斐波那契堆。
* 实际上，斐波那契堆的常数因子和编程复杂性使得它较普通二项堆不太适用。
* 二项堆和斐波那契堆对search支持不好。
#### van Emde Boas树
* 限制关键字为0 ~ u-1的整数，且无重复
* search, insert, delete, minimum, maximum, successor, predecessor运行时间位O(lglgu)
#### 用于不相交集合的数据结构
*　两种启发式策略(union by rank) 和　(path compression)的一并使用，极大地改善了disjoint_set forest上各操作的时间复杂度
* 对于n个元素的个不相交集合操作，改进后的运行时间是O(m * alpha(n))
#### 其他高级数据结构
* 动态树
* 伸展树
* 持久数据结构
* 聚合树
* 动态图数据结构


### 图算法
#### 基本图算法
* bfs, dfs的时间复杂度皆为O(V + E)
* bfs用于寻找最短路径
* dfs用于拓扑排序、寻找强连通分量
#### 最小生成树
* Kruskal算法和Prim算法，如果使用普通二叉堆，这两个算法的时间复杂度皆为O(ElogV)
* 使用斐波那契堆，可以将Prim算法的运行时间改善为O(E + lgV)
* Kruskal 的思路是循环查找最小安全边，将其加入生成树子集；相当于每步消化掉一个set。
* Prim　的思路是循环查找轻量级邻接边，并更新邻接边连接的新结点的parent和key值；相当于每步消化一个邻接的结点。
#### 单源最短路径
* Bellman_Ford运行时间为O(VE), 主要过程就是进行了|V| - 1轮的松弛操作, 可以检出负值环路的存在。
* 计算有向无环图的最短路径算法，运行时间为O(V + E)，主要过程为以拓扑顺序对每个点进行邻接边松弛，可以应用于PERT图分析。
* Dijkstra要求所有边的权重非负运行时间，O(V^2 + E), 如果用二叉堆或斐波那契堆实现最小队列，可以获得更优时间复杂度， O((V + E) * lgV), O(V * lgV + E)。
* Dijkstra算法和用于有向无环图的最短路径算法对每条边仅松弛一次，Bellman_Ford算法则对每条边松弛|V| - 1次。
#### 线性规划问题的一个特例:差分约束问题可转化为单源最短路径问题
#### 所有结点对的最短路径
##### 最短路径和矩阵乘法
* 再体会体会两种计算方式的相同点
* 用反复平方法改进后的算法运行时间为theta(n^3 * lgn)
* 要求不包含负值环路
##### Floyd_Warshall算法
* 要求不包含负值环路
* 运行时间theta(n^3)
* Floyd_Warshall算法的变体可以用于计算有向图的传递闭包。
##### Johnson算法
* 用于稀疏图， 可以处理负值环路
* 运行时间为O(V^2 * lgV + V * E)
#### 最大流
##### Edmonds_Karp算法
* Ford_Fulkerson算法的一种具体实现。
* 使用bfs来搜索增广路径。
* 运行时间为O(V * E^2)。
* Ford_Fulkerson算法可以用于寻找最大二分匹配。
##### 推送-重贴标签算法
* 基本操作的总次数是O(V^2 * E)
##### 前置重贴标签算法
* 运行时间为O(V^3)


### 算法问题选编
#### 多线程算法
* 最基本技巧就是**嵌套并行**和**并行循环**，这个单机上用简单的多线程和多进程就可以实现。
* 并行循环是增大并行度。
* 并行循环可以通过嵌套并行结合二分和归并的思路实现。
* 多线程性能的衡量最基本标准的是**工作量T1**和**持续时间T(inf)**， T1/T(inf)给出多线程计算的并行度。
#### 矩阵运算
* 计算lup分解用时theta(n^3), 用lup求解用时theta(n^2)
* 对A*x = b来说， 其lup分解近取决于A。因此求解矩阵的逆, A * X = In 不过是n次迭代求解A * Xi = ei, 用时theta(n ^ 3)
* 对称正定矩阵与最小二乘逼近。一个应用是对给定数据点进行曲线拟合。


#### 线性规划
* 单纯型算法，常用，但对于某些刻意设计的输入，可能会需要指数型时间(本章几乎全部讨论都是关于单纯型算法)。
* 椭球算法，多项式时间，但在实际中运行缓慢
* 内点法， 对于大规模输入，有可能快于单纯型算法。
##### 一般步骤
* 转化为标准型
* 转化为松弛型(N, B, A, b, c, v)
##### 转换线性规划位标准型
* 目标函数可能是最小化，而不是最大化。（将目标函数取负）
* 可能有变量不具有非负约束。(将不具有非负约束的变量xj替换为两个满足非负约束的变量的表达式xj1 - xj2)
* 可能有等式约束，即有一个等号而不是一个小于等于号。（x=y等价于x>=y且x<=y）
* 可能有不等式约束，但不是小于等于号，而是一个大于等于号。（等式两边乘-1）
##### 单源最短路径问题
* 最大化dt, 满足约束dv <= du + w(u, v), (u, v) ∈ E; ds = 0
* 有|V|个变量dv, |E| + 1个约束
##### 最大流问题
* 最大化sigma(v ∈ V)fsv - sigma(v ∈ v)fvs， 满足如下约束:
* fuv <= c(u, v), (u,v ∈ V)
* sigma(v ∈ V)fvu = sigma(v ∈ V)fuv, (u ∈ V - {s, t})
* fuv >= 0, (u,v ∈ V)
* 共 |V|^2个变量，2 * |V|^2 + |V| - 2 个约束
* 对上述3类约束条件，u,v范围加上u,v 属于 g.E的限制，可将约束数量减少至O(V + E)
##### 最小费用问题
##### 多商品流问题
##### 单纯型算法


#### 多项式与快速傅里叶变换
##### 多项式表示
* 系数表示&点阵表示
* 系数-->点阵， O(n * lgn)
* 点阵-->系数, 拉格朗日公式, O(n ^ 2)
* 多项式乘法。普通乘法:O(n ^ 2)。 高效乘法：求点值(O(n * lgn)) + 点值乘法(O(n)) + 差值(O(n * lgn)) = O(n * lgn)
##### DFT与FFT
* O(n * lgn), 分别实现点阵和系数的互相转换。
##### FFT性能优化
* 递归-->迭代
* 提高并行度


#### 数论算法
##### 常见问题及解决
* 最大公约数。Euclid。
* 求解模线性方程。
* 中国余数定理。a = (a[1]c[1] + a[2]c[2] + ... + a[k]c[k])(mod n); c[i] = m[i] * (m[i] ^ -1 mod n[i]); m[i] = n[1]n[2]...n[i - 1]n[i + 1]n[k]
* RSA密钥对生成
* 大素数生成
* 整数的因子分解。POLLARD_RHO。主要的用途是在theta(p ^ 0.5)时间内，找出n的一个小因子p。



#### 字符串匹配
##### 概览
* 朴素算法， 预处理时间0， 匹配时间O((n - m + 1)m)
* Rabin_Karp, 预处理时间theta(m), 最坏匹配时间O((n - m + 1)m)，期望时间O(n)（在q >= m时， q为用来进行模运算的素数）。
* 有限自动机算法，预处理时间O(m|sigma|), 匹配时间theta(n)
* Knuth_Morris_Pratt, 预处理时间theta(m), 匹配时间theta(n)
##### 朴素算法
##### Rabin_Karp
* 用模运算可以帮助处理难以直接操作的大数字运算。
##### 有限自动机算法
* M = (Q, q0, A, sigma, delta)
* 计算转移函数delta用时O(m ^ 3 * |sigma|)， 可改进为O(m * |sigma|)


#### 计算几何学
##### 线段的性质
* 利用叉积判断连续线段左右转
##### 确定任意一对线段是否相交
* 利用扫除确定线段集中任意两条线段是否相交。
* O(n * lgn)。
* 简化的实现假设没有三条输入线段相交于同一点。
* 扫除算法维护两组数据: sweep-line status, event-point schedule
* 扫除线状态是一个完全前序关系(可传递的完全关系)， 需要支持INSERT, DELETE, ABOVE, BELOW操作，红黑树有效满足要求。
##### 寻找凸包
* 介绍的两种主要方法都是运用"旋转扫除"技术。
* Graham 扫描法O(n * lgn)。
* Jarvis步进法(n * lgh)(h为凸包定点数)。
* 增量法O(n * lgn), 分治法(O(n * lgn)), 剪枝--搜索方法(n * lgh)
#### 寻找最近点对
* O(n * lgn)
* 书中算法用到了一种将已排序数组在O(n)时间内分成两个有序子数组的方法。



#### NP完全性
##### 常见的几个NP完全问题
* 最长简单路径问题
* 汉密尔顿圈问题
* 3-CNF可满足问题
##### NP完全问题的证明思路
* 将最优化问题转化为较简单的判定问题。
* 归约。
##### NP, co-NP, P三者的关系至今没有定论。
##### NPC问题的原始判定
* 1. L ∈ NP
* 2. 对每一个L1 ∈ NP, 有L1 <= (poly)L  (仅满足该性质，称L为NP-hard)
##### NPC问题的证明
* 布尔公式可满足性问题
* 3-CNF可满足性问题
##### 列举NP完全问题
* 团问题
* 定点覆盖问题
* 汉密尔顿回路
* 旅行商问题
* 子集和问题

#### 近似算法
##### 顶点覆盖问题
* 近似比2。
* 极大匹配作为最优解的下界，绕过了对最优顶点覆盖实际规模的计算。
##### 旅行商问题
* 如果代价函数c满足三角不等式，近似比2.
* 一般旅行商问题。证明某一问题没有近似算法的思路。
##### 集合覆盖问题
* 近似比ln|X| + 1
##### 随机化和线性规划
* 随机化。 例子:max-3-CNF可满足性问题。
* 线性规划。 例子:带权重的定点覆盖问题。
##### 子集和问题



## 下一步计划
1. 算法导论习题。。。
2. 整理算法进阶的下一步计划(小规模问题的解决《编程之美》， 低阶算法实现熟练度leetcode/lintcode, 边界在哪里？/边界之外是什么？)

