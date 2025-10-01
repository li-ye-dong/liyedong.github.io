# <font style="color:rgb(51, 51, 51);">Python 错误和内置异常</font>
<font style="color:rgb(51, 51, 51);">Python（解释器）遇到错误时会引发异常。 例如：除以零。 在本文中，您将了解Python内置的不同异常处理。</font>

<font style="color:rgb(51, 51, 51);">在编写程序时，我们经常会遇到错误。</font>

<font style="color:rgb(51, 51, 51);">由于未遵循语言的正确结构（语法）而导致的错误称为语法错误或解析错误。</font>

```python
>>> if a < 3
File "<interactive input>", line 1
if a < 3
^
SyntaxError: invalid syntax
```

<font style="color:rgb(51, 51, 51);">在这里我们可以注意到if语句中缺少一个冒号。</font>

<font style="color:rgb(51, 51, 51);">错误也可能在运行时发生，这些被称为异常。 例如，当我们尝试打开的文件不存在（FileNotFoundError），将数字除以零（ZeroDivisionError），找不到我们尝试导入的模块（ImportError）等时，就会发生这种情况。</font>

<font style="color:rgb(51, 51, 51);">每当发生这种类型的运行时错误时，Python都会创建一个异常对象。如果处理不当，它将输出对该错误的回溯，以及关于该错误发生原因的一些详细信息。</font>

```python
>>> 1 / 0
Traceback (most recent call last):
File "<string>", line 301, in runcode
File "<interactive input>", line 1, in <module>
ZeroDivisionError: division by zero

    >>> open("imaginary.txt")
    Traceback (most recent call last):
    File "<string>", line 301, in runcode
File "<interactive input>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'imaginary.txt'
```

## <font style="color:rgb(51, 51, 51);">Python内置异常</font>
<font style="color:rgb(51, 51, 51);">非法操作可能引发异常。Python中有很多内置的异常，当出现相应的错误时就会引发这些异常。我们可以使用local()内置函数查看所有的内置异常，如下所示。</font>

>>> locals()['__builtins__']

<font style="color:rgb(51, 51, 51);">这将为我们返回内置的异常，函数和属性的字典。</font>

<font style="color:rgb(51, 51, 51);">下面列出了Python编程中一些常见的内置异常以及导致该异常的错误。</font>

