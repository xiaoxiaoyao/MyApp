# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level=logging.DEBUG)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

###这些全都是异步，aiohttp就是异步，所以要async
async def hellow_world(request):
    text=b'<h1>hellow world!</h1>'
    ###最简单的hellow world!，最基础的return
    return web.Response(body=text)

async def echo(request):
    echo1 = request.match_info.get('echo1', "None")
    echo2 = request.match_info.get('echo2', "None")
    text = "<html><body><p>Hello, </p><h1>echo1 is " + echo1 + "</h1><h2>echo2 is " + echo2 + "</h2></body></html>"
    ###如果WEB页面都这样写，就没法维护了，所以还得靠模板
    return web.Response(body=text.encode('utf-8'))

###下面是https://pypi.python.org/pypi/aiohttp给出的官方例子
async def wshandler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.tp == web.MsgType.text:
            ws.send_str("Hello, {}".format(msg.data))
        elif msg.tp == web.MsgType.binary:
            ws.send_bytes(msg.data)
        elif msg.tp == web.MsgType.close:
            break

    return ws

app = web.Application(debug=True)
app.router.add_route('GET', '/', hellow_world)
app.router.add_route('GET', '/echo', wshandler)
app.router.add_route('GET', '/{echo1}/{echo2}', echo)###app.router.add_route妥妥的会被注入啊
logging.info('server started at http://127.0.0.1:9000...')
web.run_app(app,host='127.0.0.1',port=9000)