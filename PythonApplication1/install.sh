#!/usr/bin/bash
echo 马上安装常见的python包（一大堆）

echo 推荐的几个Python科学计算环境推荐
pip3 install -U anaconda ; echo Anaconda是一个和Canopy类似的科学计算环境
pip3 install -U Canopy ; echo Anaconda是一个和Canopy类似的科学计算环境

echo Python实现算法和设计模式

pip3 install -U algorithms ; echo Python的一个算法模块.
pip3 install -U PyPattyrn ; echo 一个用于实现常见设计模式的简单而有效的库.
pip3 install -U python-patterns ; echo Python中设计模式的集合.
pip3 install -U sortedcontainers ; echo 快速，纯Python的SortedList，SortedDict和SortedSet类型的实现.
 echo 构建工具
 echo 从源代码编译软件

pip3 install -U BitBake ; echo 一个嵌入Linux的类似make的构建工具.
pip3 install -U buildout ; echo 用于从多个部分创建、组装和部署应用程序的构建系统.
pip3 install -U PlatformIO ; echo 对不同开发平台的代码进行构建的控制台工具.
pip3 install -U PyBuilder ; echo 用不同开发平台构建代码的控制台工具.
pip3 install -U SCons ; echo 软件构建工具.
 echo 高速缓存
 echo 用于缓存数据的库

pip3 install -U Beaker ; echo 用于web应用和独立python脚本使用的缓存库.
pip3 install -U DiskCache ; echo SQLite和文件支持的缓存后端，具有比memcached和redis更快的查找功能.
pip3 install -U django-cache-machine ; echo Django模型的自动缓存.
pip3 install -U django-cacheops ; echo 支持自动或手动查询缓存，并且具有自动粒度事件驱动的ORM缓存.
pip3 install -U django-viewlet ; echo 使用扩展的缓存来控制渲染的模板部分.
pip3 install -U dogpile.cache ; echo dogpile.cache是一个缓存API，它提供了一个通用接口来缓存任何种类的后端.
pip3 install -U HermesCache ; echo 具有基于标签的无效和预防效果的Python缓存库.
pip3 install -U johnny-cache ; echo django应用程序的缓存框架.
pip3 install -U pylibmc ; echo 围绕libmemcached接口的Python包装器.
 echo 代码分析
 echo 用于分析、解析和操作代码的库和工具

pip3 install -U coala ; echo 语言独立、易于扩展的代码分析应用程序.
pip3 install -U code2flow ; echo 将你的Python和JavaScript代码转换为DOT流程图.
pip3 install -U pycallgraph ; echo 可视化你的Python应用程序的流程（调用图）的库.
pip3 install -U pysonar2 ; echo Python的类型参考和索引器.
 echo 命令行工具
 echo 用于构建命令行应用程序的库
 echo 命令行应用程序开发
pip3 install -U asciimatics ; echo 跨平台的全屏终端软件包（即鼠标/键盘输入和彩色定位的文本输出），具有复杂动画和特效的高级API.
pip3 install -U cement ; echo Python的CLI应用程序框架.
pip3 install -U click ; echo 用组合的方式创建美观的命令行界面的包.
pip3 install -U cliff ; echo 用多层次命令创建命令行程序的框架.
pip3 install -U clint ; echo Python命令行应用工具.
pip3 install -U colorama ; echo 跨平台彩色终端文本.
pip3 install -U docopt ; echo Pythonic命令行参数解析器.
pip3 install -U Gooey ; echo 将命令行程序转换成一行完整的GUI应用程序
pip3 install -U Python-Fire ; echo 用于从任何Python对象创建命令行界面（CLI）的库.
pip3 install -U python-prompt-toolkit ; echo 用于构建强大的交互式命令行的库.
 echo 生产力工具
pip3 install -U aws-cli ; echo Amazon Web Services的通用命令行界面.
pip3 install -U bashplotlib ; echo 在终端中制作基本图.
pip3 install -U caniusepython3 ; echo 确定哪些项目阻止你移植到Python 3.
pip3 install -U cookiecutter ; echo 从cookiecuters（项目模板）创建项目的命令行实用程序.
pip3 install -U doitlive ; echo 终端中现场演示的工具.
pip3 install -U howdoi ; echo 通过命令行即时编码.
pip3 install -U httpie ; echo 命令行HTTP客户端，是一个用户友好的cURL替换工具.
pip3 install -U mycli ; echo 具有自动完成和语法突出显示的MySQL的终端客户端.
pip3 install -U PathPicker ; echo 从bash输出选择文件.
pip3 install -U percol ; echo percol在UNIX上为传统的管道概念增添了交互式选择的风格.
pip3 install -U pgcli ; echo 具有自动完成和语法高亮的Postgres CLI.
pip3 install -U SAWS ; echo 增加的AWS命令行界面（CLI）.
pip3 install -U thefuck ; echo 更正你之前的控制台命令.
pip3 install -U try ; echo 令人敬畏的cli工具.
 echo 兼容性
 echo 从Python 2迁移到3的库

