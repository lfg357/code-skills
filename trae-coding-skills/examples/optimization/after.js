// ✅ 正例：基准测试 → 算法优化 → 验证

/**
 * 查找数组中的重复元素。
 * 
 * 基准（Node.js v20, 50000 条数据）：
 *   - 优化前：~5000ms（O(n²)）
 *   - 优化后：~8ms（O(n)）
 *   - 提升：625x
 */
function findDuplicates(arr) {
    const seen = new Set();
    const duplicates = new Set();

    for (const item of arr) {
        if (seen.has(item)) {
            duplicates.add(item);
        } else {
            seen.add(item);
        }
    }

    return Array.from(duplicates);
}

// ========== 基准测试 ==========

function benchmark(fn, arr, iterations = 5) {
    const times = [];
    for (let i = 0; i < iterations; i++) {
        const start = performance.now();
        fn(arr);
        times.push(performance.now() - start);
    }
    const avg = times.reduce((a, b) => a + b, 0) / times.length;
    return { avg, min: Math.min(...times), max: Math.max(...times) };
}

const data = Array.from({ length: 50000 }, () => Math.floor(Math.random() * 1000));
const result = benchmark(findDuplicates, data);
console.log("Benchmark:", result);
