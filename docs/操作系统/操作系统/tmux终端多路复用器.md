`tmux` 是一个终端多路复用器，它可以让你在一个终端窗口中同时使用多个会话。它非常适合需要在一个 SSH 会话中同时操作多个终端，或者在远程工作时进行高效的会话管理。以下是一些常用的 `tmux` 操作和基本概念：

### 基本概念
+ **会话 (Session)**: `tmux` 的最顶层结构，你可以在一个会话中运行多个窗口和面板。
+ **窗口 (Window)**: 一个窗口就像是一个虚拟终端，你可以在里面运行一个程序或者命令。
+ **面板 (Pane)**: 每个窗口可以被拆分成多个面板，这样你可以在一个窗口中同时查看和操作多个终端。

### 常用命令
#### 启动和管理会话
+ **启动新的 **`**tmux**`** 会话**:

```bash
tmux
```

+ **启动带名字的会话**:

```bash
tmux new -s session_name
```

+ **列出所有会话**:

```bash
tmux ls
```

+ **切换到一个已存在的会话**:

```bash
tmux attach-session -t session_name
```

+ **分离当前会话** (即退出 tmux 会话但不终止它): 按下 `Ctrl + b` 后松开，然后按下 `d`。
+ **杀死一个会话**:

```bash
tmux kill-session -t session_name
```

#### 窗口和面板操作
+ **创建新窗口**: 按下 `Ctrl + b` 后松开，然后按下 `c`。
+ **切换窗口**:
    - `Ctrl + b` 后松开，然后按下窗口号（如 `0`, `1`, `2` 等）。
    - `Ctrl + b` 后松开，然后按下 `n` (下一个窗口) 或 `p` (上一个窗口)。
+ **拆分窗口成面板**:
    - 垂直拆分: 按下 `Ctrl + b` 后松开，然后按下 `%`。
    - 水平拆分: 按下 `Ctrl + b` 后松开，然后按下 `"`。
+ **在面板之间切换**:
    - 使用 `Ctrl + b` 后松开，然后按下方向键（`←`, `→`, `↑`, `↓`）。
+ **调整面板大小**:
    - 按下 `Ctrl + b` 后松开，然后按住 `Ctrl` 和方向键来调整面板的大小。
+ **关闭当前面板**: 按下 `Ctrl + b` 后松开，然后按下 `x`，确认关闭面板。

#### 复制和粘贴
+ **进入复制模式**: 按下 `Ctrl + b` 后松开，然后按下 `[` 进入复制模式。
+ **移动光标并选择文本**: 在复制模式下，使用箭头键移动光标，按下空格键开始选择，按下回车键复制选中的文本。
+ **粘贴**: 按下 `Ctrl + b` 后松开，然后按下 `]` 粘贴之前复制的文本。

#### 设置和自定义
+ **配置文件**: `tmux` 的配置文件是 `~/.tmux.conf`。你可以在这个文件中添加自定义的快捷键、外观设置等。
+ **设置颜色**: 你可以在 `.tmux.conf` 文件中设置终端的配色方案。
+ **常见配置示例**:

```bash
# 更改前缀键为 Ctrl + a
set -g prefix C-a
unbind C-b
bind C-a send-prefix

# 启用鼠标支持
set -g mouse on
```

`tmux` 提供了强大的会话管理功能，非常适合用于长时间运行的远程任务，或者需要在多个会话中进行复杂操作的场景。