pip3 install -U Python-Future ; echo Python 2和Python 3之间缺少的兼容性层.
pip3 install -U Python-Modernize ; echo 使Python代码现代化，实现最终的Python 3迁移.
pip3 install -U Six ; echo Python 2和3兼容性实用程序.
 echo 计算机视觉
 echo 计算机视觉相关的库

pip3 install -U OpenCV ; echo 比较知名的计算机视觉的库.
pip3 install -U pyocr ; echo Tesseract和Cuneiform的包装.
pip3 install -U pytesseract ; echo Google Tesseract OCR的另一个包装.
pip3 install -U SimpleCV ; echo 构建计算机视觉应用程序的开源框架.
 echo 并发和并行
 echo 用于并发和并行执行的库

pip3 install -U eventlet ; echo 具有WSGI支持的异步框架.
pip3 install -U gevent ; echo 基于协同程序的Python网络库.
pip3 install -U multiprocessing ; echo Python标准库————基于流程的“线程”接口.
pip3 install -U threading ; echo （Python标准库）高级线程接口.
pip3 install -U Tomorrow ; echo 异步代码的魔术装饰器语法.
pip3 install -U uvloop ; echo uvloop是对内置的asyncio事件循环的一个快速、简单的替换。uvloop在Cython中实现，并使用libuv.
 echo 加密

pip3 install -U cryptography ; echo 一个旨在向Python开发人员提供加密算法的软件包.
pip3 install -U hashids ; echo 在Python 中实现hashids（Hashids），兼容Python 2和Python 3.
pip3 install -U Paramiko ; echo 实现SSHv2协议的Python（2.6 +，3.3+），提供客户端和服务器功能.
pip3 install -U Passlib ; echo 安全的密码存储/哈希库，非常高的安全级别.
pip3 install -U PyNacl ; echo Python绑定到网络和加密（NaCl）库.
 echo 数据分析
 echo 数据分析包

pip3 install -U Blaze ; echo NumPy和Pandas与Big Data接口.
pip3 install -U Open Mining ; echo 面向Pandas的商业智能（BI）界面.
pip3 install -U Orange ; echo 通过视觉编程或脚本进行数据挖掘、数据可视化、分析和机器学习.
pip3 install -U Pandas ; echo 量化领域数据分析最常用的一个包.
 echo 数据验证
 echo 用于验证数据的库。在许多情况下用于表格

pip3 install -U Cerberus ; echo 轻量级和可扩展的数据验证库.
pip3 install -U colander ; echo 通过XML、JSON、HTML表单文档获取和反序列化数据.
pip3 install -U jsonschema ; echo Python 的JSON Schema的实现.
pip3 install -U schema ; echo 用于验证Python数据结构的库.
pip3 install -U Schematics ; echo 数据结构验证.
pip3 install -U valideer ; echo 轻量级可扩展数据验证和适应库.
pip3 install -U voluptuous ; echo 一个Python数据验证库.
 echo 数据可视化
 echo 用于可视化数据的库

pip3 install -U Altair ; echo 使用Altair，您可以花费更多时间了解您的数据及其含义。Altair的API简单，友好和一致，建立在强大的 Vega-Lite JSON规范之上。这种优雅的简洁性以最少的代码产生了美丽而有效的可视化.
pip3 install -U Bokeh ; echo Python的交互式网络绘图.
pip3 install -U ggplot ; echo 与ggplot2相同的API.
pip3 install -U Matplotlib ; echo 一个Python 2D绘图库.
pip3 install -U Pygal ; echo 一个Python SVG图表创建者.
pip3 install -U PyGraphviz ; echo Graphviz的 Python接口.
pip3 install -U PyQtGraph ; echo 交互式和实时2D / 3D /图像绘图和科学/工程小部件.
pip3 install -U Seaborn ; echo 使用Matplotlib的统计数据可视化.
pip3 install -U VisPy ; echo 基于OpenGL的高性能科学可视化.
 echo 数据库
 echo 在Python中实现的数据库

