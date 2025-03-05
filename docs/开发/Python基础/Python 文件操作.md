# <font style="color:rgb(51, 51, 51);">Python 文件I/O</font>
## <font style="color:rgb(51, 51, 51);">什么是文件？</font>
<font style="color:rgb(51, 51, 51);">文件是磁盘上用于存储相关信息的命名位置。它用于将数据永久存储在非易失性存储器（例如硬盘）中。</font>

<font style="color:rgb(51, 51, 51);">由于随机存取存储器（RAM）易失，当计算机关闭时会丢失其数据，因此我们将文件用于将来的数据使用。</font>

<font style="color:rgb(51, 51, 51);">当我们要读取或写入文件时，我们需要先打开它。完成后，需要将其关闭，以便释放与文件绑定的资源。</font>

<font style="color:rgb(51, 51, 51);">因此，在Python中，文件操作按以下顺序进行。</font>

1. <font style="color:rgb(51, 51, 51);">打开文件</font>
2. <font style="color:rgb(51, 51, 51);">读取或写入（执行操作）</font>
3. <font style="color:rgb(51, 51, 51);">关闭文件</font>

## <font style="color:rgb(51, 51, 51);">如何打开文件？</font>
<font style="color:rgb(51, 51, 51);">Python具有内置函数open()来打开文件。此函数返回文件对象，也称为句柄，因为它用于相应地读取或修改文件。</font>

```python
>>> f = open("test.txt")    # 打开当前目录中的文件
>>> f = open("C:/Python33/README.txt")  # 指定完整路径
```

<font style="color:rgb(51, 51, 51);">我们可以在打开文件时指定模式。在模式下，我们指定是要读取'r'，写入'w'还是追加'a'到文件。我们还指定是否要以文本模式或二进制模式打开文件。</font>

<font style="color:rgb(51, 51, 51);">默认设置是在文本模式下阅读。在这种模式下，当从文件中读取时，我们会得到字符串。</font>

<font style="color:rgb(51, 51, 51);">另一方面，二进制模式返回字节，这是处理非文本文件（如图像或exe文件）时要使用的模式。</font>

| <font style="color:rgb(254, 254, 254);">模式</font> | <font style="color:rgb(254, 254, 254);">描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">'r'</font> | <font style="color:rgb(51, 51, 51);">打开文件进行读取。（默认）</font> |
| <font style="color:rgb(51, 51, 51);">'w'</font> | <font style="color:rgb(51, 51, 51);">打开文件进行写入。如果不存在则创建一个新文件，或者如果存在则将其截断。</font> |
| <font style="color:rgb(51, 51, 51);">'x'</font> | <font style="color:rgb(51, 51, 51);">打开文件以进行独占创建。如果文件已经存在，则操作失败。</font> |
| <font style="color:rgb(51, 51, 51);">'a'</font> | <font style="color:rgb(51, 51, 51);">打开以在文件末尾追加而不截断。如果不存在，则创建一个新文件。</font> |
| <font style="color:rgb(51, 51, 51);">'t'</font> | <font style="color:rgb(51, 51, 51);">以文本模式打开。（默认）</font> |
| <font style="color:rgb(51, 51, 51);">'b'</font> | <font style="color:rgb(51, 51, 51);">以二进制模式打开。</font> |
| <font style="color:rgb(51, 51, 51);">'+'</font> | <font style="color:rgb(51, 51, 51);">打开文件进行更新（读取和写入）</font> |


```python
f = open("test.txt")      # 等同于“ r”或“ rt”
f = open("test.txt",'w')  # 文本模式写入
f = open("img.bmp",'r+b') # 以二进制模式读取和写入
```

<font style="color:rgb(51, 51, 51);">与其他语言不同，该字符'a'在使用ASCII（或其他等效编码）进行编码之前不会暗示数字97 。</font>

<font style="color:rgb(51, 51, 51);">此外，默认编码取决于平台。在Windows中，'cp1252'但是'utf-8'在Linux中。</font>

<font style="color:rgb(51, 51, 51);">因此，我们也不能依赖默认编码，否则我们的代码在不同平台上的行为会有所不同。</font>

<font style="color:rgb(51, 51, 51);">因此，在以文本模式处理文件时，强烈建议指定编码类型。</font>

f = open("test.txt",mode = 'r',encoding = 'utf-8')

## <font style="color:rgb(51, 51, 51);">如何使用Python关闭文件？</font>
<font style="color:rgb(51, 51, 51);">完成对文件的操作后，我们需要正确关闭文件。</font>

<font style="color:rgb(51, 51, 51);">关闭文件将释放与该文件绑定的资源，并且使用close()方法完成  。</font>

