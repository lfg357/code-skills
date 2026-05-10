// ❌ 反例：无基准优化、算法复杂度高、过早优化

function findDuplicates(arr) {
    const duplicates = [];

    // O(n²) 嵌套循环
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] === arr[j] && !duplicates.includes(arr[i])) {
                duplicates.push(arr[i]);
            }
        }
    }

    return duplicates;
}

// 使用
const data = Array.from({length: 50000}, () => Math.floor(Math.random() * 1000));
console.time("findDuplicates");
findDuplicates(data);
console.timeEnd("findDuplicates"); // ~5s