pip3 install -U pickleDB ; echo 一个用于Python的简单轻便的键值存储.
pip3 install -U pip3elineDB ; echo 流式SQL数据库，一个开源关系数据库，可以连续地在流上运行SQL查询，并将结果逐个存储在表中.
pip3 install -U TinyDB ; echo 一个微小的、面向文档的数据库.
pip3 install -U ZODB ; echo Python的本机对象数据库.
 echo 数据库驱动程序
 echo 用于连接和操作数据库的库

pip3 install -U MySQL
pip3 install -U mysql-python ; echo 用于Python的MySQL数据库连接器.
pip3 install -U mysqlclient ; echo mysql-python fork支持Python 3.
pip3 install -U oursql ; echo 一个更好的MySQL连接器.
pip3 install -U PyMySQL ; echo 纯Python MySQL驱动程序兼容于mysql-python.
pip3 install -U PostgreSQL
pip3 install -U psycopg2 ; echo 最流行的适用于Python的PostgreSQL适配器.
pip3 install -U queries ; echo 用于与PostgreSQL交互的psycopg2库的包装器.
pip3 install -U txpostgres ; echo 用于PostgreSQL的基于Twisted的异步驱动程序.
 echo 其他关系型数据库
pip3 install -U apsw ; echo 另一个Python SQLite包装器.
pip3 install -U dataset ; echo 将Python脚本存储在数据库中 ; echo 与SQLite，MySQL和PostgreSQL一起使用.
pip3 install -U pymssql ; echo Microsoft SQL Server的简单数据库接口.
 echo 非关系型数据库
pip3 install -U cassandra-python-driver ; echo Cassandra的Python驱动程序.
pip3 install -U HappyBase ; echo 个开发人员友好的Apache HBase库.
pip3 install -U Plyvel ; echo 一个快速和功能丰富的Python接口到LevelDB.
pip3 install -U py2neo ; echo 适用于Neo4j 静态界面的 Python包装客户端.
pip3 install -U pycassa ; echo Cassandra的 Python Thrift驱动.
pip3 install -U PyMongo ; echo MongoDB的官方Python客户端.
pip3 install -U redis-py ; echo Redis Python客户端.
pip3 install -U telephus ; echo Cassandra的基于Twisted的客户端.
pip3 install -U txRedis ; echo Redis的基于Twisted的客户端.
 echo 日期和时间
 echo 处理日期和时间的库

pip3 install -U arrow ; echo Python功能强大的日期和时间库.
pip3 install -U Chronyk -用于解析人为时间和日期的Python 3库.
pip3 install -U dateutil ; echo 扩展到标准的Python datetime模块.
pip3 install -U delorean ; echo Delorean建立在pytz和dateutil之上，Delorean将为处理时间提供自然语言改进，并提供易于使用的日期时间抽象
pip3 install -U moment ; echo 处理日期/时间的Python库。灵感来自Moment.js.
pip3 install -U Pendulum ; echo Python datetimes变得容易.
pip3 install -U PyTime ; echo 一个易于使用的Python模块，旨在通过字符串操作日期/时间/日期时间.
pip3 install -U pytz ; echo 处理时区的一个库.
pip3 install -U when.py ; echo 提供用户友好的功能来帮助执行常见的日期和时间操作.
 echo 调试工具
 echo 代码调试工具的包
 echo 类似于pdb的调试器
pip3 install -U ipdb ; echo 启用了IPython的pdb.
pip3 install -U pdb++ ; echo pdb的另一个替代品.
pip3 install -U pudb ; echo 一个全屏幕的基于控制台的Python调试器.
pip3 install -U remote-pdb ; echo '远程vanilla PDB调试器（通过TCP sockets）.'
pip3 install -U wdb ; echo 通过WebSockets的Web调试器.
pip3 install -U Profiler性能分析器
pip3 install -U line_profiler ; echo 逐行剖析.
pip3 install -U memory_profiler ; echo 监视Python代码的内存使用情况.
pip3 install -U profiling ; echo 个交互式Python分析器.
pip3 install -U vprof ; echo Visual Python分析器.
 echo 其他
pip3 install -U django-debug-toolbar ; echo 显示Django的各种调试信息.
pip3 install -U django-devserver ; echo Django的runserver的替代品.
pip3 install -U flask-debugtoolbar ; echo django-debug工具栏的一个端口.
pip3 install -U hunter ; echo 一个灵活的代码跟踪工具包.
pip3 install -U lptrace ; echo strace for Python程序.
pip3 install -U manhole ; echo 调试服务，将接受unix域套接字连接，并显示所有线程的堆栈跟踪和交互式提示.
pip3 install -U pyelftools ; echo 解析和分析ELF文件和DWARF调试信息.
pip3 install -U pyringe ; echo 调试器能够附加和注入代码到Python进程.
 echo 深度学习
 echo 神经网络和深度学习框架