| <font style="color:rgb(254, 254, 254);">例外</font> | <font style="color:rgb(254, 254, 254);">错误原因</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">AssertionError</font> | <font style="color:rgb(51, 51, 51);">在assert语句失败时引发。</font> |
| <font style="color:rgb(51, 51, 51);">AttributeError</font> | <font style="color:rgb(51, 51, 51);">在属性分配或引用失败时引发。</font> |
| <font style="color:rgb(51, 51, 51);">EOFError</font> | <font style="color:rgb(51, 51, 51);">当input()函数达到文件结束条件时引发。</font> |
| <font style="color:rgb(51, 51, 51);">FloatingPointError</font> | <font style="color:rgb(51, 51, 51);">当浮点运算失败时引发。</font> |
| <font style="color:rgb(51, 51, 51);">GeneratorExit</font> | <font style="color:rgb(51, 51, 51);">在close()调用生成器的方法时引发。</font> |
| <font style="color:rgb(51, 51, 51);">ImportError</font> | <font style="color:rgb(51, 51, 51);">在找不到导入的模块时引发。</font> |
| <font style="color:rgb(51, 51, 51);">IndexError</font> | <font style="color:rgb(51, 51, 51);">当序列的索引超出范围时引发。</font> |
| <font style="color:rgb(51, 51, 51);">KeyError</font> | <font style="color:rgb(51, 51, 51);">在字典中找不到键时引发。</font> |
| <font style="color:rgb(51, 51, 51);">KeyboardInterrupt</font> | <font style="color:rgb(51, 51, 51);">当用户按下中断键（Ctrl + c或Delete）时引发。</font> |
| <font style="color:rgb(51, 51, 51);">MemoryError</font> | <font style="color:rgb(51, 51, 51);">在操作内存不足时引发。</font> |
| <font style="color:rgb(51, 51, 51);">NameError</font> | <font style="color:rgb(51, 51, 51);">在本地或全局范围内找不到变量时引发。</font> |
| <font style="color:rgb(51, 51, 51);">NotImplementedError</font> | <font style="color:rgb(51, 51, 51);">尚未实现的方法。</font> |
| <font style="color:rgb(51, 51, 51);">OSError</font> | <font style="color:rgb(51, 51, 51);">当系统操作导致系统相关错误时引发。</font> |
| <font style="color:rgb(51, 51, 51);">OverflowError</font> | <font style="color:rgb(51, 51, 51);">当算术运算的结果太大而无法表示时引发。</font> |
| <font style="color:rgb(51, 51, 51);">ReferenceError</font> | <font style="color:rgb(51, 51, 51);">在使用弱引用代理访问垃圾收集的引用对象时引发。</font> |
| <font style="color:rgb(51, 51, 51);">RuntimeError</font> | <font style="color:rgb(51, 51, 51);">当错误不属于任何其他类别时引发。</font> |
| <font style="color:rgb(51, 51, 51);">StopIteration</font> | <font style="color:rgb(51, 51, 51);">由next()函数引发，以指示迭代器没有其他项目可返回。</font> |
| <font style="color:rgb(51, 51, 51);">SyntaxError</font> | <font style="color:rgb(51, 51, 51);">遇到语法错误时由解析器引发。</font> |
| <font style="color:rgb(51, 51, 51);">IndentationError</font> | <font style="color:rgb(51, 51, 51);">缩进不正确时引发。</font> |
| <font style="color:rgb(51, 51, 51);">TabError</font> | <font style="color:rgb(51, 51, 51);">当缩进由不一致的制表符和空格组成时引发。</font> |
| <font style="color:rgb(51, 51, 51);">SystemError</font> | <font style="color:rgb(51, 51, 51);">在解释器检测到内部错误时引发。</font> |
| <font style="color:rgb(51, 51, 51);">SystemExit</font> | <font style="color:rgb(51, 51, 51);">由sys.exit()功能引发。</font> |
| <font style="color:rgb(51, 51, 51);">TypeError</font> | <font style="color:rgb(51, 51, 51);">当函数或操作应用于错误类型的对象时引发。</font> |
| <font style="color:rgb(51, 51, 51);">UnboundLocalError</font> | <font style="color:rgb(51, 51, 51);">在对函数或方法中的局部变量进行引用但没有值绑定到该变量时引发。</font> |
| <font style="color:rgb(51, 51, 51);">UnicodeError</font> | <font style="color:rgb(51, 51, 51);">在发生与Unicode相关的编码或解码错误时引发。</font> |
| <font style="color:rgb(51, 51, 51);">UnicodeEncodeError</font> | <font style="color:rgb(51, 51, 51);">在编码过程中发生与Unicode相关的错误时引发。</font> |
| <font style="color:rgb(51, 51, 51);">UnicodeDecodeError</font> | <font style="color:rgb(51, 51, 51);">在解码期间发生与Unicode相关的错误时引发。</font> |
| <font style="color:rgb(51, 51, 51);">UnicodeTranslateError</font> | <font style="color:rgb(51, 51, 51);">在翻译过程中发生Unicode相关错误时引发。</font> |
| <font style="color:rgb(51, 51, 51);">ValueError</font> | <font style="color:rgb(51, 51, 51);">当函数获取正确类型但值不正确的参数时引发。</font> |
| <font style="color:rgb(51, 51, 51);">ZeroDivisionError</font> | <font style="color:rgb(51, 51, 51);">当除法或模运算的第二个操作数为零时引发。</font> |


