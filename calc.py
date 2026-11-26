import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Display screen
        input_frame = tk.Frame(self.root, bg="#1e1e1e", bd=0)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        input_field = tk.Entry(
            input_frame,
            textvariable=self.input_text,
            font=("Segoe UI", 28, "bold"),
            bg="#1e1e1e",
            fg="#ffffff",
            bd=0,
            justify=tk.RIGHT,
            state="readonly",
            readonlybackground="#1e1e1e"
        )
        input_field.pack(fill=tk.BOTH, expand=True, padx=15, pady=20)

        # Button grid
        btns_frame = tk.Frame(self.root, bg="#1e1e1e")
        btns_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        buttons = [
            ('C', 0, 0, "#a5a5a5", "#000000"), ('(', 0, 1, "#a5a5a5", "#000000"),
            (')', 0, 2, "#a5a5a5", "#000000"), ('/', 0, 3, "#ff9f0a", "#ffffff"),
            ('7', 1, 0, "#333333", "#ffffff"), ('8', 1, 1, "#333333", "#ffffff"),
            ('9', 1, 2, "#333333", "#ffffff"), ('*', 1, 3, "#ff9f0a", "#ffffff"),
            ('4', 2, 0, "#333333", "#ffffff"), ('5', 2, 1, "#333333", "#ffffff"),
            ('6', 2, 2, "#333333", "#ffffff"), ('-', 2, 3, "#ff9f0a", "#ffffff"),
            ('1', 3, 0, "#333333", "#ffffff"), ('2', 3, 1, "#333333", "#ffffff"),
            ('3', 3, 2, "#333333", "#ffffff"), ('+', 3, 3, "#ff9f0a", "#ffffff"),
            ('0', 4, 0, "#333333", "#ffffff"), ('.', 4, 1, "#333333", "#ffffff"),
            ('⌫', 4, 2, "#333333", "#ffffff"), ('=', 4, 3, "#ff9f0a", "#ffffff"),
        ]

        for (text, row, col, bg_color, fg_color) in buttons:
            btn = tk.Button(
                btns_frame,
                text=text,
                font=("Segoe UI", 16, "bold"),
                bg=bg_color,
                fg=fg_color,
                activebackground="#666666",
                activeforeground="#ffffff",
                bd=0,
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

        # Configure uniform grid resizing
        for i in range(5):
            btns_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btns_frame.columnconfigure(j, weight=1)

        # Enable keyboard support
        self.root.bind("<Key>", self.on_key_press)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '⌫':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                # Evaluate mathematical expression safely
                result = str(eval(self.expression, {"__builtins__": None}, {}))
                self.expression = result
            except ZeroDivisionError:
                self.expression = ""
                self.input_text.set("Cannot divide by 0")
                return
            except Exception:
                self.expression = ""
                self.input_text.set("Error")
                return
        else:
            self.expression += str(char)

        self.input_text.set(self.expression)

    def on_key_press(self, event):
        key = event.char
        if key in '0123456789+-*/().':
            self.on_button_click(key)
        elif event.keysym == 'Return':
            self.on_button_click('=')
        elif event.keysym == 'BackSpace':
            self.on_button_click('⌫')
        elif event.keysym == 'Escape':
            self.on_button_click('C')

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()