pip3 install -U Caffe ; echo 深度学习的一个快速上手开放框架
pip3 install -U Keras ; echo 一个高级神经网络库，能够运行在TensorFlow或者Theano之上.
pip3 install -U MXNet ; echo 一个旨在提高效率和灵活性的深度学习框架.
pip3 install -U Neupy ; echo 运行和测试不同的人工神经网络算法.
pip3 install -U Pytorch ; echo 具有强大GPU加速度的Python中的Tensors和动态神经网络.
pip3 install -U TensorFlow ; echo 由Google创建的最受欢迎的深度学习框架.
pip3 install -U Theano ; echo 快速数值计算的深度学习库.
 echo 文档
 echo 用于生成项目文档的库

pip3 install -U Sphinx ; echo Python文档生成器.
pip3 install -U MkDocs ; echo Markdown友好的文档生成器.
pip3 install -U pdoc ; echo Epydoc替换为Python库自动生成API文档.
pip3 install -U Pycco ; echo 识字编程式文档生成器.
 echo 下载器
 echo 下载方面的库

pip3 install -U s3cmd ; echo 用于管理Amazon S3和CloudFront的命令行工具.
pip3 install -U s4cmd ; echo 超级S3命令行工具，有利于更高的性能.
pip3 install -U you-get -一个用Python 3编写的YouTube /优酷/ Niconico视频下载.
pip3 install -U youtube-dl ; echo 从YouTube下载视频的小型命令行程序.
 echo 电子商务
 echo 电子商务和付款框架的库.

pip3 install -U alipay ; echo 非官方的Alipay API for Python.
pip3 install -U Cartridge ; echo Cartridge是使用Django 框架构建的购物车应用程序.
pip3 install -U django-oscar ; echo Django的开源电子商务框架.
pip3 install -U django-shop ; echo 一个基于Django的商店系统.
pip3 install -U merchant ; echo 一个Django应用程序接受来自各种支付处理器的付款.
pip3 install -U money ; echo 具有可选CLDR支持的区域设置和可扩展的货币兑换解决方案的
pip3 install -U python-currencies ; echo 显示世界各国货币格式的Python包.
pip3 install -U forex-python ; echo 外汇汇率，比特币价格指数和货币兑换.
pip3 install -U shoop ; echo 基于Django的开源电子商务平台.
 echo 编辑器插件和IDE

pip3 install -U Emacs
pip3 install -U Elpy ; echo Emacs Python开发环境.
pip3 install -U Sublime Text
pip3 install -U Anaconda ; echo Anaconda将您的Sublime Text 3转换为全功能的Python开发IDE.
pip3 install -U SublimeJEDI ; echo SublimeJEDI是一个Sublime Text 2和Sublime Text 3的插件.
pip3 install -U Vim
pip3 install -U Jedi-vim ; echo 用于Python的Jedi自动完成库的Vim绑定.
pip3 install -U Python-mode ; echo 一个将Vim转换成Python IDE的插件.
pip3 install -U YouCompleteMe ; echo 包括基于Jedi的Python完成引擎.
pip3 install -U Visual Studio
pip3 install -U PTVS ; echo Visual Studio的Python工具.
pip3 install -U Visual Studio Code
pip3 install -U Python ; echo 具有丰富的Python语言支持的扩展，其中包括linting，IntelliSense，格式化，重构，调试，单元测试和jupyter支持.
pip3 install -U Magic Python -Sublime Text，Atom和Visual Studio代码的前沿Python语法荧光笔。由GitHub用来突出显示你的Python代码！
pip3 install -U IDE
pip3 install -U LiClipse ; echo 基于Eclipse的免费polyglot IDE。使用PyDev支持Python.
pip3 install -U PyCharm ; echo JetBrains的商业Python IDE。有免费社区版可用.
pip3 install -U Spyder ; echo 开源Python IDE.
 echo 邮件
 echo 用于发送和解析邮件的库

