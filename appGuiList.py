import tkinter as tk
from tkinter import simpledialog, messagebox

class ListApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("400x400")
        self.window.title("List📋")

        self.items = []

        # Entry with simulated placeholder
        self.entry = tk.Entry(self.window, width=30, fg='grey')
        self.entry.insert(0, "Enter item here...")
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(self.window, text="Add Item", command=self.add_item)
        self.add_button.pack(pady=2)

        self.edit_button = tk.Button(self.window, text="Edit Selected", command=self.edit_item)
        self.edit_button.pack(pady=2)

        self.listbox = tk.Listbox(self.window, width=40, height=10)
        self.listbox.pack(pady=5)

    def clear_placeholder(self, event):
        if self.entry.get() == "Enter item here...":
            self.entry.delete(0, tk.END)
            self.entry.config(fg='black')

    def add_placeholder(self, event):
        if self.entry.get().strip() == "":
            self.entry.insert(0, "Enter item here...")
            self.entry.config(fg='grey')

    def add_item(self):
        value = self.entry.get().strip()
        if value and value != "Enter item here...":
            self.items.append(value)
            self.listbox.insert(tk.END, value)
            self.entry.delete(0, tk.END)
            self.add_placeholder(None)
        else:
            messagebox.showinfo("Empty", "Please enter something to add.")

    def edit_item(self):
        try:
            selected_index = self.listbox.curselection()[0]
        except IndexError:
            messagebox.showinfo("No selection", "Please select an item to edit.")


        current_value = self.items[selected_index]
        new_value = simpledialog.askstring("Edit Item", "Modify the item:", initialvalue=current_value)

        if new_value:
            self.items[selected_index] = new_value
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, new_value)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ListApp(root)
    root.mainloop()
