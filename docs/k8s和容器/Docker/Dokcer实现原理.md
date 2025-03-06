<font style="color:rgb(51, 51, 51);">虚拟化核心需要解决的问题：资源隔离与资源限制</font>

+ <font style="color:rgb(51, 51, 51);">虚拟机硬件虚拟化技术， 通过一个 hypervisor 层实现对资源的彻底隔离。</font>
+ <font style="color:rgb(51, 51, 51);">容器则是操作系统级别的虚拟化，利用的是内核的 Cgroup 和 Namespace 特性，此功能完全通过软件实现。</font>

###### <font style="color:rgb(119, 119, 119);">Namespace 资源隔离</font>
<font style="color:rgb(51, 51, 51);">命名空间是全局资源的一种抽象，将资源放到不同的命名空间中，各个命名空间中的资源是相互隔离的。 通俗来讲，就是docker在启动一个容器的时候，会调用Linux Kernel Namespace的接口，来创建一块虚拟空间，创建的时候，可以支持设置下面这几种（可以随意选择）,docker默认都设置。</font>

+ <font style="color:rgb(51, 51, 51);">pid：用于进程隔离（PID：进程ID）</font>
+ <font style="color:rgb(51, 51, 51);">net：管理网络接口（NET：网络）</font>
+ <font style="color:rgb(51, 51, 51);">ipc：管理对 IPC 资源的访问（IPC：进程间通信（信号量、消息队列和共享内存））</font>
+ <font style="color:rgb(51, 51, 51);">mnt：管理文件系统挂载点（MNT：挂载）</font>
+ <font style="color:rgb(51, 51, 51);">uts：隔离主机名和域名</font>
+ <font style="color:rgb(51, 51, 51);">user：隔离用户和用户组（3.8以后的内核才支持）</font>

```c
func setNamespaces(daemon *Daemon, s *specs.Spec, c *container.Container) error {
    // user
    // network
    // ipc
    // uts
    // pid
    if c.HostConfig.PidMode.IsContainer() {
        ns := specs.LinuxNamespace{Type: "pid"}
        pc, err := daemon.getPidContainer(c)
            if err != nil {
                return err
                }
        ns.Path = fmt.Sprintf("/proc/%d/ns/pid", pc.State.GetPID())
            setNamespace(s, ns)
        } else if c.HostConfig.PidMode.IsHost() {
        oci.RemoveNamespace(s, specs.LinuxNamespaceType("pid"))
        } else {
        ns := specs.LinuxNamespace{Type: "pid"}
        setNamespace(s, ns)
        }
    return nil
    }
```

###### <font style="color:rgb(119, 119, 119);">CGroup 资源限制</font>
<font style="color:rgb(51, 51, 51);">通过namespace可以保证容器之间的隔离，但是无法控制每个容器可以占用多少资源， 如果其中的某一个容器正在执行 CPU 密集型的任务，那么就会影响其他容器中任务的性能与执行效率，导致多个容器相互影响并且抢占资源。如何对多个容器的资源使用进行限制就成了解决进程虚拟资源隔离之后的主要问题。</font>![](../../images/1733055249736-5cd7eac9-4bcf-427b-829d-ba67acd3e7ae.png)

<font style="color:rgb(51, 51, 51);">Control Groups（简称 CGroups）就是能够隔离宿主机器上的物理资源，例如 CPU、内存、磁盘 I/O 和网络带宽。每一个 CGroup 都是一组被相同的标准和参数限制的进程。而我们需要做的，其实就是把容器这个进程加入到指定的Cgroup中。

###### <font style="color:rgb(119, 119, 119);">UnionFS 联合文件系统</font>
<font style="color:rgb(51, 51, 51);">Linux namespace和cgroup分别解决了容器的资源隔离与资源限制，那么容器是很轻量的，通常每台机器中可以运行几十上百个容器， 这些个容器是共用一个image，还是各自将这个image复制了一份，然后各自独立运行呢？ 如果每个容器之间都是全量的文件系统拷贝，那么会导致至少如下问题：</font>

+ <font style="color:rgb(51, 51, 51);">运行容器的速度会变慢</font>
+ <font style="color:rgb(51, 51, 51);">容器和镜像对宿主机的磁盘空间的压力</font>

<font style="color:rgb(51, 51, 51);">怎么解决这个问题------Docker的存储驱动</font>

+ <font style="color:rgb(51, 51, 51);">镜像分层存储</font>
+ <font style="color:rgb(51, 51, 51);">UnionFS</font>

<font style="color:rgb(51, 51, 51);">Docker 镜像是由一系列的层组成的，每层代表 Dockerfile 中的一条指令，比如下面的 Dockerfile 文件：</font>

```dockerfile
FROM ubuntu:15.04
COPY . /app
RUN make /app
CMD python /app/app.py
```

<font style="color:rgb(51, 51, 51);">这里的 Dockerfile 包含4条命令，其中每一行就创建了一层，下面显示了上述Dockerfile构建出来的镜像运行的容器层的结构：</font>![](../../images/1733055260482-2a2d302b-bf7e-4674-b9a7-50d9eb8f3d65.png)

<font style="color:rgb(51, 51, 51);">镜像就是由这些层一层一层堆叠起来的，镜像中的这些层都是只读的，当我们运行容器的时候，就可以在这些基础层至上添加新的可写层，也就是我们通常说的</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">容器层</font>`<font style="color:rgb(51, 51, 51);">，对于运行中的容器所做的所有更改（比如写入新文件、修改现有文件、删除文件）都将写入这个容器层。</font>

<font style="color:rgb(51, 51, 51);">对容器层的操作，主要利用了写时复制（CoW）技术。CoW就是copy-on-write，表示只在需要写时才去复制，这个是针对已有文件的修改场景。 CoW技术可以让所有的容器共享image的文件系统，所有数据都从image中读取，只有当要对文件进行写操作时，才从image里把要写的文件复制到自己的文件系统进行修改。所以无论有多少个容器共享同一个image，所做的写操作都是对从image中复制到自己的文件系统中的复本上进行，并不会修改image的源文件，且多个容器操作同一个文件，会在每个容器的文件系统里生成一个复本，每个容器修改的都是自己的复本，相互隔离，相互不影响。使用CoW可以有效的提高磁盘的利用率。 </font>![](../../images/1733055269704-1b9e42be-7cf3-4cf6-8b14-062293ea235b.png)

<font style="color:rgb(51, 51, 51);">镜像中每一层的文件都是分散在不同的目录中的，如何把这些不同目录的文件整合到一起呢？</font>

<font style="color:rgb(51, 51, 51);">UnionFS 其实是一种为 Linux 操作系统设计的用于把多个文件系统联合到同一个挂载点的文件系统服务。 它能够将不同文件夹中的层联合（Union）到了同一个文件夹中，整个联合的过程被称为联合挂载（Union Mount）。</font>![](../../images/1733055280716-04008e33-23ce-48aa-b5b6-723bf0d50cd3.png)

<font style="color:rgb(51, 51, 51);">上图是AUFS的实现，AUFS是作为Docker存储驱动的一种实现，Docker 还支持了不同的存储驱动，包括 aufs、devicemapper、overlay2、zfs 和 Btrfs 等等，在最新的 Docker 中，overlay2 取代了 aufs 成为了推荐的存储驱动，但是在没有 overlay2 驱动的机器上仍然会使用 aufs 作为 Docker 的默认驱动。 </font>

