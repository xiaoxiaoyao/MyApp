
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
'''
