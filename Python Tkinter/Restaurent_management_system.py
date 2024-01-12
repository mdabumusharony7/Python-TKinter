import tkinter as tk
from tkinter import messagebox

class RestaurantManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")

        # Menu items
        self.menu_items = {
            "Burger": 5.99,
            "Pizza": 8.99,
            "Pasta": 6.99,
            "Salad": 4.99,
            "Soda": 1.99,
        }

        # Order details
        self.order_items = {}
        self.total_price = tk.DoubleVar()

        # Tax and Service Charge variables
        self.tax_rate = tk.DoubleVar(value=0.1)
        self.service_charge = tk.DoubleVar(value=0.05)

        # GUI components
        self.create_menu_frame()
        self.create_order_frame()
        self.create_buttons()
        self.create_calculator_frame()

    def create_menu_frame(self):
        # Existing code remains unchanged

    def create_order_frame(self):
        # Existing code remains unchanged

    def create_buttons(self):
        # Existing code remains unchanged

        btn_reset = tk.Button(btn_frame, text="Reset Order", command=self.reset_order)
        btn_reset.pack(side=tk.LEFT)

        btn_calculator = tk.Button(btn_frame, text="Open Calculator", command=self.open_calculator)
        btn_calculator.pack(side=tk.RIGHT)

    def create_calculator_frame(self):
        calculator_frame = tk.Frame(self.root, padx=10, pady=10)
        calculator_frame.pack(side=tk.BOTTOM, pady=10)

        label_calculator = tk.Label(calculator_frame, text="Calculator", font=("Helvetica", 16, "bold"))
        label_calculator.pack()

        entry_calculator = tk.Entry(calculator_frame)
        entry_calculator.pack(pady=10, fill=tk.X)

        btn_calculate = tk.Button(calculator_frame, text="Calculate", command=lambda: self.calculate(entry_calculator.get()))
        btn_calculate.pack(pady=10)

    def add_to_order(self):
        # Existing code remains unchanged

    def update_order_list(self):
        # Existing code remains unchanged

    def place_order(self):
        # Existing code remains unchanged

    def reset_order(self):
        self.order_items = {}
        self.update_order_list()

    def calculate(self, expression):
        try:
            result = eval(expression)
            messagebox.showinfo("Calculation Result", f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression: {e}")

    def open_calculator(self):
        calculator_window = tk.Toplevel(self.root)
        calculator_window.title("Calculator")

        entry_calculator = tk.Entry(calculator_window)
        entry_calculator.pack(pady=10, fill=tk.X)

        btn_calculate = tk.Button(calculator_window, text="Calculate", command=lambda: self.calculate(entry_calculator.get()))
        btn_calculate.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    root.mainloop()
