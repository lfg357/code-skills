// ✅ 正例：只实现需求，删除一切非必要代码

import java.util.List;
import java.util.Map;
import java.util.ArrayList;

public class UserFormatter {

    public List<String> formatValidUsers(List<Map<String, String>> users) {
        List<String> result = new ArrayList<>();

        for (Map<String, String> user : users) {
            String name = user.get("name");
            String email = user.get("email");

            if (isValid(name, email)) {
                result.add("User: " + name + " <" + email + ">");
            }
        }

        return result;
    }

    private boolean isValid(String name, String email) {
        return name != null && !name.isBlank()
            && email != null && email.contains("@");
    }
}