pip3 install -U envelopes ; echo 发送邮件的库.
pip3 install -U flanker ; echo 用于发送和解析邮件的库.
pip3 install -U imbox ; echo 用于人类的Python IMAP.
pip3 install -U inbox.py ; echo 用于人类的Python SMTP服务器.
pip3 install -U lamson ; echo Pythonic SMTP应用服务器.
pip3 install -U Marrow Mailer ; echo 高性能可扩展邮件传递框架.
pip3 install -U modoboa -邮件托管和管理平台，包括现代和简化的Web UI.
pip3 install -U Nylas Sync Engine -在功能强大的电子邮件同步平台之上提供RESTful API.
pip3 install -U yagmail ; echo 另一个Gmail / SMTP客户端.
 echo 环境管理

pip3 install -U Python版本和环境管理库

pip3 install -U pip3env ; echo pip3file，pip3和Virtualenv的组合.
pip3 install -U p -交互式Python版本管理.
pip3 install -U pyenv -简单的Python版本管理.
pip3 install -U venv ; echo Python 3.3+中的 Python标准库）创建轻量级的虚拟环境.
pip3 install -U virtualenv ; echo 创建孤立的Python环境的工具.
pip3 install -U virtualenvwrapper ; echo 一组对virtualenv的扩展.
pip3 install -U GUI
 echo 用于使用图形用户界面应用程序的库

pip3 install -U curses ; echo 用于创建终端GUI应用程序的ncurses的内置包装器.
pip3 install -U enaml ; echo 使用声明式语法（如QML）创建漂亮的用户界面.
pip3 install -U Flexx ; echo Flexx是一个纯Python工具包，用于创建GUI，它使用Web技术进行渲染.
pip3 install -U kivy ; echo 用于创建在Windows，Linux，Mac OS X，Android和iOS上运行的NUI应用程序的库.
pip3 install -U pyglet ; echo 一个用于Python的跨平台窗口和多媒体库.
pip3 install -U PyGObject ; echo 用于GLib / GObject / GIO / GTK +（GTK + 3）的Python绑定
pip3 install -U PyQt ; echo 用于Qt跨平台应用程序和UI框架的Python绑定，支持Qt v4和Qt v5框架.
pip3 install -U PySide ; echo 用于Qt跨平台应用程序和UI框架的Python绑定，支持Qt v4框架.
pip3 install -U pywebview ; echo 围绕Webview组件的轻量级跨平台本机包装，允许在自己的本机专用窗口中显示HTML内容
pip3 install -U Tkinter ; echo Tkinter是Python的事实上的标准GUI包.
pip3 install -U Toga ; echo 一个Python本机的OS本机GUI工具包.
pip3 install -U urwid ; echo 用于创建终端GUI应用程序的库，具有对窗口小部件、事件、丰富颜色等的强大支持.
pip3 install -U wxPython ; echo wxWidgets C ++类库与Python的混合.
 echo 游戏开发
 echo 游戏开发库.

pip3 install -U Cocos2d ; echo Cocos2d是构建2D游戏，演示和其他图形/交互应用程序的框架。它是基于pyglet.
pip3 install -U Panda3D ; echo 迪斯尼开发和卡内基梅隆大学娱乐技术中心保持的3D游戏引擎。用C ++编写，完全包含在Python中.
pip3 install -U Pygame ; echo Pygame是一组用于编写游戏的Python模块.
pip3 install -U PyOgre ; echo Ogre 3D渲染引擎的Python绑定，可用于游戏、模拟、任何3D.
pip3 install -U PyOpenGL ; echo 用于OpenGL的Python ctypes绑定及其相关API.
pip3 install -U PySDL2 ; echo SDL2库的基于ctypes的包装器.
pip3 install -U RenPy ; echo 视觉新颖引擎.
 echo 地理位置
 echo 地理编码地图和纬度和经度的库

pip3 install -U django-countries ; echo 提供用于表单选择的Django应用程序，可以标志图标静态文件和模型的国家/地区字段.
pip3 install -U GeoDjango ; echo 世界级的地理网络框架.
pip3 install -U GeoIP ; echo 用于MaxMind GeoIP遗留数据库的Python API.
pip3 install -U geojson ; echo GeoJSON的Python绑定和实用程序.
pip3 install -U geopy ; echo Python地理编码工具箱.
pip3 install -U pygeoip -纯Python GeoIP API.
pip3 install -U HTML操作
 echo 使用HTML和XML的库

