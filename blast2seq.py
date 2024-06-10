#GUI for blast2sequences; created by ChatGPT 20230914
import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def run_blastn():
    query_text = query_textbox.get("1.0", "end-1c")
    subject_text = subject_textbox.get("1.0", "end-1c")

    if query_file_path.get():
        query_file = query_file_path.get()
    else:
        # Save query to a temporary file
        with open("temp_query.fasta", "w") as query_file:
            query_file.write(query_text)
        query_file = "temp_query.fasta"

    if subject_file_path.get():
        subject_file = subject_file_path.get()
    else:
        # Save subject to a temporary file
        with open("temp_subject.fasta", "w") as subject_file:
            subject_file.write(subject_text)
        subject_file = "temp_subject.fasta"

    command = [
        "blastn",
        "-query", query_file,
        "-subject", subject_file,
    ]

    # Include -task option if the checkbox is selected
    if task_var.get():
        command.extend(["-task", "blastn-short"])

    try:
        # Run the blastn command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

        # Display the results in the text box
        result_text.delete(1.0, tk.END)  # Clear previous results
        result_text.insert(tk.END, result.stdout)
    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e.stderr}")
    finally:
        # Remove temporary files after the blast search
        if not query_file_path.get():
            os.remove("temp_query.fasta")
        if not subject_file_path.get():
            os.remove("temp_subject.fasta")

def browse_file(entry_widget):
    file_path = filedialog.askopenfilename()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, file_path)

app = tk.Tk()
app.title("BLASTN GUI")

# Query sequence section
query_label = tk.Label(app, text="Query Sequence:")
query_label.pack()

query_textbox = tk.Text(app, wrap=tk.WORD, width=100, height=10)
query_textbox.pack()

#query_paste_button = tk.Button(app, text="Paste Query", command=lambda: query_textbox.insert("end", app.clipboard_get()))
#query_paste_button.pack()

query_file_path = tk.StringVar()
query_file_entry = tk.Entry(app, textvariable=query_file_path, width=100)
query_file_entry.pack()

query_browse_button = tk.Button(app, text="Browse Query File", command=lambda: browse_file(query_file_entry))
query_browse_button.pack()

# Subject sequence section
subject_label = tk.Label(app, text="Subject Sequence:")
subject_label.pack()

subject_textbox = tk.Text(app, wrap=tk.WORD, width=100, height=10)
subject_textbox.pack()

#subject_paste_button = tk.Button(app, text="Paste Subject", command=lambda: subject_textbox.insert("end", app.clipboard_get()))
#subject_paste_button.pack()

subject_file_path = tk.StringVar()
subject_file_entry = tk.Entry(app, textvariable=subject_file_path, width=100)
subject_file_entry.pack()

subject_browse_button = tk.Button(app, text="Browse Subject File", command=lambda: browse_file(subject_file_entry))
subject_browse_button.pack()

# Checkbox for the -task option
task_var = tk.BooleanVar()
task_checkbox = tk.Checkbutton(app, text="Use blastn-short task", variable=task_var)
task_checkbox.pack()

# Run button and result display
run_button = tk.Button(app, text="Run BLASTN", command=run_blastn)
run_button.pack()

result_label = tk.Label(app, text="BLASTN Results:")
result_label.pack()

# Add a vertical scrollbar
scrollbar = tk.Scrollbar(app)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text = tk.Text(app, wrap=tk.WORD, width=100, height=60, yscrollcommand=scrollbar.set)
result_text.pack()

# Configure the scrollbar to control the result_text widget
scrollbar.config(command=result_text.yview)

app.mainloop()
