import tkinter as tk
from tkinter import messagebox, filedialog
import statistics
import csv


def determine_grade(score, best_score):
    if score >= best_score - 10:
        return 'A'
    elif score >= best_score - 20:
        return 'B'
    elif score >= best_score - 30:
        return 'C'
    elif score >= best_score - 40:
        return 'D'
    else:
        return 'F'


def calculate_and_display():
    try:
        num_students = int(num_students_entry.get())
        scores = list(map(int, grades_entry.get().split(',')))

        if len(scores) != num_students:
            raise ValueError("The number of grades does not match the number of students.")

        best_score = max(scores)
        avg_score = statistics.mean(scores)
        min_score = min(scores)
        max_score = max(scores)
        std_dev = statistics.stdev(scores) if len(scores) > 1 else 0

        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"Best Score: {best_score}\n")
        results_text.insert(tk.END, f"Average: {avg_score:.2f}\n")
        results_text.insert(tk.END, f"Minimum: {min_score}\n")
        results_text.insert(tk.END, f"Maximum: {max_score}\n")
        results_text.insert(tk.END, f"Standard Deviation: {std_dev:.2f}\n\n")

        for i in range(num_students):
            grade = determine_grade(scores[i], best_score)
            results_text.insert(tk.END, f"Student {i + 1}: Score = {scores[i]}, Grade = {grade}\n")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


def add_grades_to_csv():
    scores = grades_entry.get()
    if not scores:
        messagebox.showerror("Error", "No grades to add!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Grades"])
            writer.writerow(scores.split(','))
        messagebox.showinfo("Success", "Grades added to CSV file.")


def delete_grades_from_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Grades"])
        messagebox.showinfo("Success", "Grades deleted from CSV file.")


def clear_inputs():
    num_students_entry.delete(0, tk.END)
    grades_entry.delete(0, tk.END)
    results_text.delete(1.0, tk.END)

root = tk.Tk()
root.title("Charlie's Grade Tracker")

tk.Label(root, text="Number of Students:").grid(row=0, column=0, padx=10, pady=5)
num_students_entry = tk.Entry(root)
num_students_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Grades (comma-separated):").grid(row=1, column=0, padx=10, pady=5)
grades_entry = tk.Entry(root)
grades_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate Grades & Stats", command=calculate_and_display).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="Add Grades to CSV", command=add_grades_to_csv).grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Clear", command=clear_inputs).grid(row=2, column=3, padx=10, pady=5)

tk.Label(root, text="Results:").grid(row=3, column=0, padx=10, pady=5)
results_text = tk.Text(root, height=15, width=60)
results_text.grid(row=4, column=0, columnspan=4, padx=10, pady=5)

root.mainloop()
