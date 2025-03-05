<font style="color:rgb(51, 51, 51);">SQLite以其卓越的零配置特性而闻名，这意味着不需要复杂的设置或管理。本章将带您完成在Windows、Linux和macosx上设置SQLite的过程。</font>

## <font style="color:rgb(51, 51, 51);">在Windows上安装SQLite</font>
+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Step 1</font>**`<font style="color:rgb(51, 51, 51);">− 转到</font>[<font style="color:rgb(51, 51, 51);">SQLite下载页面</font>](https://www.sqlite.org/download.html)<font style="color:rgb(51, 51, 51);">，然后从Windows部分下载预编译的二进制文件。</font>
+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Step 2</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 下载sqlite-shell-win32-*.zip和sqlite-dll-win32-*.zip压缩文件。</font>
+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Step 3</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 创建一个文件夹 C:\>sqlite ，并在该文件夹中的两个压缩文件上方解压缩，这将为您提供sqlite3.def，sqlite3.dll和sqlite3.exe文件。</font>
+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Step 4</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 在PATH环境变量中添加C:\>sqlite，最后转到命令提示符并发出sqlite3命令，该命令将显示以下结果。</font>

```powershell
C:\>sqlite3
SQLite version 3.7.15.2 2013-01-09 11:53:05
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```

## <font style="color:rgb(51, 51, 51);">在Linux上安装SQLite</font>
<font style="color:rgb(51, 51, 51);">今天，几乎所有版本的Linux OS都随SQLite一起提供。因此，您只需发出以下命令来检查计算机上是否已经安装了SQLite。</font>

```powershell
$sqlite3
SQLite version 3.7.15.2 2013-01-09 11:53:05
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```

<font style="color:rgb(51, 51, 51);">如果看不到以上结果，则表明您的Linux机器上未安装SQLite。以下是安装SQLite的以下步骤-</font>

+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Step 1</font>**`<font style="color:rgb(51, 51, 51);">−转到</font>[<font style="color:rgb(51, 51, 51);">SQLite下载页面，</font>](https://www.sqlite.org/download.html)<font style="color:rgb(51, 51, 51);">然后从源代码部分下载sqlite-autoconf-*.tar.gz。</font>
+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Step 2</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">−运行以下命令−</font>

```powershell
$tar xvfz sqlite-autoconf-3071502.tar.gz
$cd sqlite-autoconf-3071502
$./configure --prefix=/usr/local$make
$make install
```

<font style="color:rgb(51, 51, 51);">以上命令将在Linux机器上安装SQLite结束。您可以按照上面的说明进行验证。</font>

## <font style="color:rgb(51, 51, 51);">在Mac OS X上安装SQLite</font>
<font style="color:rgb(51, 51, 51);">虽然最新版本的Mac OS X预先安装了SQLite，但是如果您没有可用的安装，请按照以下步骤操作-</font>

+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Step 1</font>**`<font style="color:rgb(51, 51, 51);">−转到</font>[<font style="color:rgb(51, 51, 51);">SQLite下载页面</font>](https://www.sqlite.org/download.html)<font style="color:rgb(51, 51, 51);">，然后从源代码部分下载sqlite-autoconf-*。tar.gz。</font>
+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">Step 2</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">−运行以下命令−</font>

```powershell
$tar xvfz sqlite-autoconf-3071502.tar.gz
$cd sqlite-autoconf-3071502
$./configure --prefix=/usr/local
$make
$make install
```

<font style="color:rgb(51, 51, 51);">以上过程将在Mac OS X计算机上以SQLite安装结束。您可以通过发出以下命令来验证-</font>

```powershell
$sqlite3

SQLite version 3.7.15.2 2013-01-09 11:53:05
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```

<font style="color:rgb(51, 51, 51);">最后，您具有SQLite命令提示符，可以在其中发出用于练习的SQLite命令。</font>

