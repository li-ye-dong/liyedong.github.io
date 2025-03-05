例如：

+ <font style="color:rgb(13, 13, 13);">型号	Intel(R) Xeon(R) Gold 6346 CPU @ 3.10GHz </font>
+ <font style="color:rgb(13, 13, 13);">处理器速度	3.09 GHz </font>
+ <font style="color:rgb(13, 13, 13);">处理器插槽	2 </font>
+ <font style="color:rgb(13, 13, 13);">每个插槽的处理器内核数	16 </font>
+ <font style="color:rgb(13, 13, 13);">逻辑处理器	64 </font>
+ <font style="color:rgb(13, 13, 13);">超线程	活动</font>

:::info
<font style="color:rgb(13, 13, 13);">表明你的计算机上有两个插槽，每个插槽都安装了一个 Intel Xeon Gold 6346 处理器。每个处理器有 16 个内核，总共有 32 个内核。由于超线程处于活动状态，每个内核可以处理两个线程，因此总共有 64 个逻辑处理器。</font>

:::

<font style="color:rgb(51, 51, 51);">在物理主机上，每个物理CPU均对应若干内存，CPU可读写所有内存的数据，但对本身对应的内存做读写操作时性能最佳。</font>

<font style="color:rgb(51, 51, 51);">基于此，虚拟机在使用多个CPU时，可通过设置虚拟机CPU插槽，使虚拟机的CPU平均地由多个物理CPU提供，此时对单个物理CPU的压力较小，同时也能达到更佳的内存读写性能。</font>

<font style="color:rgb(51, 51, 51);">虚拟机CPU插槽数量即指定了虚拟机的多个CPU可平均分布到多少个物理CPU上。因此，虚拟机CPU插槽的数量必须能整除虚拟机的CPU个数。 </font>

<font style="color:rgb(51, 51, 51);">对于一台虚拟机来说，一般推荐CPU插槽数：每插槽的内核数=1:2，高计算力的虚拟机可能达到1:4甚至更高。</font>

<font style="color:rgb(51, 51, 51);">假设一个简单的场景：</font>

<font style="color:rgb(51, 51, 51);">环境中每台主机拥有4颗8核的物理CPU，总物理核数为32个。</font>

<font style="color:rgb(51, 51, 51);">一个未设置CPU插槽的虚拟机，CPU数量为8个，则可能由主机上一个物理CPU的8个内核组成虚拟机的8个虚拟CPU;或可能由一个物理CPU提供5个内核，另一个物理CPU提供3个内核，一同组成虚拟机的8个虚拟机CPU，等等。</font>

<font style="color:rgb(51, 51, 51);">另一个虚拟机设置了CPU插槽数量为4，此时虚拟机的8个CPU平均地由主机上的4颗物理CPU提供，每个物理CPU提供2个内核，达到了最佳的计算性能。</font>

