from quart_converter import app
from quart import url_for
import asyncio

async def run_url_for():
    async with app.test_request_context('/', method="GET"):
        print(url_for('person', name='Ali'))
        

loop = asyncio.get_event_loop()
loop.run_until_complete(run_url_for())