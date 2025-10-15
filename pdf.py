import PyPDF2
from tkinter import Tk, filedialog, Listbox, Button, END, SINGLE, messagebox

def add_files():
    files = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF files", "*.pdf")]
    )
    for f in files:
        listbox.insert(END, f)

def move_up():
    selected = listbox.curselection()
    if not selected:
        return
    index = selected[0]
    if index == 0:
        return
    text = listbox.get(index)
    listbox.delete(index)
    listbox.insert(index - 1, text)
    listbox.selection_set(index - 1)

def move_down():
    selected = listbox.curselection()
    if not selected:
        return
    index = selected[0]
    if index == listbox.size() - 1:
        return
    text = listbox.get(index)
    listbox.delete(index)
    listbox.insert(index + 1, text)
    listbox.selection_set(index + 1)

def merge_pdfs():
    if listbox.size() == 0:
        messagebox.showwarning("No Files", "Please add PDF files before merging.")
        return
    
    merger = PyPDF2.PdfMerger()
    for i in range(listbox.size()):
        merger.append(listbox.get(i))

    output_file = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save merged PDF as"
    )
    if output_file:
        merger.write(output_file)
        merger.close()
        messagebox.showinfo("Success", f"Merged PDF saved successfully!\n\nFile: {output_file}")
        listbox.delete(0, END)  # ✅ Clear listbox after saving

# GUI
root = Tk()
root.title("PDF Merger with Reorder")

listbox = Listbox(root, selectmode=SINGLE, width=80)
listbox.pack(pady=10)

Button(root, text="Add PDFs", command=add_files).pack(pady=5)
Button(root, text="Move Up", command=move_up).pack(pady=5)
Button(root, text="Move Down", command=move_down).pack(pady=5)
Button(root, text="Merge and Save", command=merge_pdfs).pack(pady=10)

root.mainloop()
