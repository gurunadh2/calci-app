import tkinter as tk
from tkinter import messagebox, scrolledtext

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Calculator App")
        self.expression = ""  # to keep current expression
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        # Display for current expression/result
        self.display_var = tk.StringVar()
        display = tk.Entry(self.root, textvariable=self.display_var, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify='right')
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Buttons layout
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '%', '+'),
            ('C', '(', ')', '**'),
            ('//', 'History', '=', ''),
        ]

        # Color scheme
        num_color = "#d0e1f9"
        op_color = "#f9d0d0"
        func_color = "#d0f9d6"

        for r, row in enumerate(buttons, 1):
            for c, btn_text in enumerate(row):
                if btn_text == '':
                    continue  # skip empty spots

                btn = tk.Button(self.root, text=btn_text, font=("Arial", 18), relief=tk.RAISED, bd=3,
                                command=lambda x=btn_text: self.on_button_click(x))
                
                # Color code buttons
                if btn_text.isdigit() or btn_text == '.':
                    btn.config(bg=num_color)
                elif btn_text in ['+', '-', '*', '/', '%', '**', '//']:
                    btn.config(bg=op_color)
                else:
                    btn.config(bg=func_color)

                btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

        # History window (hidden by default)
        self.history_window = None

        # Configure grid weights for resizing
        for i in range(4):
            self.root.columnconfigure(i, weight=1)
        for i in range(len(buttons) + 1):
            self.root.rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("")
        elif char == '=':
            self.calculate()
        elif char == 'History':
            self.show_history()
        else:
            # Append character to expression
            self.expression += char
            self.display_var.set(self.expression)

    def calculate(self):
        try:
            # Evaluate the expression safely
            # Allowed names for safety: just math operators
            allowed_chars = "0123456789+-*/%.() "
            if any(c not in allowed_chars and c not in ['*'] for c in self.expression):
                raise ValueError("Invalid characters in expression")

            # Use eval carefully:
            result = eval(self.expression)
            self.display_var.set(str(result))
            self.history.append(f"{self.expression} = {result}")
            self.expression = str(result)  # let user continue calculating
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {e}")
            self.expression = ""
            self.display_var.set("")

    def show_history(self):
        if self.history_window and tk.Toplevel.winfo_exists(self.history_window):
            self.history_window.lift()
            return

        self.history_window = tk.Toplevel(self.root)
        self.history_window.title("Calculation History")
        self.history_window.geometry("300x400")

        txt = scrolledtext.ScrolledText(self.history_window, font=("Arial", 12))
        txt.pack(expand=True, fill='both')
        txt.insert(tk.END, "\n".join(self.history))
        txt.configure(state='disabled')

        btn_clear = tk.Button(self.history_window, text="Clear History", command=self.clear_history)
        btn_clear.pack(pady=5)

    def clear_history(self):
        self.history = []
        if self.history_window:
            self.history_window.destroy()
            self.history_window = None


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
