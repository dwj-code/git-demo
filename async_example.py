import asyncio
import time

async def my_async_function():
    """
    异步函数示例：包含两次await等待（顺序执行）
    """
    print(f"开始执行: {time.strftime('%H:%M:%S')}")
    
    # 第一次await：等待1秒
    print("等待1秒...")
    await asyncio.sleep(1)
    print(f"1秒后: {time.strftime('%H:%M:%S')}")
    
    # 第二次await：等待2秒
    print("等待2秒...")
    await asyncio.sleep(2)
    print(f"2秒后: {time.strftime('%H:%M:%S')}")
    
    print("异步函数执行完成！")

async def my_async_function_parallel():
    """
    真正的异步函数：同时执行两个等待（总共只需要2秒）
    """
    print(f"开始并行执行: {time.strftime('%H:%M:%S')}")
    
    # 同时启动两个等待任务
    task1 = asyncio.create_task(asyncio.sleep(1))
    task2 = asyncio.create_task(asyncio.sleep(2))
    
    print("同时等待1秒和2秒...")
    
    # 等待两个任务都完成
    await asyncio.gather(task1, task2)
    
    print(f"并行执行完成: {time.strftime('%H:%M:%S')}")
    print("总共只等待了2秒！")

# 运行异步函数
async def main():
    print("=== 顺序执行（等待3秒）===")
    await my_async_function()
    
    print("\n=== 并行执行（等待2秒）===")
    await my_async_function_parallel()

if __name__ == "__main__":
    # 在Windows上使用asyncio.run()
    asyncio.run(main())
