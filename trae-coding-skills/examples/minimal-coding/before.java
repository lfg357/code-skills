// ❌ 反例：过度设计、未使用代码、防御过度

import java.util.*;

public class UserProcessor {
    private static final int DEFAULT_TIMEOUT = 30;
    private static final String VERSION = "2.0.0";

    private Map<String, Object> config;
    private List<Observer> observers = new ArrayList<>();

    public UserProcessor(Map<String, Object> config) {
        this.config = config != null ? config : new HashMap<>();
    }

    public void addObserver(Observer o) {
        observers.add(o);
    }

    public List<String> processUsers(List<Map<String, String>> users) {
        // 预留扩展：未来可能支持多种处理策略
        Strategy strategy = StrategyFactory.create(config);

        List<String> result = new ArrayList<>();
        if (users == null) {
            return result; // 防御性编程
        }

        for (int i = 0; i < users.size(); i++) {
            Map<String, String> user = users.get(i);
            if (user == null) continue;

            String name = user.get("name");
            String email = user.get("email");

            if (name != null && !name.isEmpty() && email != null && email.contains("@")) {
                String formatted = String.format("User: %s <%s>", name, email);
                result.add(formatted);
            }
        }

        // 预留：未来可能通知观察者
        // for (Observer o : observers) { o.onComplete(result); }

        return result;
    }

    // 未使用的内部类
    interface Observer {
        void onComplete(List<String> result);
    }

    static class StrategyFactory {
        static Strategy create(Map<String, Object> cfg) {
            return new DefaultStrategy();
        }
    }

    interface Strategy {}
    static class DefaultStrategy implements Strategy {}
}
