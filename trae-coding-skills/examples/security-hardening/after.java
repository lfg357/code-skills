// ✅ 正例：参数化查询、环境变量密钥、最小权限、脱敏输出

import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;
import java.util.logging.Logger;

public class UserServlet extends HttpServlet {
    private static final Logger LOGGER = Logger.getLogger(UserServlet.class.getName());

    private final DataSource dataSource;

    public UserServlet(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) 
            throws ServletException, IOException {

        String userId = req.getParameter("id");

        // 输入验证
        if (userId == null || !userId.matches("\d+")) {
            resp.setStatus(HttpServletResponse.SC_BAD_REQUEST);
            resp.getWriter().write("{"error":"invalid id"}");
            return;
        }

        try (Connection conn = dataSource.getConnection();
             // 参数化查询，杜绝 SQL 注入
             PreparedStatement stmt = conn.prepareStatement(
                 "SELECT user_id, name, email FROM users WHERE user_id = ?"
             )) {

            stmt.setInt(1, Integer.parseInt(userId));

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    // 仅返回必要字段，敏感信息已脱敏
                    resp.setContentType("application/json");
                    resp.getWriter().write(String.format(
                        "{"user_id":%d,"name":"%s","email":"%s"}",
                        rs.getInt("user_id"),
                        escapeJson(rs.getString("name")),
                        maskEmail(rs.getString("email"))
                    ));
                } else {
                    resp.setStatus(HttpServletResponse.SC_NOT_FOUND);
                    resp.getWriter().write("{"error":"not found"}");
                }
            }
        } catch (SQLException e) {
            // 记录详细错误，但返回泛化信息
            LOGGER.severe("Database error: " + e.getMessage());
            resp.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
            resp.getWriter().write("{"error":"internal error"}");
        }
    }

    private String escapeJson(String input) {
        return input.replace("\", "\\")
                    .replace(""", "\"")
                    .replace("
", "\n");
    }

    private String maskEmail(String email) {
        int atIndex = email.indexOf("@");
        if (atIndex <= 1) return "***" + email.substring(atIndex);
        return email.charAt(0) + "***" + email.substring(atIndex);
    }
}