pip3 install -U BeautifulSoup ; echo Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序.
pip3 install -U bleach ; echo 理HTML（需要html5lib）.
pip3 install -U cssutils ; echo 个用于Python的CSS库.
pip3 install -U html5lib ; echo 根据WHATWG规范生成HTML/ XML文档的DOM。该规范被用在现在所有的浏览器上.
pip3 install -U lxml ; echo 一个用于处理HTML和XML的非常快速、易于使用和通用的库.
pip3 install -U MarkupSafe ; echo 为Python编写XML / HTML / XHTML标记安全字符串.
pip3 install -U pyquery ; echo 解析DOM树和jQuery选择器.
pip3 install -U untangle ; echo 轻松实现将XML文件转换为Python对象.
pip3 install -U WeasyPrint ; echo 可以导出为PDF的HTML和CSS的视觉呈现引擎.
pip3 install -U xmldataset ; echo 简单的XML解析.
pip3 install -U xmltodict ; echo 使用XML感觉就像使用JSON一样.
pip3 install -U Hardware
 echo 与硬件相关的库.

pip3 install -U ino ; echo 与Arduino合作的命令行工具包.
pip3 install -U Pingo ; echo Pingo提供统一的API来编程像Raspberry Pi、pcDuino、Intel Galileo等设备.
pip3 install -U Pyro ; echo Python机器人.
pip3 install -U PyUserInput ; echo 用于跨平台控制鼠标和键盘的模块.
pip3 install -U scapy ; echo Scapy是一个可以让用户发送、侦听和解析并伪装网络报文的Python程序。这些功能可以用于制作侦测、扫描和攻击网络的工具.
pip3 install -U wifi ; echo 在Linux上使用WiFi的Python库和命令行工具.
 echo 图像
 echo 处理图像的库

pip3 install -U hmap ; echo 图像直方图的库.
pip3 install -U imgSeek ; echo 使用视觉相似性搜索图像集合的项目.
pip3 install -U nude.py ; echo 色情图片识别的库.
pip3 install -U pagan ; echo 基于输入字符串和散列的复古识别（Avatar）生成.
pip3 install -U pillow ; echo Pillow由PIL而来，是一个图像处理库.
pip3 install -U pyBarcode ; echo 在Python中创建条形码而不需要PIL.
pip3 install -U pygram ; echo 像Instagram的图像过滤器.
pip3 install -U python-qrcode ; echo 一个纯Python QR码生成器.
pip3 install -U Quads ; echo 基于四叉树的计算机艺术.
pip3 install -U scikit-image ; echo 用于（科学）图像处理的Python库.
pip3 install -U thumbor ; echo 一个小型图像服务，具有剪裁，尺寸重设和翻转功能.
pip3 install -U wand ; echo MagickWand的 Python绑定，ImageMagick的 C API.
 echo 交互式
 echo 交互式Python解释器（REPL）

pip3 install -U bpython ; echo 强大的交互式Python终端.
pip3 install -U Jupyter Notebook （IPython） ; echo 一个丰富的工具包，可帮助您充分利用交互式使用Python.
pip3 install -U ptpython ; echo 高级Python REPL构建在python-prompt-toolkit之上.
 echo 日志
 echo 用于生成和使用日志的库

pip3 install -U Eliot ; echo 复杂和分布式系统的日志记录.
pip3 install -U logbook ; echo Logging replacement for Python.
pip3 install -U logging ; echo （Python standard library） Logging facility for Python.
pip3 install -U Sentry ; echo A realtime logging and aggregation server.
 echo 机器学习
 echo 机器学习相关的资源库.

pip3 install -U gensim ; echo Gensim是用于主题建模、文档索引 和大型语料库的相似检索的Python库.
pip3 install -U Metrics ; echo 一个Python实现的一些流行的推荐算法.
pip3 install -U NuPIC ; echo Apache Spark的可扩展机器学习库.
pip3 install -U scikit-learn ; echo 机器学习最流行的Python库.
pip3 install -U Spark ML ; echo 是一个Python scikit构建和分析推荐系统.
pip3 install -U vowpal_porpoise ; echo 一个轻量级的Python包装的Vowpal Wabbit.
pip3 install -U xgboost ; echo 可扩展、便携式和分布式梯度提升（GBDT，GBRT或GBM）库，适用于Python、R、Java、Scala、C ++等。
pip3 install -U Microsoft Windows

pip3 install -U Microsoft Windows上的Python编程

pip3 install -U Python（x,y） ; echo 基于Qt和Spyder的基于科学应用的Python分发.
pip3 install -U pythonlibs ; echo 用于Python扩展程序包的非官方Windows二进制文件.
pip3 install -U PythonNet ; echo 与.NET公共语言运行时（CLR）的Python集成.
pip3 install -U PyWin32 ; echo 适用于Windows的Python扩展.
pip3 install -U WinPython ; echo 适用于Windows 7/8的便携式开发环境.
 echo 自然语言处理
 echo 人类语言处理的库

