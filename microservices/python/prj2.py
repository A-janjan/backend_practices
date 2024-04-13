from aiohttp import web
import time



"""
this code sets up a basic aiohttp web application with a 
single route ('/') that directs requests to a handler function. 
hen you run the application with web.run_app(), it will start 
serving requests, and the specified handler will process requests 
to the root URL.
"""

async def handle(request):
    return web.json_response({ 'time' : time.time()})


if name == '__main__':
    app = web.Application()
    app.router.append('/', handle)
    web.run_app(app)