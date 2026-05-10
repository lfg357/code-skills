# ❌ 反例：并发 Bug、掩盖症状、未理解根因

import threading

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        try:
            self.lock.acquire()
            current = self.count
            # 模拟一些处理
            import time
            time.sleep(0.001)
            self.count = current + 1
        except Exception:
            pass  # 忽略错误，避免崩溃
        finally:
            self.lock.release()

    def get(self):
        return self.count

# 使用
from concurrent.futures import ThreadPoolExecutor

counter = Counter()
with ThreadPoolExecutor(max_workers=10) as executor:
    for _ in range(1000):
        executor.submit(counter.increment)

print(counter.get())  # 经常输出 < 1000
