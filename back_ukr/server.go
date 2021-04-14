package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os/exec"
	"strings"

	socketio "github.com/googollee/go-socket.io"
)

type TranRequest struct {
	FromSystem string `json:"fromSystem"`
	ToSystem   string `json:"toSystem"`
	Text       string `json:"text"`
}

type Resp struct {
	Success bool   `json:"success"`
	Message string `json:"message"`
}

func tranFunc(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	SystemMap := map[string]bool{"ky": true, "ln": true, "ld": true}

	var (
		message TranRequest
		resp    Resp
	)
	_ = json.NewDecoder(r.Body).Decode(&message)

	if SystemMap[message.FromSystem] && message.FromSystem != "ld" {
		if SystemMap[message.ToSystem] {
			resp.Success = true
			if message.FromSystem == message.ToSystem {
				resp.Message = message.Text
			} else {
				text := fmt.Sprintf("import worker; print(worker.translate('%s', '%s', '%s'), end=\"\")", message.FromSystem, message.ToSystem, message.Text)
				cmd := exec.Command("python3", "-c", text)
				out, err := cmd.CombinedOutput()
				if err != nil {
					fmt.Println(err)
				}
				resp.Message = string(out)
			}
			json.NewEncoder(w).Encode(resp)
			return
		} else {
			resp.Message = "Incorrect value of 'toSystem'"
		}
	} else {
		resp.Message = "Incorrect value of 'FromSystem'"
	}
	resp.Success = false
	json.NewEncoder(w).Encode(resp)
}

func main() {
	server := socketio.NewServer(nil)

	server.OnConnect("/", func(s socketio.Conn) error {
		fmt.Println("connected:", s.ID())
		return nil
	})

	server.OnEvent("/", "translate", func(s socketio.Conn, data map[string]string) {
		text := fmt.Sprintf("import worker; print(worker.translate('%s', '%s', \"\"\"%s\"\"\"), end=\"\")", data["fromSystem"], data["toSystem"], data["text"])
		cmd := exec.Command("python3", "-c", text)
		out, err := cmd.CombinedOutput()
		if err != nil {
			fmt.Println(err)
		}
		newText := strings.Replace(string(out), "\n", "<br>", -1)
		s.Emit("translated", newText)
	})

	server.OnError("/", func(s socketio.Conn, e error) {
		fmt.Println("meet error:", e)
	})

	server.OnDisconnect("/", func(s socketio.Conn, reason string) {
		fmt.Println("closed", reason)
	})

	go server.Serve()
	defer server.Close()

	http.Handle("/socket.io/", server)

	http.Handle("/", http.FileServer(http.Dir("../front_ukr")))

	http.HandleFunc("/api/translate", tranFunc)

	log.Println("Serving at localhost:8000...")
	log.Fatal(http.ListenAndServe(":8000", nil))
}
