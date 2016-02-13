import time
import datetime
import asyncio
#在同一个线程里并行执行，异步IO，python3.5新特性

async def async_now(*args, **kw):
    print(datetime.datetime.now(),' Hello once! , run now_a= await asyncio.sleep(1) ,async_id=',*args)
    now_a= await asyncio.sleep(1)
    print(datetime.datetime.now(),' Hello twice! , run time.sleep(1) ,async_id=',*args)
    time.sleep(1)
    print(datetime.datetime.now(),' Hello thrice! , run again now_a= await asyncio.sleep(1) ,async_id=',*args)
    now_a= await asyncio.sleep(1)
    print(datetime.datetime.now(),'hello four times! , now return ,async_id=',*args)
    return

print(datetime.datetime.now())
print('''
run 

run=[async_now(x) for x in range(0,7)]
loop = asyncio.get_event_loop()

''')
run=[async_now(x) for x in range(0,7)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(run))
loop.close