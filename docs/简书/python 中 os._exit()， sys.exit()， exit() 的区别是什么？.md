# python 中 os._exit()， sys.exit()， exit() 的区别是什么？

 退出方式不一样（ exit()和sys.exit()会raise **SystemExit**(code)， os._exit()直接退出。exit()基本只是在IDLE和命令行中使用）。

回答最下面有运行效果和源代码

`sys.exit`在*sysmodule.c中源代码是这样的（注意*PyErr_SetObject(PyExc_SystemExit, exit_code);，这个操作相当于raise **SystemExit**(code)：

```C
static PyObject *
sys_exit(PyObject *self, PyObject *args)
{
    PyObject *exit_code = 0;
    if (!PyArg_UnpackTuple(args, "exit", 0, 1, &exit_code))
        return NULL;
    /* Raise SystemExit so callers may catch it or clean up. */
    PyErr_SetObject(PyExc_SystemExit, exit_code);
   return NULL;
}

```

再来看看官方英文版原版解释：

[sys.exit([arg])¶](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/sys.html%3Fsys.exit%28%255Barg%255D%29%25C2%25B6%23sys.exit)

Exit from Python. This is implemented by raising the [`SystemExit`](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/exceptions.html%23SystemExit) exception, so cleanup actions specified by finally clauses of [`try`](https://link.zhihu.com/?target=https%3A//docs.python.org/3/reference/compound_stmts.html%23try) statements are honored, and it is possible to intercept the exit attempt at an outer level.

The optional argument *arg* can be an integer giving the exit status (defaulting to zero), or another type of object. If it is an integer, zero is considered “successful termination” and any nonzero value is considered “abnormal termination” by shells and the like. Most systems require it to be in the range 0–127, and produce undefined results otherwise. Some systems have a convention for assigning specific meanings to specific exit codes, but these are generally underdeveloped; Unix programs generally use 2 for command line syntax errors and 1 for all other kind of errors. If another type of object is passed, `None` is equivalent to passing zero, and any other object is printed to [`stderr`](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/sys.html%23sys.stderr) and results in an exit code of 1\. In particular, `sys.exit("some Errormessage")` is a quick way to exit a program when an error occurs.

Since [`exit()`](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/constants.html%23exit) ultimately “only” raises an exception, it will only exit the process when called from the main thread, and the exception is not intercepted.

*Changed in version 3.6:* If an error occurs in the cleanup after the Python interpreter has caught [`SystemExit`](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/exceptions.html%23SystemExit) (such as an error flushing buffered data in the standard streams), the exit status is changed to 120.

[os._exit(n)](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/os.html%23os._exit)

Exit the process with status *n*, without calling cleanup handlers, flushing stdio buffers, etc.

**Note**
The standard way to exit is `sys.exit(n)`. [`_exit()`](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/os.html%23os._exit) should normally only be used in the child process after a [`fork()`](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/os.html%23os.fork).

The following exit codes are defined and can be used with [`_exit()`](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/os.html%23os._exit), although they are not required. These are typically used for system programs written in Python, such as a mail server’s external command delivery program.

**Note**
Some of these may not be available on all Unix platforms, since there is some variation. These constants are defined where they are defined by the underlying platform.

直接运行一下看效果（因为运行时把SystemExit给 catch 了，所以 Python 不会真正退出）：

第一个：os._exit(0) ，**os._exit()直接将python解释器退出，余下的语句不会执行。**os._exit() 调用 C 语言的 _exit() 函数。相当于强制退出。

![os._exit(0)](http://upload-images.jianshu.io/upload_images/1897298-f18cf8d5db7d81a9.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

第二个：sys.exit(n) ，**调用后会引发SystemExit异常，可以捕获此异常做清理工作。甚至可以阻止程序退出。**

![sys.exit(n) ](http://upload-images.jianshu.io/upload_images/1897298-97db50c31bee6a74.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

第三个：exit()/quit()，这种实际上和sys.exit(n) 没有什么区别

![exit()/quit()](http://upload-images.jianshu.io/upload_images/1897298-0b5befc0ac2141c1.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```PYTHON 3
#代码如下，可以运行一下看效果
import os,sys
#%% os._exit(0)
try:
    print('run:    os._exit(0) # os._exit(n), 直接退出, 不抛异常, 不执行相关清理工作. 常用在子进程的退出')
    os._exit(0) # os._exit(n), 直接退出, 不抛异常, 不执行相关清理工作. 常用在子进程的退出
except:
    print('except:xiaoyao_os._exit(0)_知乎：小尧') # 不运行
finally:
    print('xiaoyao_os._exit(0)quit_知乎：小尧') # 不运行
#%% sys.exit(n)
try:# 如果在 shell 里面用 try/except 包住这样写，实际上 shell 不会退出，因为 SystemExit 被 catch 了
    sys.exit('run:xiaoyao_sys.exit(4)_知乎：小尧') #  sys.exit(n) ，sys.exit(0)最终效果一样。sys.exit()  可以sys.exit("sorry, goodbye!"); 一般主程序中使用此退出.
except SystemExit:# 如果没有 except SystemExit ，程序就能正常退出。这边为了演示，加上 except SystemExit
    print('except:xiaoyao_sys.exit(4)_知乎：小尧')
finally:
    print('xiaoyao_sys.exit(4)quit_知乎：小尧')
#%% exit()/quit()
try:# 如果在 shell 里面用 try/except 包住这样写，实际上 shell 不会退出，因为 SystemExit 被 catch 了
    quit() # exit()/quit(), 跑出SystemExit异常. 一般在交互式shell中退出时使用.
except SystemExit:# 如果没有 except SystemExit ，程序就能正常退出。这边为了演示，加上 except SystemExit
    print('except:xiaoyao_exit()_知乎：小尧')
finally:
    print('xiaoyao_exit()quit_知乎：小尧')
#%%
print('xiaoyao_能执行到这里？知乎小尧觉得不可能吧？')
'''
python3运行环境：
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
[Clang 6.0 (clang-600.0.57)] on darwin，知乎回答 written by 小尧
Type "help", "copyright", "credits" or "license" for more information.
退出代码是告诉解释器的（或操作系统）
link : https://www.zhihu.com/question/21187839/answer/569180438
'''

```
