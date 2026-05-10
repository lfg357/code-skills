// ❌ 反例：多处问题待审查

package main

import (
	"database/sql"
	"fmt"
	"net/http"
)

func GetUser(w http.ResponseWriter, r *http.Request) {
	id := r.URL.Query().Get("id")

	db, _ := sql.Open("postgres", "host=localhost user=admin password=secret123")
	defer db.Close()

	query := fmt.Sprintf("SELECT name, email FROM users WHERE id = %s", id)
	row := db.QueryRow(query)

	var name, email string
	err := row.Scan(&name, &email)
	if err != nil {
		w.WriteHeader(500)
		w.Write([]byte(err.Error()))
		return
	}

	w.Write([]byte(fmt.Sprintf(`{"name":"%s","email":"%s"}`, name, email)))
}
