package handler

import (
	"encoding/json"
	"fmt"
	"net/http"
	"runtime"
	"time"
)

func Handler(w http.ResponseWriter, r *http.Request) {
	if r.Method == "GET" {
		data := map[string]interface{}{
			"message":  "Hello from Vercel Go API!",
			"go":       runtime.Version(),
			"platform": fmt.Sprintf("%s/%s", runtime.GOOS, runtime.GOARCH),
		}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(data)
		return
	}

	if r.Method == "POST" {
		var body interface{}
		if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(map[string]string{
				"error":   "Invalid JSON body",
				"details": err.Error(),
			})
			return
		}

		loc := time.FixedZone("UTC+8", 8*60*60)
		response := map[string]interface{}{
			"received":  body,
			"timestamp": time.Now().In(loc).Format("2006-01-02T15:04:05+08:00"),
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(response)
		return
	}

	http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
}
