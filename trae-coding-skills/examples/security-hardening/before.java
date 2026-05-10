// ❌ 反例：SQL 注入、硬编码密钥、信息泄露

import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class UserServlet extends HttpServlet {
    // 硬编码密钥
    private static final String API_KEY = "sk-live-abc123xyz789";

    protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
        String userId = req.getParameter("id");

        try {
            Connection conn = DriverManager.getConnection(
                "jdbc:mysql://localhost/db", "root", "password123"
            );

            // SQL 注入漏洞
            String query = "SELECT * FROM users WHERE id = " + userId;
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            if (rs.next()) {
                // 敏感信息直接输出
                resp.getWriter().write("{"name":"" + rs.getString("name") + 
                                       "","ssn":"" + rs.getString("ssn") + ""}");
            }
        } catch (Exception e) {
            // 泄露内部堆栈
            e.printStackTrace(resp.getWriter());
        }
    }
}
