# ✅ 正例：根因修复 + 回归测试

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


class Counter:
    """线程安全的计数器。"""

    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()

    def increment(self):
        # 根因：原代码在锁内读取后修改，存在竞态窗口。
        # 修复：将读取+修改作为原子操作。
        with self._lock:
            self._count += 1

    def get(self):
        with self._lock:
            return self._count


# ========== 回归测试 ==========

def test_counter_thread_safety():
    """验证 1000 次并发递增结果正确。"""
    counter = Counter()
    num_threads = 10
    increments_per_thread = 100

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(lambda: [counter.increment() for _ in range(increments_per_thread)])
            for _ in range(num_threads)
        ]
        for future in as_completed(futures):
            future.result()  # 确保无异常

    expected = num_threads * increments_per_thread
    actual = counter.get()
    assert actual == expected, f"Expected {expected}, got {actual}"
    print(f"✅ Test passed: {actual} == {expected}")


if __name__ == "__main__":
    test_counter_thread_safety()