<font style="color:rgb(51, 51, 51);">我们也可以在Python中定义我们自己的异常(如果需要的话)。访问此页面以了解有关</font>[<font style="color:rgb(51, 51, 51);">用户定义的异常的</font>](https://www.cainiaoplus.com/python/python-user-defined-exception.html)<font style="color:rgb(51, 51, 51);">更多信息。 </font>

<font style="color:rgb(51, 51, 51);">我们可以使用try、except和finally语句</font>[<font style="color:rgb(51, 51, 51);">在Python中处理这些内置的和用户定义的异常</font>](https://www.cainiaoplus.com/python/python-exception-handling.html)<font style="color:rgb(51, 51, 51);">。</font>

# <font style="color:rgb(51, 51, 51);">Python异常处理 - Try, Except和finally</font>
<font style="color:rgb(51, 51, 51);">在本文中，您将了解如何使用try、except和finally语句在Python程序中处理异常。这将激励您用Python编写干净、可读和高效的代码。</font>

## <font style="color:rgb(51, 51, 51);">Python中的异常是什么?</font>
<font style="color:rgb(51, 51, 51);">Python有许多</font>[<font style="color:rgb(51, 51, 51);">内置的异常</font>](https://www.cainiaoplus.com/python/python-exceptions.html)<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);"> ，当其中的某些错误出现时，它们会强制您的程序输出错误。</font>

<font style="color:rgb(51, 51, 51);">当发生这些异常时，它将导致当前进程停止并将其传递给调用进程，直到被处理为止。如果不处理，我们的程序将崩溃。</font>

<font style="color:rgb(51, 51, 51);">例如，如果函数A调用函数B，后者又调用函数C，并且在函数C中发生异常。如果不在C中处理该异常，则该异常将传递给B，然后传递给A。</font>

<font style="color:rgb(51, 51, 51);">如果不进行处理，就会抛出一条错误消息，我们的程序就会意外地突然停止。</font>

## <font style="color:rgb(51, 51, 51);">在Python中捕捉异常</font>
<font style="color:rgb(51, 51, 51);">在Python中，可以使用try语句处理异常。</font>

<font style="color:rgb(51, 51, 51);">可能引发异常的关键操作放在try子句中，并且将处理异常的代码编写在except子句中。</font>

<font style="color:rgb(51, 51, 51);">捕获异常后，我们将执行什么操作取决于我们自己。这是一个简单的示例。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```python
# 导入模块sys以获取异常的类型
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)
```

**<font style="color:rgb(51, 51, 51);">输出结果</font>**

```python
The entry is a
Oops! <class 'ValueError'> occured.
Next entry.

    The entry is 0
Oops! <class 'ZeroDivisionError' > occured.
Next entry.

    The entry is 2
The reciprocal of 2 is 0.5
```

<font style="color:rgb(51, 51, 51);">在此程序中，我们循环执行，直到用户输入具有有效倒数的整数。可能导致异常的部分放在try块中。</font>

<font style="color:rgb(51, 51, 51);">如果没有异常发生，则跳过除块以外的内容，并继续正常流程。但是，如果发生任何异常，它将被except块捕获。</font>

<font style="color:rgb(51, 51, 51);">在这里，我们使用sys模块中的exinfo()函数打印异常的名称，并要求用户再试一次。我们可以看到值‘a’和‘1.3’会导致ValueError，‘0’会导致ZeroDivisionError。</font>

## <font style="color:rgb(51, 51, 51);">捕获Python中的特定异常</font>
<font style="color:rgb(51, 51, 51);">在上面的示例中，我们没有在except子句中提到任何异常。</font>

<font style="color:rgb(51, 51, 51);">这不是一个好的编程习惯，因为它将捕获所有异常并以相同的方式处理每种情况。 我们可以指定except子句会捕获哪些异常。</font>

<font style="color:rgb(51, 51, 51);">一个try子句可以有任意数量的except子句来以不同的方式处理它们，但是在发生异常时只会执行一个except子句。</font>

<font style="color:rgb(51, 51, 51);">我们可以使用值的元组在except子句中指定多个异常。下面是一个伪代码示例。</font>

```python
try:
    #执行某些代码
    pass

except ValueError:
    # 处理ValueError异常
    pass

except (TypeError, ZeroDivisionError):
    # 处理多个异常
    # TypeError 和 ZeroDivisionError 异常
    pass

except:
    # 处理所有其他异常
    pass
```

## <font style="color:rgb(51, 51, 51);">引发异常</font>
<font style="color:rgb(51, 51, 51);">在Python编程中，异常是在运行时出现相应错误时抛出的，但是我们可以使用关键字raise强制抛出异常。</font>

<font style="color:rgb(51, 51, 51);">我们还可以选择将值传递给异常，以阐明为什么会引发异常。</font>

```python
>>> raise KeyboardInterrupt
Traceback (most recent call last):
...
KeyboardInterrupt

>>> raise MemoryError("This is an argument")
Traceback (most recent call last):
...
MemoryError: This is an argument

    >>> try:
    ...     a = int(input("输入一个正整数: "))
...     if a <= 0:
...         raise ValueError("这不是一个正数!")
... except ValueError as ve:
...     print(ve)
...    
输入一个正整数: -2
这不是一个正数!
```

## <font style="color:rgb(51, 51, 51);">try...finally</font>
<font style="color:rgb(51, 51, 51);">Python中的try语句可以有一个可选的finally子句。不管在什么情况下都会执行这个子句，它通常用于释放外部资源。</font>

<font style="color:rgb(51, 51, 51);">例如，我们可以通过网络连接到远程数据中心，或者使用文件或使用图形用户界面(GUI)。</font>

<font style="color:rgb(51, 51, 51);">在所有这些情况下，无论资源是否成功，我们都必须清除该资源。这些操作（关闭文件，GUI或与网络断开连接）在finally子句中执行，以确保执行。</font>

<font style="color:rgb(51, 51, 51);">这是一个</font>[<font style="color:rgb(51, 51, 51);">文件操作</font>](https://www.cainiaoplus.com/python/python-file-operation.html)<font style="color:rgb(51, 51, 51);">的示例来说明这一点。</font>

```python
try:
    f = open("test.txt",encoding = 'utf-8')
# 执行文件操作
finally:
    f.close()
```

<font style="color:rgb(51, 51, 51);">这种类型的构造确保即使发生异常也关闭文件。</font>

# <font style="color:rgb(51, 51, 51);">Python 自定义异常</font>
<font style="color:rgb(51, 51, 51);">Python有许多</font>[<font style="color:rgb(51, 51, 51);">内置的异常</font>](https://www.cainiaoplus.com/python/python-exceptions.html)<font style="color:rgb(51, 51, 51);">，当其中的某些错误出现时，它们会强制您的程序输出错误。</font>

<font style="color:rgb(51, 51, 51);">但是，有时您可能需要创建符合您目的的自定义异常处理。</font>

<font style="color:rgb(51, 51, 51);">在Python中，用户可以通过创建新类来定义此类异常。该异常类必须直接或间接地从Exception该类派生。大多数内置异常也是从此类派生的。</font>

```python
>>> class CustomError(Exception):
    ...     pass
...

>>> raise CustomError
Traceback (most recent call last):
...
__main__.CustomError

>>> raise CustomError("An error occurred")
Traceback (most recent call last):
...
__main__.CustomError: An error occurred
```

<font style="color:rgb(51, 51, 51);">在这里，我们创建了一个名为CustomError的用户定义异常，该异常是从Exception类派生的。 与其他异常一样，可以使用带有可选错误消息的raise语句来引发此新异常。</font>

<font style="color:rgb(51, 51, 51);">当我们开发大型Python程序时，最好将程序引发的所有用户定义的异常放在单独的文件中。许多标准模块可以做到这一点。他们分别将例外定义为exceptions.py或errors.py。</font>

<font style="color:rgb(51, 51, 51);">用户定义的异常类可以实现普通类可以执行的所有操作，但是我们通常使它们简单明了。大多数实现都声明一个自定义基类，并从该基类派生其他异常类。在下面的示例中，将使该概念更清晰。</font>

## <font style="color:rgb(51, 51, 51);">示例：Python中的用户定义异常</font>
<font style="color:rgb(51, 51, 51);">在此示例中，我们将说明如何在程序中使用用户定义的异常来引发和捕获错误。</font>

<font style="color:rgb(51, 51, 51);">该程序将要求用户输入一个数字，直到他们正确猜出所存储的数字为止。为了帮助他们弄清楚，将提示他们的猜测是大于还是小于存储的数字。</font>

```python
# 定义Python用户定义的异常
class Error(Exception):
    """其他异常的基类"""
    pass

class ValueTooSmallError(Error):
    """当输入值太小时引发"""
    pass

class ValueTooLargeError(Error):
    """当输入值过大时引发"""
    pass

# 我们的主程序
# 用户猜出一个数字，直到他/她猜对为止

# 你需要猜这个数字
number = 10

while True:
    try:
        i_num = int(input("输入数字: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("这个值太小，请再试一次!")
        print()
    except ValueTooLargeError:
        print("这个值太大，请再试一次!")
        print()

print("恭喜你！ 你猜对了.")
```

<font style="color:rgb(51, 51, 51);">这是该程序的示例运行。</font>

```python
输入数字: 12
这个值太大，请再试一次!

输入数字: 0
这个值太小，请再试一次!

输入数字: 9
这个值太小，请再试一次!

输入数字: 10
恭喜你！ 你猜对了.
```

<font style="color:rgb(51, 51, 51);">在这里，我们定义了一个名为Error的基类。</font>

<font style="color:rgb(51, 51, 51);">我们的程序实际引发的另外两个异常(ValueTooSmallError和ValueTooLargeError)是从这个类派生出来的。这是在Python编程中定义用户定义异常的标准方法，但您并不仅限于此方法。  
</font>

<font style="color:rgb(51, 51, 51);">访问此页面以详细了解</font>[<font style="color:rgb(51, 51, 51);">如何处理Python中的异常</font>](https://www.cainiaoplus.com/python/python-exception-handling.html)<font style="color:rgb(51, 51, 51);">。</font>

