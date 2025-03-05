<font style="color:rgb(51, 51, 51);">ERROR Verification failed: (0x1A) Security Violation Ventoy引导启动报错</font>

**<font style="color:#ff0000;">通过ventoy启动电脑时，你不会看到想要的ventoy选择系统镜像的界面，而是会看到屏幕显示如下提示：</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:#ff0000;">ERROR Verification failed: (0x1A) Security Violation</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:#ff0000;">这是因为主板开启了安全启动</font>**

**<font style="color:#000000;">我们先按ok，然后任意键进入MOK management：</font>**

**<font style="color:#000000;">1、光标选择第二项enroll key from disk</font>**

**<font style="color:#000000;">2、找到UTOYEFI这个选项回车</font>**

**<font style="color:#000000;">3、找到ENROLL_THIS_KEY_IN_MOKMANAGER.cer回车</font>**

**<font style="color:#000000;">4、选择continue回车</font>**

**<font style="color:#000000;">5、选择yes回车</font>**

**<font style="color:#000000;">6、选择reboot回车</font>**

**<font style="color:#000000;">此时我们可以重新启动电脑就能进入正常的镜像列表了。</font>**

