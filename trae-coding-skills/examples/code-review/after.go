// ✅ 正例：修复审查中发现的问题

package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"net/http"
	"time"

	_ "github.com/lib/pq"
)

type User struct {
	Name  string `json:"name"`
	Email string `json:"email"`
}

var db *sql.DB

func init() {
	var err error
	db, err = sql.Open("postgres", "host=localhost user=admin password=secret123")
	if err != nil {
		panic(fmt.Sprintf("connect db: %v", err))
	}
	db.SetConnMaxLifetime(5 * time.Minute)
	db.SetMaxOpenConns(25)
}

func GetUser(w http.ResponseWriter, r *http.Request) {
	id := r.URL.Query().Get("id")
	if id == "" {
		http.Error(w, `{"error":"missing id"}`, http.StatusBadRequest)
		return
	}

	var user User
	err := db.QueryRow(
		"SELECT name, email FROM users WHERE id = $1",
		id,
	).Scan(&user.Name, &user.Email)

	if err == sql.ErrNoRows {
		http.Error(w, `{"error":"not found"}`, http.StatusNotFound)
		return
	}
	if err != nil {
		http.Error(w, `{"error":"internal error"}`, http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(user)
}