pip3 install -U Jieba ; echo 中文分词包.
pip3 install -U langid.py ; echo 独立语言识别系统.
pip3 install -U NLTK ; echo 构建Python程序以处理人类语言数据的领先平台.
pip3 install -U Pattern ; echo Python的Web挖掘模块.
pip3 install -U SnowNLP ; echo 用于处理中文文本的库.
pip3 install -U spaCy ; echo spaCy擅长大规模的信息提取任务.
pip3 install -U TextBlob ; echo 具有文本处理 、 情绪分析、词性标注、名词短语提取、翻译等功能的一个库.
pip3 install -U TextGrocery ; echo 一种基于LibLinear和Jieba的简单、高效的短文分类工具.
 echo 包管理
 echo 一种基于LibLinear和Jieba的简单，高效的短文分类工具

pip3 install -U pip3 ; echo Python包和依赖关系管理器.
pip3 install -U conda ; echo Conda是一个开源软件包管理系统和环境管理系统，用于安装多个版本的软件包及其依赖关系，并在它们之间轻松切换。它适用于Linux，OS X和Windows，并且是为Python程序创建的，但可以打包和分发任何软件.
pip3 install -U Curdling ; echo Curdling是用于管理Python包的命令行工具.
pip3 install -U pip3-tools ; echo 能够保证你Python依赖为最新的一组工具.
pip3 install -U wheel ; echo 新的Python分发标准，旨在取代egg.
 echo 科学计算
 echo 科学计算的库

pip3 install -U astropy ; echo 一个用于天文学的社区Python库.
pip3 install -U bcbio-nextgen ; echo 其目标是克服在快速变化的研究领域工作在复杂管道上的个体开发人员的生物、算法和计算挑战.
pip3 install -U bccb ; echo 生物分析的库.
pip3 install -U Biopython ; echo Biopython是一套免费提供的生物计算工具.
pip3 install -U cclib ; echo 用于解析和解释计算化学包的结果的库.
pip3 install -U NetworkX ; echo 复杂社会网络研究的Python库.
pip3 install -U NIPY ; echo 神经成像工具包的集合.
pip3 install -U NumPy ; echo 用Python进行科学计算的基础软件包.
pip3 install -U Open Babel ; echo 一种化学工具箱，旨在呈现多种语言的化学数据.
pip3 install -U ObsPy ; echo 地震学的Python工具箱.
pip3 install -U PyDy ; echo Python Dynamics的缩写，用于协助动态运动建模中的工作流程.
pip3 install -U PyMC ; echo Python Dynamics的缩写，用于协助动态运动建模中的工作流程.
pip3 install -U RDKit ; echo 化学信息学和机器学习软件.
pip3 install -U SciPy ; echo SciPy是另一种使用NumPy来做高等数学、信号处理、优化、统计和许多其它科学任务的语言扩展。.
pip3 install -U statsmodels ; echo Python中的统计建模和计量经济学.
pip3 install -U SymPy ; echo Python中的统计建模和计量经济学.
pip3 install -U Zipline ; echo 一个Pythonic算法交易库.
pip3 install -U BigQuant ; echo 首个人工智能量化投资平台，可直接使用机器学习、深度学习技术开发量化策略; echo 特殊格式处理
 echo 用于解析和操纵特定文本格式的库

pip3 install -U General
pip3 install -U tablib ; echo 处理XLS，CSV，JSON，YAML中的表格数据集的模块.
pip3 install -U Office
pip3 install -U Marmir ; echo 使用Python数据结构并将其转换成电子表格.
pip3 install -U openpyxl ; echo 用于读写Excel 2010 xlsx / xlsm / xltx / xltm文件的库.
pip3 install -U pyexcel ; echo 提供一个用于读取，操作和编写csv、ods、xls、xlsx和xlsm文件的APIs.
pip3 install -U python-docx ; echo 读取、查询和修改Microsoft Word 2007/2008 docx文件.
pip3 install -U relatorio ; echo 模板OpenDocument文件.
pip3 install -U unoconv ; echo 转换LibreOffice / OpenOffice支持的任何文档格式.
pip3 install -U XlsxWriter ; echo 用于创建Excel .xlsx文件的Python模块.
pip3 install -U xlwings ; echo 一个BSD许可的库，可以轻松地从Excel调用Python，反之亦然.
pip3 install -U xlwt / xlrd ; echo 从Excel文件中写入和读取数据和格式化信息.
pip3 install -U PDF
pip3 install -U PDFMiner ; echo 从PDF文档中提取信息的工具.
pip3 install -U PyPDF2 ; echo 能够分割、合并和转换PDF页面的库.
pip3 install -U ReportLab ; echo 允许快速创建丰富的PDF文档.
pip3 install -U Markdown
pip3 install -U Mistune ; echo 快速、功能齐全的纯文本解析器.
pip3 install -U Python-Markdown ; echo John Gruber的Markdown的Python实现.
pip3 install -U YAML
pip3 install -U PyYAML ; echo Python的PyYAML ; echo YAML实现.
pip3 install -U CSV
pip3 install -U csvkit ; echo 用于转换和使用CSV的工具.
pip3 install -U Archive
pip3 install -U unp ; echo 一个可以轻松解压存档的命令行工具.
 echo 视频
 echo 用于操纵视频和GIF的库.

