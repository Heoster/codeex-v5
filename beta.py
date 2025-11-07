import customtkinter as ctk
from tkinter import messagebox, filedialog
import subprocess
import threading
import time
import requests
import json
import os
from datetime import datetime
import psutil

class CodeexChat:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Codeex AI Chat - Powered by Ollama")
        self.window.geometry("1200x800")
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Colors
        self.primary_color = "#1e3a8a"
        self.secondary_color = "#3b82f6"
        self.accent_color = "#60a5fa"
        self.bg_color = "#0f172a"
        self.chat_bg = "#1e293b"
        self.user_msg_color = "#3b82f6"
        self.ai_msg_color = "#64748b"
        
        # Variables
        self.conversation_history = []
        self.current_chat_file = None
        self.ollama_running = False
        self.model_name = "phi3:mini"
        
        # Create directories
        os.makedirs("saved_chats", exist_ok=True)
        
        # Initialize UI
        self.setup_ui()
        
        # Auto-start Ollama
        self.auto_start_ollama()
        
    def setup_ui(self):
        # Main container
        self.window.configure(fg_color=self.bg_color)
        
        # ==================== HEADER ====================
        header_frame = ctk.CTkFrame(self.window, fg_color=self.primary_color, height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Logo and Title
        title_label = ctk.CTkLabel(
            header_frame,
            text="⚡ CODEEX AI CHAT",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="white"
        )
        title_label.pack(side="left", padx=30, pady=20)
        
        # Status indicator
        self.status_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        self.status_frame.pack(side="right", padx=30)
        
        self.status_dot = ctk.CTkLabel(
            self.status_frame,
            text="●",
            font=ctk.CTkFont(size=24),
            text_color="red"
        )
        self.status_dot.pack(side="left", padx=5)
        
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Initializing...",
            font=ctk.CTkFont(size=14),
            text_color="white"
        )
        self.status_label.pack(side="left", padx=5)
        
        # ==================== SIDEBAR ====================
        sidebar = ctk.CTkFrame(self.window, width=280, fg_color=self.chat_bg)
        sidebar.pack(side="left", fill="y", padx=0, pady=0)
        sidebar.pack_propagate(False)
        
        # Sidebar title
        sidebar_title = ctk.CTkLabel(
            sidebar,
            text="💾 Chat History",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="white"
        )
        sidebar_title.pack(pady=20, padx=20)
        
        # New Chat Button
        new_chat_btn = ctk.CTkButton(
            sidebar,
            text="➕ New Chat",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.secondary_color,
            hover_color=self.accent_color,
            height=40,
            command=self.new_chat
        )
        new_chat_btn.pack(pady=10, padx=20, fill="x")
        
        # Save Chat Button
        save_btn = ctk.CTkButton(
            sidebar,
            text="💾 Save Chat",
            font=ctk.CTkFont(size=14),
            fg_color="#059669",
            hover_color="#10b981",
            height=40,
            command=self.save_chat
        )
        save_btn.pack(pady=5, padx=20, fill="x")
        
        # Load Chat Button
        load_btn = ctk.CTkButton(
            sidebar,
            text="📂 Load Chat",
            font=ctk.CTkFont(size=14),
            fg_color="#7c3aed",
            hover_color="#8b5cf6",
            height=40,
            command=self.load_chat
        )
        load_btn.pack(pady=5, padx=20, fill="x")
        
        # Export Chat Button
        export_btn = ctk.CTkButton(
            sidebar,
            text="📄 Export to TXT",
            font=ctk.CTkFont(size=14),
            fg_color="#d97706",
            hover_color="#f59e0b",
            height=40,
            command=self.export_chat
        )
        export_btn.pack(pady=5, padx=20, fill="x")
        
        # Clear Chat Button
        clear_btn = ctk.CTkButton(
            sidebar,
            text="🗑️ Clear Display",
            font=ctk.CTkFont(size=14),
            fg_color="#dc2626",
            hover_color="#ef4444",
            height=40,
            command=self.clear_display
        )
        clear_btn.pack(pady=5, padx=20, fill="x")
        
        # Saved Chats List
        chats_label = ctk.CTkLabel(
            sidebar,
            text="Saved Conversations:",
            font=ctk.CTkFont(size=12),
            text_color="#94a3b8"
        )
        chats_label.pack(pady=(30, 10), padx=20, anchor="w")
        
        self.chats_listbox = ctk.CTkScrollableFrame(sidebar, fg_color="#0f172a")
        self.chats_listbox.pack(pady=5, padx=20, fill="both", expand=True)
        
        self.refresh_chat_list()
        
        # Footer in sidebar
        footer_label = ctk.CTkLabel(
            sidebar,
            text="Created by heoster\n© 2024 Codeex",
            font=ctk.CTkFont(size=10),
            text_color="#64748b"
        )
        footer_label.pack(side="bottom", pady=15)
        
        # ==================== MAIN CHAT AREA ====================
        main_area = ctk.CTkFrame(self.window, fg_color=self.bg_color)
        main_area.pack(side="right", fill="both", expand=True, padx=0, pady=0)
        
        # Chat display
        chat_frame = ctk.CTkFrame(main_area, fg_color="transparent")
        chat_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.chat_display = ctk.CTkTextbox(
            chat_frame,
            font=ctk.CTkFont(size=13),
            fg_color=self.chat_bg,
            text_color="white",
            wrap="word",
            state="disabled"
        )
        self.chat_display.pack(fill="both", expand=True)
        
        # Input area
        input_frame = ctk.CTkFrame(main_area, fg_color="transparent", height=100)
        input_frame.pack(fill="x", padx=20, pady=(0, 20))
        input_frame.pack_propagate(False)
        
        # Input field
        self.input_field = ctk.CTkTextbox(
            input_frame,
            font=ctk.CTkFont(size=14),
            fg_color=self.chat_bg,
            text_color="white",
            height=60,
            wrap="word"
        )
        self.input_field.pack(side="left", fill="both", expand=True, padx=(0, 10))
        self.input_field.bind("<Return>", self.send_message_event)
        self.input_field.bind("<Shift-Return>", lambda e: None)
        
        # Send button
        send_btn = ctk.CTkButton(
            input_frame,
            text="Send ➤",
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=self.secondary_color,
            hover_color=self.accent_color,
            width=120,
            height=60,
            command=self.send_message
        )
        send_btn.pack(side="right")
        
        # Welcome message
        self.display_message("System", "Welcome to Codeex AI Chat! 🚀\nInitializing Ollama service...", "system")
    
    def auto_start_ollama(self):
        """Automatically start Ollama and pull model"""
        def start_process():
            try:
                # Check if Ollama is already running
                if self.check_ollama_running():
                    self.update_status("Connected", "green")
                    self.display_message("System", "✅ Ollama service is already running!", "system")
                else:
                    self.display_message("System", "🔄 Starting Ollama service...", "system")
                    
                    # Start Ollama serve in background
                    if os.name == 'nt':  # Windows
                        subprocess.Popen(['ollama', 'serve'], 
                                       creationflags=subprocess.CREATE_NO_WINDOW)
                    else:  # Linux/Mac
                        subprocess.Popen(['ollama', 'serve'], 
                                       stdout=subprocess.DEVNULL, 
                                       stderr=subprocess.DEVNULL)
                    
                    # Wait for service to start
                    time.sleep(3)
                    
                    if self.check_ollama_running():
                        self.update_status("Connected", "green")
                        self.display_message("System", "✅ Ollama service started successfully!", "system")
                    else:
                        self.update_status("Error", "red")
                        self.display_message("System", "❌ Failed to start Ollama. Please start it manually.", "system")
                        return
                
                # Check and pull model
                self.display_message("System", f"🔍 Checking for {self.model_name} model...", "system")
                
                if not self.check_model_exists():
                    self.display_message("System", f"📥 Downloading {self.model_name}... (This may take a while)", "system")
                    self.pull_model()
                else:
                    self.display_message("System", f"✅ Model {self.model_name} is ready!", "system")
                
                self.display_message("System", "🎉 All systems ready! Start chatting below.", "system")
                self.ollama_running = True
                
            except Exception as e:
                self.update_status("Error", "red")
                self.display_message("System", f"❌ Error: {str(e)}\nPlease install Ollama from: https://ollama.ai", "system")
        
        thread = threading.Thread(target=start_process, daemon=True)
        thread.start()
    
    def check_ollama_running(self):
        """Check if Ollama service is running"""
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def check_model_exists(self):
        """Check if model is already downloaded"""
        try:
            response = requests.get("http://localhost:11434/api/tags")
            if response.status_code == 200:
                models = response.json().get('models', [])
                return any(self.model_name in model.get('name', '') for model in models)
            return False
        except:
            return False
    
    def pull_model(self):
        """Pull the model"""
        try:
            subprocess.run(['ollama', 'pull', self.model_name], check=True)
            return True
        except:
            return False
    
    def update_status(self, text, color):
        """Update status indicator"""
        self.status_label.configure(text=text)
        self.status_dot.configure(text_color=color)
    
    def display_message(self, sender, message, msg_type="user"):
        """Display message in chat"""
        self.chat_display.configure(state="normal")
        
        timestamp = datetime.now().strftime("%H:%M")
        
        if msg_type == "system":
            self.chat_display.insert("end", f"\n[{timestamp}] 🔧 SYSTEM\n", "system_sender")
            self.chat_display.insert("end", f"{message}\n", "system_msg")
            self.chat_display.insert("end", "─" * 80 + "\n", "separator")
        elif msg_type == "user":
            self.chat_display.insert("end", f"\n[{timestamp}] 👤 YOU\n", "user_sender")
            self.chat_display.insert("end", f"{message}\n", "user_msg")
        else:  # AI
            self.chat_display.insert("end", f"\n[{timestamp}] 🤖 CODEEX AI\n", "ai_sender")
            self.chat_display.insert("end", f"{message}\n", "ai_msg")
            self.chat_display.insert("end", "─" * 80 + "\n", "separator")
        
        # Configure tags (without font parameter)
        self.chat_display.tag_config("system_sender", foreground="#fbbf24")
        self.chat_display.tag_config("system_msg", foreground="#fcd34d")
        self.chat_display.tag_config("user_sender", foreground="#60a5fa")
        self.chat_display.tag_config("user_msg", foreground="#93c5fd")
        self.chat_display.tag_config("ai_sender", foreground="#34d399")
        self.chat_display.tag_config("ai_msg", foreground="#d1d5db")
        self.chat_display.tag_config("separator", foreground="#374151")
        
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")
    
    def send_message_event(self, event):
        """Handle Enter key press"""
        if not event.state & 0x1:  # Check if Shift is not pressed
            self.send_message()
            return "break"
    
    def send_message(self):
        """Send message to AI"""
        message = self.input_field.get("1.0", "end-1c").strip()
        
        if not message:
            return
        
        if not self.ollama_running:
            messagebox.showerror("Error", "Ollama service is not running!")
            return
        
        # Clear input
        self.input_field.delete("1.0", "end")
        
        # Display user message
        self.display_message("You", message, "user")
        
        # Add to history
        self.conversation_history.append({"role": "user", "content": message})
        
        # Get AI response in thread
        thread = threading.Thread(target=self.get_ai_response, args=(message,), daemon=True)
        thread.start()
    
    def get_ai_response(self, message):
        """Get response from Ollama"""
        try:
            url = "http://localhost:11434/api/chat"
            
            data = {
                "model": self.model_name,
                "messages": self.conversation_history,
                "stream": True
            }
            
            response = requests.post(url, json=data, stream=True)
            
            full_response = ""
            
            # Add initial AI message header
            timestamp = datetime.now().strftime("%H:%M")
            self.window.after(0, lambda: self.start_ai_message(timestamp))
            
            # Stream response
            for line in response.iter_lines():
                if line:
                    json_response = json.loads(line)
                    if 'message' in json_response:
                        content = json_response['message'].get('content', '')
                        full_response += content
                        
                        # Update display in real-time
                        self.window.after(0, lambda c=content: self.append_to_last_message(c))
            
            # Add to history
            self.conversation_history.append({"role": "assistant", "content": full_response})
            
            # Add separator
            self.window.after(0, lambda: self.add_separator())
            
        except Exception as e:
            self.window.after(0, lambda: self.display_message("System", f"❌ Error: {str(e)}", "system"))
    
    def start_ai_message(self, timestamp):
        """Start a new AI message"""
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", f"\n[{timestamp}] 🤖 CODEEX AI\n", "ai_sender")
        self.chat_display.tag_config("ai_sender", foreground="#34d399")
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")
    
    def append_to_last_message(self, content):
        """Append content to last message (for streaming)"""
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", content, "ai_msg")
        self.chat_display.tag_config("ai_msg", foreground="#d1d5db")
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")
    
    def add_separator(self):
        """Add separator line"""
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", "\n" + "─" * 80 + "\n", "separator")
        self.chat_display.tag_config("separator", foreground="#374151")
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")
    
    def new_chat(self):
        """Start a new chat"""
        if len(self.conversation_history) > 0:
            if messagebox.askyesno("New Chat", "Start a new conversation? Current chat will be lost if not saved."):
                self.conversation_history = []
                self.current_chat_file = None
                self.chat_display.configure(state="normal")
                self.chat_display.delete("1.0", "end")
                self.chat_display.configure(state="disabled")
                self.display_message("System", "New conversation started! 🎉", "system")
        else:
            self.conversation_history = []
            self.current_chat_file = None
            self.chat_display.configure(state="normal")
            self.chat_display.delete("1.0", "end")
            self.chat_display.configure(state="disabled")
            self.display_message("System", "New conversation started! 🎉", "system")
    
    def clear_display(self):
        """Clear chat display without clearing history"""
        self.chat_display.configure(state="normal")
        self.chat_display.delete("1.0", "end")
        self.chat_display.configure(state="disabled")
        self.display_message("System", "Display cleared! Conversation history maintained.", "system")
    
    def save_chat(self):
        """Save current chat"""
        if not self.conversation_history:
            messagebox.showinfo("Info", "No conversation to save!")
            return
        
        filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join("saved_chats", filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.conversation_history, f, indent=2, ensure_ascii=False)
        
        self.current_chat_file = filepath
        self.refresh_chat_list()
        messagebox.showinfo("Success", f"Chat saved as:\n{filename}")
    
    def load_chat(self):
        """Load a saved chat"""
        filepath = filedialog.askopenfilename(
            initialdir="saved_chats",
            title="Select chat file",
            filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
        )
        
        if filepath:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.conversation_history = json.load(f)
                
                self.current_chat_file = filepath
                
                # Display loaded conversation
                self.chat_display.configure(state="normal")
                self.chat_display.delete("1.0", "end")
                self.chat_display.configure(state="disabled")
                
                for msg in self.conversation_history:
                    role = msg.get('role', 'user')
                    content = msg.get('content', '')
                    
                    if role == 'user':
                        self.display_message("You", content, "user")
                    else:
                        self.display_message("AI", content, "ai")
                
                messagebox.showinfo("Success", "Chat loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load chat:\n{str(e)}")
    
    def export_chat(self):
        """Export chat to text file"""
        if not self.conversation_history:
            messagebox.showinfo("Info", "No conversation to export!")
            return
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
            initialfile=f"codeex_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        
        if filepath:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write("=" * 80 + "\n")
                    f.write("CODEEX AI CHAT TRANSCRIPT\n")
                    f.write(f"Created by: heoster\n")
                    f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("=" * 80 + "\n\n")
                    
                    for msg in self.conversation_history:
                        role = "YOU" if msg.get('role') == 'user' else "CODEEX AI"
                        content = msg.get('content', '')
                        f.write(f"{role}:\n{content}\n\n")
                        f.write("-" * 80 + "\n\n")
                
                messagebox.showinfo("Success", f"Chat exported to:\n{filepath}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export chat:\n{str(e)}")
    
    def refresh_chat_list(self):
        """Refresh the list of saved chats"""
        # Clear existing items
        for widget in self.chats_listbox.winfo_children():
            widget.destroy()
        
        # Get saved chats
        if os.path.exists("saved_chats"):
            chats = sorted([f for f in os.listdir("saved_chats") if f.endswith('.json')], reverse=True)
            
            for chat_file in chats[:10]:  # Show last 10 chats
                chat_btn = ctk.CTkButton(
                    self.chats_listbox,
                    text=chat_file.replace('chat_', '').replace('.json', ''),
                    font=ctk.CTkFont(size=11),
                    fg_color="#1e293b",
                    hover_color="#334155",
                    height=30,
                    anchor="w",
                    command=lambda f=chat_file: self.load_specific_chat(f)
                )
                chat_btn.pack(pady=2, padx=5, fill="x")
    
    def load_specific_chat(self, filename):
        """Load a specific chat file"""
        filepath = os.path.join("saved_chats", filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.conversation_history = json.load(f)
            
            self.current_chat_file = filepath
            
            # Display loaded conversation
            self.chat_display.configure(state="normal")
            self.chat_display.delete("1.0", "end")
            self.chat_display.configure(state="disabled")
            
            for msg in self.conversation_history:
                role = msg.get('role', 'user')
                content = msg.get('content', '')
                
                if role == 'user':
                    self.display_message("You", content, "user")
                else:
                    self.display_message("AI", content, "ai")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load chat:\n{str(e)}")
    
    def run(self):
        """Run the application"""
        self.window.mainloop()

# Run the application
if __name__ == "__main__":
    app = CodeexChat()
    app.run()
