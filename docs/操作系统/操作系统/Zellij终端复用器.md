```bash
curl -LO https://github.com/zellij-org/zellij/releases/latest/download/zellij-x86_64-unknown-linux-musl.tar.gz
tar -xzf zellij-x86_64-unknown-linux-musl.tar.gz
mv zellij /usr/local/bin/
chmod +x /usr/local/bin/zellij
zellij

```

## 快捷键（记住这几个就能用了）
`Alt + n``ctrl+p+n`新建pane 窗格

`ctrl+t+n`新建tab标签

`ctrl+o+d`退出并且保活

```bash
zellij ls 
zellij -s test
zellij attach test   #或者zellij a test

```

+ <font style="color:rgba(0, 0, 0, 0.75);">新建窗格</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Alt + n</font>`
+ <font style="color:rgba(0, 0, 0, 0.75);">窗格导航</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Alt + <←↓↑→></font>`<font style="color:rgba(0, 0, 0, 0.75);"> </font><font style="color:rgba(0, 0, 0, 0.75);">或</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Alt + <hjkl></font>`
+ <font style="color:rgba(0, 0, 0, 0.75);">调整窗格(面板)大小</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Alt + <+-></font>`
+ <font style="color:rgba(0, 0, 0, 0.75);">锁定或解锁:</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Ctrl + g</font>`<font style="color:rgba(0, 0, 0, 0.75);">, 使用后会自动屏蔽zellij的其他快捷键, 如ctrl + q退出等</font>
+ <font style="color:rgba(0, 0, 0, 0.75);">窗格快捷键:</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Ctrl + p</font>`<font style="color:rgba(0, 0, 0, 0.75);">, 按下后, 可以直接 ←↓↑→ 移动(也可以直接鼠标点), n 新建窗格, x关闭窗格, c 重命名窗格, d 下方新建窗格, r 右边新建窗格, f 全屏, z 显示或隐藏边框, w 悬浮(居中?), e 嵌入, p 选中下一个窗格, ENTER 进入选中窗格</font>
+ <font style="color:rgba(0, 0, 0, 0.75);">标签页快捷键:</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Ctrl + Tab</font>`<font style="color:rgba(0, 0, 0, 0.75);">, 按下后, n 新建类似浏览器的标签页, ←→或Tab切换标签页(当然也可以直接鼠标点), x 关闭标签页, r 重命名标签页, s 同步模式(多个窗格可以同时输入), ENTER 进入窗格</font>
+ <font style="color:rgba(0, 0, 0, 0.75);">调整大小的快捷键:</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Ctrl + n</font>`<font style="color:rgba(0, 0, 0, 0.75);">, 按下后, 使用</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);"><←↓↑→> 或 <hjkl> 或 <+-></font>`<font style="color:rgba(0, 0, 0, 0.75);"> </font><font style="color:rgba(0, 0, 0, 0.75);">调整窗格大小</font>
+ <font style="color:rgba(0, 0, 0, 0.75);">移动窗格的快捷键:</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Ctrl + h</font>`<font style="color:rgba(0, 0, 0, 0.75);">, 按下后, 使用</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);"><←↓↑→> 或 n(下一个)</font><font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);"> </font>`<font style="color:rgba(0, 0, 0, 0.75);">来移动窗格位置</font>
+ <font style="color:rgba(0, 0, 0, 0.75);">搜索:</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Ctrl + s</font>`
+ <font style="color:rgba(0, 0, 0, 0.75);">会话(session):</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Ctrl + o</font>`<font style="color:rgba(0, 0, 0, 0.75);">, 按下后, d Detach离开zellij (后台运行, 可以zellij a session_name重新进入会话, session_name可以只输入前面几个字母), 打印</font><font style="color:rgba(0, 0, 0, 0.75);"> </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Session detached</font>`
+ <font style="color:rgba(0, 0, 0, 0.75);">退出: </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Ctrl + q</font>`<font style="color:rgba(0, 0, 0, 0.75);">, 退出会话后, 不会后台运行, 打印 </font>`<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Bye from Zellij!</font>`

