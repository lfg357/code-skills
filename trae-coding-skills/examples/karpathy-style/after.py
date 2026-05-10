"""✅ 正例：命名自解释、扁平结构、显式处理"""
from typing import List, Dict
from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    event_id: str
    event_type: str
    is_active: bool
    value: int


class EventAggregator:
    """按 event_id 聚合 active user 事件的 value 总和。"""

    def __init__(self) -> None:
        self._events_by_id: Dict[str, List[Event]] = {}

    def add(self, event: Event) -> None:
        if not event.is_active:
            return
        self._events_by_id.setdefault(event.event_id, []).append(event)

    def get_aggregated_sums(self) -> List[Dict[str, object]]:
        results = []
        for event_id, events in self._events_by_id.items():
            if not events:
                continue
            total_value = sum(event.value for event in events)
            results.append({
                "event_id": event_id,
                "total_value": total_value,
            })
        return results


def aggregate_user_events(raw_events: List[dict]) -> List[Dict[str, object]]:
    """从原始数据中提取并聚合用户事件。"""
    aggregator = EventAggregator()

    for raw in raw_events:
        if raw.get("type") != "user":
            continue

        event = Event(
            event_id=raw["id"],
            event_type=raw["type"],
            is_active=raw.get("is_active", False),
            value=raw.get("value", 0),
        )
        aggregator.add(event)

    return aggregator.get_aggregated_sums()