```bash
# tmux窗口中 Ctrl+b,? 查看帮助
C-b C-b     Send the prefix key	发送前缀键
C-b C-o     Rotate through the panes 旋转窗格
C-b C-z     Suspend the current client 挂起当前客户端
C-b Space   Select next layout 选择下一个布局
C-b !       Break pane to a new window 打破窗格到一个新窗口
C-b "       Split window vertically 垂直分割窗口
C-b #       List all paste buffers 列出所有粘贴缓冲区
C-b $       Rename current session 重命名当前会话
C-b %       Split window horizontally 水平分割窗口
C-b &       Kill current window 关闭当前窗口
C-b '       Prompt for window index to select 提示要选择的窗口索引
C-b (       Switch to previous client 切换到上一个客户端
C-b )       Switch to next client 切换到下一个客户端
C-b ,       Rename current window 重命名当前窗口
C-b -       Delete the most recent paste buffer 删除最近的粘贴缓冲区
C-b .       Move the current window 移动当前窗口
C-b /       Describe key binding 描述键绑定
C-b 0       Select window 0 选择窗口0
C-b 1       Select window 1
C-b 2       Select window 2
C-b 3       Select window 3
C-b 4       Select window 4
C-b 5       Select window 5
C-b 6       Select window 6
C-b 7       Select window 7
C-b 8       Select window 8
C-b 9       Select window 9
C-b :       Prompt for a command 命令提示符
C-b ;       Move to the previously active pane 移动到先前活动的窗格
C-b =       Choose a paste buffer from a list 从列表中选择粘贴缓冲
C-b ?       List key bindings 列出键绑定
C-b C       Customize options 自定义选项
C-b D       Choose a client from a list 从列表中选择一个客户端
C-b E       Spread panes out evenly 将窗格均匀摊开
C-b L       Switch to the last client 切换到最后一个客户端
C-b M       Clear the marked pane 清除已标记的窗格
C-b [       Enter copy mode 进入拷贝模式
C-b ]       Paste the most recent paste buffer 粘贴缓冲区中最近的待粘贴项
C-b c       Create a new window 创建一个新窗口
C-b d       Detach the current client 分离当前客户端
C-b f       Search for a pane 搜索一个窗格
C-b i       Display window information 显示窗口信息
C-b l       Select the previously current window 选择先前的当前窗口
C-b m       Toggle the marked pane 切换标记的窗格
C-b n       Select the next window 选择下一个窗口
C-b o       Select the next pane 选择下一个窗格
C-b p       Select the previous window 选择上一个窗口
C-b q       Display pane numbers 显示窗格编号
C-b r       Redraw the current client 重绘当前客户端
C-b s       Choose a session from a list 从列表中选择会话
C-b t       Show a clock 显示时钟
C-b w       Choose a window from a list 从列表中选择一个窗口
C-b x       Kill the active pane 关闭活动窗格
C-b z       Zoom the active pane 缩放活动窗格
C-b {       Swap the active pane with the pane above 将活动窗格与上面的窗格交换
C-b }       Swap the active pane with the pane below 将活动窗格与下面的窗格交换
C-b ~       Show messages 显示消息
C-b DC      Reset so the visible part of the window follows the cursor 重置，使窗口的可见部分跟随游标
C-b PPage   Enter copy mode and scroll up 进入复制模式并向上滚动
C-b Up      Select the pane above the active pane 选择活动窗格上方的窗格
C-b Down    Select the pane below the active pane 选择活动窗格下面的窗格
C-b Left    Select the pane to the left of the active pane 选择活动窗格左侧的窗格
C-b Right   Select the pane to the right of the active pane 选择活动窗格右侧的窗格
C-b M-1     Set the even-horizontal layout 设置均匀水平布局
C-b M-2     Set the even-vertical layout 设置均匀垂直布局
C-b M-3     Set the main-horizontal layout 设置主水平布局
C-b M-4     Set the main-vertical layout 设置主垂直布局
C-b M-5     Select the tiled layout 选择平铺布局
C-b M-n     Select the next window with an alert 选择带有警报的下一个窗口
C-b M-o     Rotate through the panes in reverse 反向旋转窗格
C-b M-p     Select the previous window with an alert 选择带有警报的前一个窗口
C-b M-Up    Resize the pane up by 5 将窗格的大小向上调整5
C-b M-Down  Resize the pane down by 5 将窗格的大小向下调整5
C-b M-Left  Resize the pane left by 5 将窗格的大小向左调整5
C-b M-Right Resize the pane right by 5 将窗格的大小向右调整5
C-b C-Up    Resize the pane up 向上调整窗格的大小
C-b C-Down  Resize the pane down 向下调整窗格的大小
C-b C-Left  Resize the pane left 向左调整窗格的大小
C-b C-Right Resize the pane right 向右调整窗格的大小
C-b S-Up    Move the visible part of the window up 向上移动窗口的可见部分
C-b S-Down  Move the visible part of the window down 向下移动窗口的可见部分
C-b S-Left  Move the visible part of the window left 向左移动窗口的可见部分
C-b S-Right Move the visible part of the window right 向右移动窗口的可见部分

```

