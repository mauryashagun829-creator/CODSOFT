"""
To-Do List Application (GUI version)
Built with Tkinter (Python's built-in GUI library).
Tasks are stored in memory only - they reset when you close the app.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("420x520")
        self.root.minsize(380, 420)
        self.root.configure(bg="#f4f6f8")

        self.tasks = []  # list of dicts: {"title": str, "done": bool}

        self._build_ui()

    # ---------- UI SETUP ----------
    def _build_ui(self):
        # Title
        title_label = tk.Label(
            self.root, text="My To-Do List",
            font=("Segoe UI", 18, "bold"),
            bg="#f4f6f8", fg="#222"
        )
        title_label.pack(pady=(15, 5))

        # Entry + Add button
        entry_frame = tk.Frame(self.root, bg="#f4f6f8")
        entry_frame.pack(pady=10, padx=15, fill="x")

        self.task_entry = tk.Entry(
            entry_frame, font=("Segoe UI", 12),
            relief="solid", bd=1
        )
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 8), ipady=4)
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        add_btn = tk.Button(
            entry_frame, text="Add", command=self.add_task,
            bg="#4CAF50", fg="white", font=("Segoe UI", 10, "bold"),
            relief="flat", padx=12, pady=4, cursor="hand2"
        )
        add_btn.pack(side="right")

        # Task list
        list_frame = tk.Frame(self.root, bg="#f4f6f8")
        list_frame.pack(pady=5, padx=15, fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.task_listbox = tk.Listbox(
            list_frame, font=("Segoe UI", 12),
            selectmode="single", activestyle="none",
            yscrollcommand=scrollbar.set,
            relief="solid", bd=1
        )
        self.task_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.task_listbox.yview)

        # Action buttons
        btn_frame = tk.Frame(self.root, bg="#f4f6f8")
        btn_frame.pack(pady=12, padx=15, fill="x")

        buttons = [
            ("Mark Done", "#2196F3", self.mark_done),
            ("Edit", "#FF9800", self.edit_task),
            ("Delete", "#F44336", self.delete_task),
            ("Clear All", "#757575", self.clear_all),
        ]

        for text, color, command in buttons:
            b = tk.Button(
                btn_frame, text=text, command=command,
                bg=color, fg="white", font=("Segoe UI", 10, "bold"),
                relief="flat", padx=8, pady=6, cursor="hand2"
            )
            b.pack(side="left", expand=True, fill="x", padx=4)

        # Status bar
        self.status_label = tk.Label(
            self.root, text="0 tasks", font=("Segoe UI", 9),
            bg="#f4f6f8", fg="#666"
        )
        self.status_label.pack(pady=(0, 10))

    # ---------- LOGIC ----------
    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            prefix = "[✓] " if task["done"] else "[ ] "
            self.task_listbox.insert(tk.END, prefix + task["title"])
            if task["done"]:
                index = self.task_listbox.size() - 1
                self.task_listbox.itemconfig(index, fg="#888888")

        done_count = sum(1 for t in self.tasks if t["done"])
        self.status_label.config(
            text=f"{len(self.tasks)} task(s) — {done_count} completed"
        )

    def get_selected_index(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showinfo("No selection", "Please select a task first.")
            return None
        return selection[0]

    def add_task(self):
        title = self.task_entry.get().strip()
        if not title:
            messagebox.showwarning("Empty task", "Please enter a task description.")
            return
        self.tasks.append({"title": title, "done": False})
        self.task_entry.delete(0, tk.END)
        self.refresh_list()

    def mark_done(self):
        index = self.get_selected_index()
        if index is not None:
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.refresh_list()

    def edit_task(self):
        index = self.get_selected_index()
        if index is not None:
            current_title = self.tasks[index]["title"]
            new_title = simpledialog.askstring(
                "Edit Task", "Update task description:",
                initialvalue=current_title
            )
            if new_title and new_title.strip():
                self.tasks[index]["title"] = new_title.strip()
                self.refresh_list()

    def delete_task(self):
        index = self.get_selected_index()
        if index is not None:
            title = self.tasks[index]["title"]
            confirm = messagebox.askyesno("Delete Task", f'Delete "{title}"?')
            if confirm:
                self.tasks.pop(index)
                self.refresh_list()

    def clear_all(self):
        if not self.tasks:
            return
        confirm = messagebox.askyesno("Clear All", "Delete all tasks?")
        if confirm:
            self.tasks.clear()
            self.refresh_list()


def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
