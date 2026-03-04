





# 文件（File)

# 1. open() 方法

Python open() 方法用于打开一个文件，并返回文件对象。
在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。

注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。

`open(file, mode='r')`

完整语法：

`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`

参数说明:
    
    file: 必需，文件路径（相对或者绝对路径）。
    mode: 可选，文件打开模式
    buffering: 设置缓冲
    encoding: 一般使用utf8
    errors: 报错级别
    newline: 区分换行符
    closefd: 传入的file参数类型
    opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

mode 参数有：

    t	文本模式 (默认)。
    x	写模式，新建一个文件，如果该文件已存在则会报错。
    b	二进制模式。
    +	打开一个文件进行更新(可读可写)。
    U	通用换行模式（Python 3 不支持）。
    r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
    r+	打开一个文件用于读写。文件指针将会放在文件的开头。
    rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
    w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
    w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
    a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。





# 3. Python with 关键字

在 Python 编程中，资源管理是一个重要但容易被忽视的环节。with 关键字为我们提供了一种优雅的方式来处理文件操作、数据库连接等需要明确释放资源的场景。

with 是 Python 中的一个关键字，用于上下文管理协议（Context Management Protocol）。它简化了资源管理代码，特别是那些需要明确释放或清理的资源（如文件、网络连接、数据库连接等）。





## 3.1 with 语句的基本语法

**基础用法：**

with 语句的基本形式如下：

```py
with expression [as variable]:
    # 代码块
```

- expression 返回一个支持上下文管理协议的对象
- as variable 是可选的，用于将表达式结果赋值给变量
- 代码块执行完毕后，自动调用清理方法

**文件操作示例：**

最常见的 with 语句应用是文件操作：

```py
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# 文件已自动关闭
```

这段代码等价于前面的 try-finally 实现，但更加简洁明了。





## 3.2 with 语句的工作原理

**上下文管理协议:**

with 语句背后是 Python 的上下文管理协议，该协议要求对象实现两个方法：

```py
__enter__()：进入上下文时调用，返回值赋给 as 后的变量
__exit__()：退出上下文时调用，处理清理工作
```

![image.png](attachment:4ced7bb5-1921-4ca0-82f0-e70b33835db5.png)

**异常处理机制：**

```py
__exit__() 方法接收三个参数：

exc_type：异常类型
exc_val：异常值
exc_tb：异常追踪信息
```
如果 __exit__() 返回 True，则表示异常已被处理，不会继续传播；返回 False 或 None，异常会继续向外传播。





## 3.3 实际应用场景

1. 文件操作:

   ```py
   # 同时打开多个文件
   with open('input.txt', 'r') as file, open('output.txt', 'w') as outfile:
       content = infile.read()
       outfile.write(content.upper())
   ```

   ​    

2. 数据库连接

   ```py
   import sqlite3
   
   with sqlite3.connect('database.db') as conn:
       cursor = cnn.cursor()
       cursor.execute('SELECT * FROM users')
       results = cursor.fetchall()
   # 连接自动关闭
   ```

3. 线程锁

   ```py
   import threading 
   
   lock = threading.Lock()
   
   with lock:
       # 临界区代码
       print("这段代码是线程安全的")
   ```

4. 临时修改系统状态

   ```py
   import decimal 
   
   with decimal.localcontext() as ctx:
       ctx.prec = 42  # 临时设置高精度
       # 执行高精度计算
   # 精度恢复原设置
   ```

   



## 3.4 创建自定义的上下文件管理器

### 3.4.1 类实现方式
我们可以通过实现 `__enter__` 和 `__exit__`方法创建自定义的上下文管理器：

```py
class Timer: 
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time 
        self.end = time.time()
        print(f"耗时：{self.end - self.start:.2f}秒")
        return False
    
# 使用示例
with Timer() as t:
    # 执行一些耗时操作
    sum(range(1000000))
```

### 3.4.2 使用 contextlib 模块

Python 的 `contextlib` 模块提供了更简单的方式来创建上下文管理器：

```py
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

# 使用示例
with tag("h1"):
    print("这是一个标题")
```



## 3.5 常见问题与最佳实践

### 3.5.1 常见错误

**1、错误地认为 with 只能用于文件**：

**2、忽略__exit__的返回值**.



### 3.5.2 最佳实践

1. **优先使用 with 管理资源**：对于文件、网络连接、锁等资源，总是优先考虑使用 `with` 语句
2. **保持上下文简洁**：`with` 块中的代码应该只包含与资源相关的操作
3. **合理处理异常**：在自定义上下文管理器中，根据需求决定是否抑制异常
4. **利用多个上下文**：Python 允许在单个 `with` 语句中管理多个资源





# 面向对象

## 面向对象技术简介

- **类(Class):** 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
- **方法：**类中定义的函数。
- **类变量：**类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
- **数据成员：**类变量或者实例变量用于处理类及其实例对象的相关的数据。
- **方法重写：**如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
- **局部变量：**定义在方法中的变量，只作用于当前实例的类。
- **实例变量：**在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
- **继承：**即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
- **实例化：**创建一个类的实例，类的具体对象。
- **对象：**通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

## 类定义

```python 
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

类实例化后，可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性。



## 类对象

类对象支持两种操作：属性引用和实例化。

属性引用使用和 Python 中所有的属性引用一样的标准语法：**obj.name**。

类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:

```python 
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'
 
# 实例化类
x = MyClass()
 
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
```

以上创建了一个新的类实例并将该对象赋给局部变量 x，x 为空的对象。



类有一个名为 __init__() 的特殊方法（**构造方法**），该方法在类实例化时会自动调用，像下面这样：

```py
def __init__(self):
    self.data = []
```

类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法。

 __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。如：

```python 
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
```

### self 代表类的实例，而非类

类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的**第一个参数名称**, 按照惯例它的名称是 self。

```py 
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()
```

以上实例执行结果为：

```py
<__main__.Test instance at 0x100771878>
__main__.Test
```

从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。

在 Python中，self 是一个惯用的名称，用于表示类的实例（对象）自身。它是一个指向实例的引用，使得类的方法能够访问和操作实例的属性。



## 类的方法

在类的内部，使用 **def** 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。

```py
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 实例化类
p = people('runoob',10,30)
p.speak()
```



## 继承

Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:

```py
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。

BaseClassName（实例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:



```py
class DerivedClassName(modname.BaseClassName):
```

```py
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
 
 
s = student('ken',10,60,3)
s.speak()
```



## 多继承