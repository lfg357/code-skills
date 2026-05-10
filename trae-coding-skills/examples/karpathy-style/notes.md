# 修改点说明

1. **命名自解释**
   - `DM` → `EventAggregator`：类名即职责
   - `p/g` → `add/get_aggregated_sums`：函数名即行为
   - `d/t/a/v` → `events_by_id/event_type/is_active/value`

2. **引入数据结构**
   - 使用 `@dataclass` 替代裸 dict，显式定义字段和类型
   - `frozen=True` 保证不可变性，消除副作用风险

3. **扁平化结构**
   - 提前返回替代深层嵌套
   - 列表推导 / sum() 替代手动索引循环

4. **显式边界处理**
   - `is_active` 默认值显式声明
   - `get()` 提供默认值，避免 KeyError
