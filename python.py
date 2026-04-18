import csv
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from tkinter import messagebox, ttk


SUBJECTS = [
]

CLASSES = [f"{number}반" for number in range(1, 11)]
DATA_FILE = Path(__file__).resolve().parent / "class_progress_data.csv"


class ProgressApp:
        self.selected_subject = tk.StringVar(value=SUBJECTS[0])
        self.page_input = tk.StringVar()

        self._ensure_data_file()
        self._build_ui()
        self._load_saved_data()

    def _build_ui(self) -> None:
        title_label = tk.Label(
        )
        self.result_label.pack(pady=10)

        table_frame = tk.LabelFrame(
            self.root,
            text="저장된 진도",
            font=("Malgun Gothic", 11, "bold"),
            padx=10,
            pady=10,
        )
        table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        columns = ("class_name", "subject_name", "page")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)
        self.tree.heading("class_name", text="반")
        self.tree.heading("subject_name", text="과목")
        self.tree.heading("page", text="페이지")
        self.tree.column("class_name", width=100, anchor="center")
        self.tree.column("subject_name", width=140, anchor="center")
        self.tree.column("page", width=100, anchor="center")
        self.tree.pack(fill="both", expand=True)

    def _ensure_data_file(self) -> None:
        if DATA_FILE.exists():
            return

        with DATA_FILE.open("w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(["반", "과목", "페이지"])

    def _save_data(self, class_name: str, subject_name: str, page: str) -> None:
        with DATA_FILE.open("a", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow([class_name, subject_name, page])

    def _load_saved_data(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)

        with DATA_FILE.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.tree.insert("", "end", values=(row["반"], row["과목"], row["페이지"]))

    def show_result(self) -> None:
        page = self.page_input.get().strip()

            f"{self.selected_class.get()} / {self.selected_subject.get()} / "
            f"{page}페이지"
        )
        self._save_data(self.selected_class.get(), self.selected_subject.get(), page)
        self._load_saved_data()
        self.result_label.config(text=result_text)
        messagebox.showinfo("입력 완료", f"입력한 진도: {result_text}")
        self.page_input.set("")


def main() -> None:
