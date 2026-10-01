import tkinter as tk
import re
import random
import sys
import os
import ctypes





def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller .exe"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def load_custom_font(font_path):
    """Temporarily loads a font into Windows memory just for this app."""
    FR_PRIVATE = 0x10
    
    if os.path.exists(font_path):
        ctypes.windll.gdi32.AddFontResourceExW(font_path, FR_PRIVATE, 0)


load_custom_font(resource_path(os.path.join("fonts", "Silkscreen-Regular.ttf")))
load_custom_font(resource_path(os.path.join("fonts", "Audiowide-Regular.ttf")))






KNOWLEDGE_BASE = {
    "greetings": {
        "keywords": ["hi", "hello", "hey", "yo", "sup"],
        "responses": ["Hi there!", "Hey! So good to hear from you.", "Hello! What's on your mind?", "Hey! How's your day?"]
    },
    "well_being": {
        "keywords": ["how", "are", "you", "doing", "been", "fine", "good", "okay"],
        "responses": ["I'm doing great, thank you! And you?", "I'm good! Just having a nice day.", "Doing really well! Hope you are too."]
    },
    "school_venting": {
        "keywords": ["school", "homework", "exam", "boards", "teacher", "sucks", "study"],
        "responses": ["School can be a lot. Make sure to take breaks!", "Don't stress too much, you're doing great."]
    },
    "invite_play": {
        "keywords": ["wanna", "lets", "join", "lobby", "ready", "coop"],
        "responses": ["Sure, I'd love to play!", "Sounds like fun. Let's do it!"]
    },
    "gaming": {
        "keywords": ["game", "play", "playing", "boss", "stuck", "mech", "hollow", "mod"],
        "responses": ["That sounds like a fun game!", "Gaming is the best way to relax."]
    },
    "weekend_vibes": {
        "keywords": ["weekend", "bored", "free", "music", "lofi", "vibe", "chill", "tired"],
        "responses": ["Time to just relax and be happy.", "Listening to music is a great idea."]
    }
}

FALLBACK_RESPONSES = [
    "That's really nice.", "Oh, cool!", "I see what you mean.", 
    "That makes sense.", "Tell me more about that!", "Sounds good to me."
]








def clean_input(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()

def get_response(user_input):
    words = clean_input(user_input)
    for category, data in KNOWLEDGE_BASE.items():
        for keyword in data["keywords"]:
            if keyword in words:
                return random.choice(data["responses"])
    return random.choice(FALLBACK_RESPONSES)

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))










