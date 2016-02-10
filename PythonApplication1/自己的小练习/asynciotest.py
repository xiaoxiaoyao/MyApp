import time
import datetime
import asyncio
#在同一个线程里并行执行  异步IO
@asyncio.coroutine
def async_now(*args, **kw):
    print(datetime.datetime.now(),*args)
    print("Hello world!")    
    now_a= yield from asyncio.sleep(1)
    time.sleep(1)
    print(datetime.datetime.now(),*args)
    print("Hello sleep!")
    now_a= yield from asyncio.sleep(1)
    print(now_a)
    print(datetime.datetime.now(),*args)
    print("Hello again!",*args)
    return

print(datetime.datetime.now())
print('loop = asyncio.get_event_loop()')
run=[async_now(x) for x in range(1, 11)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(run))
loop.close