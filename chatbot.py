import g4f
import customtkinter as ctk

def ask_gpt(prompt):
    response = g4f.ChatCompletion.create(
        model="gpt-4",  
        messages=[{"role": "user", "content": prompt}]
    )
    return response

def send_message():
    user_input = entry.get()
    if user_input.lower() in ["exit", "quit", "bye"]:
        app.destroy()
    else:
        response = ask_gpt(user_input)
        chatbox.insert("end", f"You: {user_input}\n")
        chatbox.insert("end", f"Bot: {response}\n\n")
        entry.delete(0, "end")

# UI Design
app = ctk.CTk()
app.geometry("500x600")
app.title("Chatbot App")

chatbox = ctk.CTkTextbox(app, width=480, height=400, corner_radius=10)
chatbox.pack(pady=20)

entry = ctk.CTkEntry(app, width=400)
entry.pack(pady=10)

send_button = ctk.CTkButton(app, text="Send", command=send_message)
send_button.pack(pady=10)

app.mainloop()