pip3 install -U moviepy ; echo 用于基于脚本的电影编辑的模块，包括动画GIF等多种格式.
pip3 install -U scikit-video ; echo SciPy的视频处理模块.
 echo 音频
 echo 用来操作音频的库

pip3 install -U audiolazy -Python 的数字信号处理包。
pip3 install -U audioread – 交叉库 （GStreamer + Core Audio + MAD + FFmpeg） 音频解码。
pip3 install -U beets – 一个音乐库管理工具及 MusicBrainz 标签添加工具
pip3 install -U dejavu – 音频指纹提取和识别
pip3 install -U django-elastic-transcoder – Django + Amazon Elastic Transcoder。
pip3 install -U eyeD3 – 一个用来操作音频文件的工具，具体来讲就是包含 ID3 元信息的 MP3 文件。
pip3 install -U id3reader – 一个用来读取 MP3 元数据的 Python 模块。
pip3 install -U m3u8 – 一个用来解析 m3u8 文件的模块。
pip3 install -U mutagen – 一个用来处理音频元数据的 Python 模块。
pip3 install -U pydub – 通过简单、简洁的高层接口来操作音频文件。
pip3 install -U pyechonest – Echo Nest API 的 Python 客户端
pip3 install -U talkbox – 一个用来处理演讲/信号的 Python 库
pip3 install -U TimeSide – 开源 web 音频处理框架。
pip3 install -U tinytag – 一个用来读取MP3, OGG, FLAC 以及 Wave 文件音乐元数据的库。
pip3 install -U mingus – 一个高级音乐理论和曲谱包，支持 MIDI 文件和回放功能。; echo 网络爬虫
 echo 网络站点爬取的库.

pip3 install -U cola ; echo 一个分布式爬虫框架.
pip3 install -U Demiurge ; echo 基于PyQuery 的爬虫微型框架.
pip3 install -U feedparser ; echo 通用 feed 解析器.
pip3 install -U Grab ; echo 站点爬取框架.
pip3 install -U MechanicalSoup ; echo 用于自动和网络站点交互的 Python 库.
pip3 install -U portia ; echo Scrapy 可视化爬取.
pip3 install -U pyspider ; echo 一个强大的爬虫系统.
pip3 install -U RoboBrowser ; echo A simple, Pythonic library for browsing the web without a standalone web browser.
pip3 install -U Scrapy ; echo 一个简单的Python 风格的库，用来浏览网站，而不需要一个独立安装的浏览器.
pip3 install -U Web框架
 echo 全栈式web框架

pip3 install -U Bottle ; echo 快速、简单和轻量级的WSGI微网框架.
pip3 install -U CherryPy ; echo 一个简约的Python Web框架，HTTP / 1.1兼容和WSGI线程池.
pip3 install -U Django ; echo Python中最流行的Web框架.
pip3 install -U Flask ; echo 一个 Python 微型框架.
pip3 install -U Pyramid ; echo 一个小而快速的，开放源码的Python Web框架.

pip3 install -U Sanic ; echo 写得快的Web服务器.

pip3 install -U Tornado ; echo 个Web框架和异步网络库.
pip3 install -U TurboGears ; echo 拥有可扩展到完整堆栈解决方案的微型功能.
pip3 install -U Web2py ; echo 用于安全数据库驱动的基于Web的应用程序的全栈企业框架.
 echo 代码质量

pip3 install -U Codacy ; echo 自动代码审查，以更快的速度运送更好的代码。免费开源.
pip3 install -U Codecov ; echo 代码覆盖仪表板.
pip3 install -U Landscape ; echo 托管连续的Python代码指标.
pip3 install -U QuantifiedCode ; echo 数据驱动、自动化、连续的代码审查工具.