<font style="color:rgb(51, 51, 51);">Python有一个垃圾收集器来清理未引用的对象，但是，我们绝对不能依靠它来关闭文件。</font>

```python
f = open("test.txt",encoding = 'utf-8')
# 执行文件操作
f.close()
```

<font style="color:rgb(51, 51, 51);">这种方法并不完全安全。如果对文件执行某些操作时发生异常，则代码将退出而不关闭文件。</font>

<font style="color:rgb(51, 51, 51);">一种更安全的方法是使用</font>[<font style="color:rgb(51, 51, 51);">try ... finally</font>](https://www.cainiaoplus.com/python/python-exception-handling.html)<font style="color:rgb(51, 51, 51);">块。</font>

```python
try:
    f = open("test.txt",encoding = 'utf-8')
# 执行文件操作
finally:
    f.close()
```

<font style="color:rgb(51, 51, 51);">这样，我们可以保证即使引发异常也可以正确关闭文件，从而导致程序流停止。</font>

<font style="color:rgb(51, 51, 51);">最好的方法是使用with语句。这样可以确保在with退出内部块时关闭文件。</font>

<font style="color:rgb(51, 51, 51);">我们不需要显式调用该close()方法。它是在内部完成的。</font>

```python
with open("test.txt",encoding = 'utf-8') as f:
    # 执行文件操作
```

## <font style="color:rgb(51, 51, 51);">如何使用Python写入文件？</font>
<font style="color:rgb(51, 51, 51);">为了用Python写入文件，我们可以以 'w' 模式写入，'a'模式追加或独占创建'x'模式打开它。</font>

<font style="color:rgb(51, 51, 51);">我们需要谨慎使用该'w'模式，因为它会覆盖文件（如果已存在）。以前的所有数据都将被删除。</font>

<font style="color:rgb(51, 51, 51);">写入字符串或字节序列（对于二进制文件）是使用write()方法完成的。此方法返回写入文件的字符数。</font>

```python
with open("test.txt",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
```

<font style="color:rgb(51, 51, 51);">'test.txt'如果不存在，该程序将创建一个名为的新文件。如果确实存在，则将其覆盖。</font>

<font style="color:rgb(51, 51, 51);">我们必须自己包括换行符，以区分不同的行。</font>

## <font style="color:rgb(51, 51, 51);">如何在Python中读取文件？</font>
<font style="color:rgb(51, 51, 51);">要使用Python读取文件，我们必须以读取模式打开文件。</font>

<font style="color:rgb(51, 51, 51);">有多种方法可用于此目的。我们可以使用该read(size)方法读取</font><font style="color:rgb(51, 51, 51);">大小</font><font style="color:rgb(51, 51, 51);">数据。如果未指定</font><font style="color:rgb(51, 51, 51);">size</font><font style="color:rgb(51, 51, 51);">参数，它将读取并返回到文件末尾。</font>

```python
>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # 读取前4个数据
'This'

>>> f.read(4)    # 读取接下来的4个数据
' is '

>>> f.read()     # 读取其余部分，直到文件末尾
'my first file\nThis file\ncontains three lines\n'

>>> f.read()  # 进一步读取返回空字符串
''
```

<font style="color:rgb(51, 51, 51);">我们可以看到，read()方法将换行符返回为'\n'。到达文件末尾后，我们将在进一步阅读时得到空字符串。</font>

<font style="color:rgb(51, 51, 51);">我们可以使用seek()方法更改当前文件的光标（位置）。同样，tell()方法返回我们的当前位置（以字节数为单位）。</font>

```python
>>> f.tell()    # 获取当前文件位置
56

>>> f.seek(0)   # 将文件光标移到初始位置
0

>>> print(f.read())  # 读取整个文件
This is my first file
This file
contains three lines
```

<font style="color:rgb(51, 51, 51);">我们可以使用</font>[<font style="color:rgb(51, 51, 51);">for循环</font>](https://www.cainiaoplus.com/python/python-for-loop.html)<font style="color:rgb(51, 51, 51);">逐行读取文件。这既高效又快速。</font>

```python
>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines
```

<font style="color:rgb(51, 51, 51);">文件本身的行具有换行符'\n'。</font>

<font style="color:rgb(51, 51, 51);">此外，print()结束参数在打印时避免了两行换行。</font>

<font style="color:rgb(51, 51, 51);">或者，我们可以使用readline()方法读取文件的各个行。此方法读取文件，直到换行符为止，包括换行符。</font>

```python
>>> f.readline()
'This is my first file\n'

>>> f.readline()
'This file\n'

>>> f.readline()
'contains three lines\n'

>>> f.readline()
''
```

<font style="color:rgb(51, 51, 51);">最后，该readlines()方法返回整个文件的其余行的列表。当到达文件结尾（EOF）时，所有这些读取方法都将返回空值。</font>

```python
>>> f.readlines()
['This is my first file\n', 'This file\n', 'contains three lines\n']
```

## <font style="color:rgb(51, 51, 51);">Python文件方法</font>
<font style="color:rgb(51, 51, 51);">文件对象有多种可用方法。其中一些已在以上示例中使用。</font>

<font style="color:rgb(51, 51, 51);">这是文本模式下方法的完整列表，并带有简要说明。</font>

| [<font style="color:rgb(51, 51, 51);">close()</font>](https://www.cainiaoplus.com/python/python-file-close.html) | <font style="color:rgb(51, 51, 51);">关闭文件。</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">detach()</font> | <font style="color:rgb(51, 51, 51);">从缓冲区返回分离的原始流（raw stream）。</font> |
| [<font style="color:rgb(51, 51, 51);">fileno()</font>](https://www.cainiaoplus.com/python/python-file-fileno.html) | <font style="color:rgb(51, 51, 51);">从操作系统的角度返回表示流的数字。</font> |
| [<font style="color:rgb(51, 51, 51);">flush()</font>](https://www.cainiaoplus.com/python/python-file-flush.html) | <font style="color:rgb(51, 51, 51);">刷新内部缓冲区。</font> |
| [<font style="color:rgb(51, 51, 51);">isatty()</font>](https://www.cainiaoplus.com/python/python-file-isatty.html) | <font style="color:rgb(51, 51, 51);">返回文件流是否是交互式的。</font> |
| [<font style="color:rgb(51, 51, 51);">read()</font>](https://www.cainiaoplus.com/python/python-file-read.html) | <font style="color:rgb(51, 51, 51);">返回文件内容。</font> |
| [<font style="color:rgb(51, 51, 51);">readable()</font>](https://www.cainiaoplus.com/python/python-file-readable.html) | <font style="color:rgb(51, 51, 51);">返回是否能够读取文件流。</font> |
| [<font style="color:rgb(51, 51, 51);">readline()</font>](https://www.cainiaoplus.com/python/python-file-readline.html) | <font style="color:rgb(51, 51, 51);">返回文件中的一行。</font> |
| [<font style="color:rgb(51, 51, 51);">readlines()</font>](https://www.cainiaoplus.com/python/python-file-readlines.html) | <font style="color:rgb(51, 51, 51);">返回文件中的行列表。</font> |
| [<font style="color:rgb(51, 51, 51);">seek()</font>](https://www.cainiaoplus.com/python/python-file-seek.html) | <font style="color:rgb(51, 51, 51);">更改文件位置。</font> |
| [<font style="color:rgb(51, 51, 51);">seekable()</font>](https://www.cainiaoplus.com/python/python-file-seekable.html) | <font style="color:rgb(51, 51, 51);">返回文件是否允许我们更改文件位置。</font> |
| [<font style="color:rgb(51, 51, 51);">tell()</font>](https://www.cainiaoplus.com/python/python-file-tell.html) | <font style="color:rgb(51, 51, 51);">返回当前的文件位置。</font> |
| [<font style="color:rgb(51, 51, 51);">truncate()</font>](https://www.cainiaoplus.com/python/python-file-truncate.html) | <font style="color:rgb(51, 51, 51);">把文件调整为指定的大小。</font> |
| [<font style="color:rgb(51, 51, 51);">writeable()</font>](https://www.cainiaoplus.com/python/python-file-writeable.html) | <font style="color:rgb(51, 51, 51);">返回是否能够写入文件。</font> |
| [<font style="color:rgb(51, 51, 51);">write()</font>](https://www.cainiaoplus.com/python/python-file-write.html) | <font style="color:rgb(51, 51, 51);">把指定的字符串写入文件。</font> |
| [<font style="color:rgb(51, 51, 51);">writelines()</font>](https://www.cainiaoplus.com/python/python-file-writelines.html) | <font style="color:rgb(51, 51, 51);">把字符串列表写入文件。</font> |


# <font style="color:rgb(51, 51, 51);">Python 目录和文件管理</font>
<font style="color:rgb(51, 51, 51);">在本文中，您将了解Python中的文件和目录管理，即创建一个目录，重命名它，列出所有目录并使用它们。</font>

## <font style="color:rgb(51, 51, 51);">Python中的目录是什么？</font>
<font style="color:rgb(51, 51, 51);">如果您的Python程序中</font>[<font style="color:rgb(51, 51, 51);">要处理</font>](https://www.cainiaoplus.com/python/python-file-operation.html)<font style="color:rgb(51, 51, 51);">大量</font>[<font style="color:rgb(51, 51, 51);">文件</font>](https://www.cainiaoplus.com/python/python-file-operation.html)<font style="color:rgb(51, 51, 51);">，则可以将代码排列在不同的目录中，以使事情更易于管理。</font>

<font style="color:rgb(51, 51, 51);">目录或文件夹是文件和子目录的集合。Python具有os</font><font style="color:rgb(51, 51, 51);"> </font>[<font style="color:rgb(51, 51, 51);">模块</font>](https://www.cainiaoplus.com/python/python-modules.html)<font style="color:rgb(51, 51, 51);">，它为我们提供了许多使用目录（和文件）的有用方法。</font>

## <font style="color:rgb(51, 51, 51);">获取当前目录</font>
<font style="color:rgb(51, 51, 51);">我们可以使用该getcwd()方法获取当前的工作目录。</font>

<font style="color:rgb(51, 51, 51);">此方法以字符串形式返回当前工作目录。我们还可以使用getcwdb()方法将其作为字节对象获取。</font>

```python
>>> import os

>>> os.getcwd()
'C:\\Program Files\\PyScripter'

>>> os.getcwdb()
b'C:\\Program Files\\PyScripter'
```

<font style="color:rgb(51, 51, 51);">额外的反斜杠表示转义序列。print()函数将正确地呈现它。</font>

```python
>>> print(os.getcwd())
C:\Program Files\PyScripter
```

## <font style="color:rgb(51, 51, 51);">更改目录</font>
<font style="color:rgb(51, 51, 51);">我们可以使用chdir()方法更改当前工作目录。</font>

<font style="color:rgb(51, 51, 51);">我们要更改的新路径必须作为字符串提供给此方法。我们可以使用正斜杠（/）或反斜杠（\）来分隔路径。</font>

<font style="color:rgb(51, 51, 51);">使用反斜杠时，用转义序列更安全。</font>

```python
>>> os.chdir('C:\\Python33')

>>> print(os.getcwd())
C:\Python33
```

## <font style="color:rgb(51, 51, 51);">列出目录和文件</font>
<font style="color:rgb(51, 51, 51);">使用listdir()方法可以知道目录内的所有文件和子目录。</font>

<font style="color:rgb(51, 51, 51);">此方法采用一个路径，并返回该路径中的子目录和文件的列表。如果未指定路径，它将从当前工作目录返回。</font>

```python
>>> print(os.getcwd())
C:\Python33

>>> os.listdir()
['DLLs',
 'Doc',
 'include',
 'Lib',
 'libs',
 'LICENSE.txt',
 'NEWS.txt',
 'python.exe',
 'pythonw.exe',
 'README.txt',
 'Scripts',
 'tcl',
 'Tools']

>>> os.listdir('G:\\')
['$RECYCLE.BIN',
 'Movies',
 'Music',
 'Photos',
 'Series',
 'System Volume Information']
```

## <font style="color:rgb(51, 51, 51);">创建新目录</font>
<font style="color:rgb(51, 51, 51);">我们可以使用mkdir()方法创建一个新目录。</font>

<font style="color:rgb(51, 51, 51);">此方法采用新目录的路径。如果未指定完整路径，则会在当前工作目录中创建新目录。</font>

```python
>>> os.mkdir('test')

>>> os.listdir()
['test']
```

## <font style="color:rgb(51, 51, 51);">重命名目录或文件</font>
<font style="color:rgb(51, 51, 51);">rename()方法可以重命名目录或文件。</font>

<font style="color:rgb(51, 51, 51);">第一个参数是旧名称，而新名称必须作为第二个参数。</font>

```python
>>> os.listdir()
['test']

>>> os.rename('test','new_one')

>>> os.listdir()
['new_one']
```

## <font style="color:rgb(51, 51, 51);">删除目录或文件</font>
<font style="color:rgb(51, 51, 51);">使用remove()方法可以删除（删除）文件。</font>

<font style="color:rgb(51, 51, 51);">同样，rmdir()方法将删除一个空目录。</font>

```python
>>> os.listdir()
['new_one', 'old.txt']

>>> os.remove('old.txt')
>>> os.listdir()
['new_one']

>>> os.rmdir('new_one')
>>> os.listdir()
[]
```

<font style="color:rgb(51, 51, 51);">但是，请注意rmdir()方法只能删除空目录。</font>

<font style="color:rgb(51, 51, 51);">为了删除一个非空目录，我们可以使用shutil模块内部的rmtree()方法。</font>

```python
>>> os.listdir()
['test']

>>> os.rmdir('test')
Traceback (most recent call last):
...
OSError: [WinError 145] The directory is not empty: 'test'

>>> import shutil

>>> shutil.rmtree('test')
>>> os.listdir()
[]
```



