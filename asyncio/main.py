import time
import asyncio


# Synchronous: Blocking, sequential execution.
def sync_example():
    print('sync_example')
    time.sleep(5)     # Blocks execution for 5 seconds
    print('sync_example done')
    
# sync_example()


# Asynchronous: Non-blocking, concurrent execution using async/await.
async def async_example():
    print('async_example')
    await asyncio.sleep(5)    # Blocks execution for 5 seconds
    print('async_example done')

asyncio.run(async_example())

