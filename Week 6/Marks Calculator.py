import tkinter as tk

def calculate_result():
    try:
        m1 = float(entry1.get())
        m2 = float(entry2.get())
        m3 = float(entry3.get())

        if not all(0 <= m <= 100 for m in [m1, m2, m3]):
            result_label.config(text="Marks must be between 0 and 100")
            return

        avg = (m1 + m2 + m3) / 3
        status = "Passed" if avg >= 50 else "Failed"

        result_label.config(text=f"Average: {avg:.2f} - {status}")
    except ValueError:
        result_label.config(text="Enter valid numbers")

# Main window
root = tk.Tk()
root.title("Student Result Calculator")
root.geometry("280x200")

tk.Label(root, text="Enter Marks:").pack(pady=5)

entry1 = tk.Entry(root, width=10)
entry1.pack(pady=2)

entry2 = tk.Entry(root, width=10)
entry2.pack(pady=2)

entry3 = tk.Entry(root, width=10)
entry3.pack(pady=2)

tk.Button(root, text="Calculate", command=calculate_result).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