class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatterbox OS")
        
        try:
            self.root.state('zoomed')
        except:
            self.root.attributes('-fullscreen', True)

       
        self.grad_top = "#0f172a"    
        self.grad_bot = "#334155"    
        self.text_main = "#ffffff"   
        self.text_sub = "#cbd5e1"    
        self.accent = "#3b82f6"      
        self.box_bg = "#1e293b"      
        
        self.font_header = ("Silkscreen", 42, "bold")
        self.font_title = ("Silkscreen", 26)
        self.font_body = ("Audiowide", 18)
        self.font_btn = ("Audiowide", 16, "bold")
        
        self.user_name = "Person A"
        self.bot_name = "Person B"
        self.current_page = None

        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.root.bind_all("<MouseWheel>", self.on_mousewheel)
        
        self.draw_gradient()
        self.show_intro_screen()

    def draw_gradient(self):
        r1, g1, b1 = hex_to_rgb(self.grad_top)
        r2, g2, b2 = hex_to_rgb(self.grad_bot)
        limit = 3500 
        for i in range(limit):
            nr = int(r1 + (r2 - r1) * i / limit)
            ng = int(g1 + (g2 - g1) * i / limit)
            nb = int(b1 + (b2 - b1) * i / limit)
            color = f"#{nr:02x}{ng:02x}{nb:02x}"
            self.canvas.create_line(0, i, 4000, i, fill=color)

    def on_mousewheel(self, event):
        if self.current_page == "intro":
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def clear_elements(self):
        self.canvas.delete("ui")
        for widget in self.root.place_slaves():
            widget.destroy()






    def show_intro_screen(self):
        self.clear_elements()
        self.current_page = "intro"
        
        self.canvas.yview_moveto(0)
        self.canvas.config(scrollregion=(0, 0, 2000, 2200)) 
        
       
        self.canvas.create_text(150, 100, text="MY VIRTUAL FRIEND", font=self.font_header, fill=self.text_main, anchor="nw", tags="ui")
        
        
        self.canvas.create_text(150, 250, text="WHAT IS A CHATTERBOX?", font=self.font_title, fill=self.accent, anchor="nw", tags="ui")
        text_1 = (
            "A Chatterbox is a modern implementation of a classic computer science milestone: the rule-based "
            "conversational agent. Long before the invention of Large Language Models (LLMs) and complex neural networks, "
            "developers built chatbots using pure deterministic logic.\n\n"
            "This application is a tribute to that era of programming. It contains absolutely zero artificial intelligence. "
            "It does not think, it does not learn, and it does not inherently understand the meaning of the words you type. "
            "Instead, it operates entirely on mechanical logic and string manipulation."
        )
        self.canvas.create_text(150, 310, text=text_1, font=self.font_body, fill=self.text_sub, anchor="nw", width=1400, tags="ui")
        

        self.canvas.create_text(150, 600, text="HOW IT WORKS UNDER THE HOOD", font=self.font_title, fill=self.accent, anchor="nw", tags="ui")
        text_2 = (
            "At its core, this system relies on explicit pattern matching and a hardcoded 'Knowledge Base.'\n\n"
            "When you transmit a message, the engine instantly strips away all punctuation and converts your string to "
            "lowercase to standardize the data. It then scans your input against arrays of predefined keyword clusters.\n\n"
            "If a mathematical match is found (e.g., the system detects the exact string 'homework' or 'stuck'), it routes "
            "the execution flow to a specific dictionary key. It then retrieves a randomized, pre-written response from "
            "that category to simulate a fluid conversation."
        )
        self.canvas.create_text(150, 660, text=text_2, font=self.font_body, fill=self.text_sub, anchor="nw", width=1400, tags="ui")
        

        self.canvas.create_text(150, 950, text="CRITICAL SYSTEM LIMITATIONS", font=self.font_title, fill=self.accent, anchor="nw", tags="ui")
        text_3 = (
            "Because this is a rule-based system, you will encounter strict boundaries while interacting with it:\n\n"
            "• NO CONTEXTUAL AWARENESS: The program evaluates strings purely on a syntactic level. It does not comprehend "
            "semantic meaning. If you type 'I am not stressed about school', it only sees the keyword 'school' and may "
            "incorrectly offer a sympathetic response about academic stress.\n\n"
            "• ABSOLUTE ZERO MEMORY: The system operates entirely statelessly. Each input is processed in a vacuum. It cannot "
            "remember your previous message, reference past topics, or hold a continuous train of thought.\n\n"
            "• STRICT SYNTAX DEPENDENCY: Unrecognized synonyms, severe spelling errors, or modern slang that isn't manually "
            "hardcoded into the dictionary will cause the logic to bypass all specific categories and trigger a generic fallback sequence.\n\n"
            "• STATIC OUTPUT GENERATION: It cannot synthesize novel text. Every single response you see has been manually typed. "
            "There is no generative capability."
        )
        self.canvas.create_text(150, 1010, text=text_3, font=self.font_body, fill=self.text_sub, anchor="nw", width=1400, tags="ui")
        
       
        btn = tk.Button(self.root, text="ACKNOWLEDGE & PROCEED \u2193", font=self.font_btn, bg=self.accent, fg="white", borderwidth=0, command=self.show_setup_screen, cursor="hand2")
        self.canvas.create_window(150, 1600, window=btn, anchor="nw", width=450, height=70, tags="ui")






    def show_setup_screen(self):
        self.clear_elements()
        self.current_page = "setup"
        self.canvas.yview_moveto(0)
        self.canvas.config(scrollregion=(0, 0, 2000, 1000)) 
        
        self.canvas.create_text(150, 100, text="INITIALIZATION SETUP", font=self.font_header, fill=self.text_main, anchor="nw", tags="ui")
        
        self.canvas.create_text(150, 260, text="ENTER USER DESIGNATION (YOUR NAME):", font=self.font_body, fill=self.text_sub, anchor="nw", tags="ui")
        
        frame_user = tk.Frame(self.root, bg=self.box_bg)
        frame_user.place(x=150, y=300, relwidth=0.5, height=70) 
        self.entry_user = tk.Entry(frame_user, font=self.font_body, bg=self.box_bg, fg=self.text_main, borderwidth=0, insertbackground="white")
        self.entry_user.insert(0, "Person A")
        self.entry_user.pack(fill=tk.BOTH, expand=True, padx=25, pady=15)
        
        self.canvas.create_text(150, 420, text="ENTER TARGET DESIGNATION (FRIEND'S NAME):", font=self.font_body, fill=self.text_sub, anchor="nw", tags="ui")
        
        frame_bot = tk.Frame(self.root, bg=self.box_bg)
        frame_bot.place(x=150, y=460, relwidth=0.5, height=70)
        self.entry_bot = tk.Entry(frame_bot, font=self.font_body, bg=self.box_bg, fg=self.text_main, borderwidth=0, insertbackground="white")
        self.entry_bot.insert(0, "Person B")
        self.entry_bot.pack(fill=tk.BOTH, expand=True, padx=25, pady=15)
        
        btn = tk.Button(self.root, text="BOOT INTERFACE \u2192", font=self.font_btn, bg=self.accent, fg="white", borderwidth=0, command=self.start_chat_interface, cursor="hand2")
        btn.place(x=150, y=600, width=350, height=70)



    def start_chat_interface(self):
        user_val = self.entry_user.get().strip()
        bot_val = self.entry_bot.get().strip()
        if user_val: self.user_name = user_val
        if bot_val: self.bot_name = bot_val
        self.show_chat_screen()

    def show_chat_screen(self):
        self.clear_elements()
        self.current_page = "chat"
        self.canvas.yview_moveto(0)
        
        self.canvas.create_text(150, 50, text=f"CONNECTION ESTABLISHED: {self.bot_name}", font=self.font_title, fill=self.text_main, anchor="nw", tags="ui")

        self.chat_area = tk.Text(self.root, wrap=tk.WORD, bg=self.box_bg, fg=self.text_main, font=self.font_body, borderwidth=0, state='disabled', padx=30, pady=30)
        self.chat_area.place(relx=0.1, y=120, relwidth=0.8, relheight=0.65)

        entry_frame = tk.Frame(self.root, bg="#2d3748")
        entry_frame.place(relx=0.1, rely=0.85, relwidth=0.65, height=70)
        self.entry = tk.Entry(entry_frame, bg="#2d3748", fg=self.text_main, font=self.font_body, borderwidth=0, insertbackground="white")
        self.entry.bind("<Return>", self.send_message)
        self.entry.pack(fill=tk.BOTH, expand=True, padx=25, pady=15)

        btn = tk.Button(self.root, text="TRANSMIT", bg=self.accent, fg="white", font=self.font_btn, borderwidth=0, command=self.send_message, cursor="hand2")
        btn.place(relx=0.77, rely=0.85, relwidth=0.13, height=70)
        
        self.display_message(self.bot_name, f"Hi {self.user_name}! It's great to see you.")
        self.entry.focus()



    def display_message(self, sender, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{sender}:\n{message}\n\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def send_message(self, event=None):
        user_text = self.entry.get().strip()
        if not user_text:
            return
        
        self.display_message(self.user_name, user_text)
        self.entry.delete(0, tk.END)

        reply = get_response(user_text)
        self.display_message(self.bot_name, reply)




if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()