# From relu to gelu
## 激活函数的特性 

[从ReLU到GELU，一文概览神经网络的激活函数](https://zhuanlan.zhihu.com/p/98863801) 



| 激活函数名 | sigmoid                 | relu                 | elu                 | leaky relu            | selu                                    | gelu                 |
|------------|-------------------------|----------------------|---------------------|-----------------------|-----------------------------------------|----------------------|
| 函数公式   | ![](sigmoid-text.jpg)   | ![](relu-text.jpg)   | ![](elu-text.jpg)   | ![](lrelu-text.jpg)   | ![](selu-text1.jpg) ![](selu-text2.jpg) | ![](gelu-text.png)   |
| 函数图像   | ![](sigmoid-pic.jpg)    | ![](relu-pic.jpg)    | ![](elu-pic.jpg)    | ![](lrelu-pic.jpg)    | ![](selu-pic.jpg)                       | ![](gelu-pic.jpg)    |
| 函数导数   | ![](sigmoid-d-text.jpg) | ![](relu-d-text.jpg) | ![](elu-d-text.jpg) | ![](lrelu-d-text.jpg) | ![](selu-d-text.jpg)                    | ![](gelu-d-text.png) |
| 导数图像   | ![](sigmoid-d-pic.jpg)  | ![](relu-d-pic.jpg)  | ![](elu-d-pic.jpg)  | ![](lrelu-d-pic.jpg)  | ![](selu-d-pic.jpg)                     | ![](gelu-d-pic.jpg)  |
| 优点       |-                         |1.相比于sigmoid，由于稀疏性，时间和空间复杂度更低；<br>2.不涉及成本更高的指数运算；能避免梯度消失问题。                      |1.能避免死亡ReLU问题；<br>2.能得到负值输出，这能帮助网络向正确的方向推动权重和偏置变化；<br>3.在计算梯度时能得到激活，而不是让它们等于0。                     |1.类似ELU，Leaky ReLU 也能避免死亡ReLU问题，因为其在计算导数时允许较小的梯度；<br>2.由于不包含指数运算，所以计算速度比 ELU 快。                       |1.内部归一化的速度比外部归一化快，这意味着网络能更快收敛；<br>2.不可能出现梯度消失或爆炸问题，见SELU论文附录的定理2和3。                                         |1.似乎是NLP领域的当前最佳；<br>2.尤其在Transformer模型中表现最好；<br>3.能避免梯度消失问题。                      |
| 缺点       |-                         |1.引入了死亡ReLU问题，即网络的大部分分量都永远不会更新。但这有时候也是一个优势；<br>2.ReLU 不能避免梯度爆炸问题。                      |1.由于包含指数运算，所以计算时间更长；<br>2.无法避免梯度爆炸问题；<br>3.神经网络不学习 α 值。                     |1.无法避免梯度爆炸问题；<br>2.神经网络不学习α值；<br>3.在微分时，两部分都是线性的；<br>4.而ELU的一部分是线性的，一部分是非线性的。                       |1.这个激活函数相对较新——需要更多论文比较性地探索其在CNN和RNN等架构中应用。<br>2.这里有一篇使用SELU的CNN论文：[https://arxiv.org/pdf/1905.01338.pdf]()                                        |1.尽管是2016年提出的，但在实际应用中还是一个相当新颖的激活函数。                      |


