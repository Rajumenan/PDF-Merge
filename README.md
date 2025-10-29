# 📄 PDF Merger with Reorder GUI

A **Python-based desktop application** that allows users to easily merge multiple PDF files into one — with the added ability to **reorder files** before merging.  
Built using **Tkinter** for the GUI and **PyPDF2** for PDF manipulation, this tool offers a simple, lightweight, and efficient solution for document management.

---

## 🧭 Project Overview

The **PDF Merger with Reorder GUI** simplifies the process of combining multiple PDF files.  
Users can select multiple files, rearrange their order, and merge them into a single output PDF with just a few clicks.

This project demonstrates practical knowledge in:
- Python GUI programming (Tkinter)
- File handling
- PDF manipulation using PyPDF2

---

## 🎯 Objectives

- Develop a **user-friendly interface** for selecting and managing PDF files  
- Enable users to **reorder** files before merging  
- Efficiently **merge multiple PDFs** into a single output file  
- Provide **error handling** and user notifications for smooth operation  

---

## 🧰 Tools & Technologies

| Category | Technology |
|-----------|-------------|
| **Programming Language** | Python 3.x |
| **Libraries Used** | PyPDF2, Tkinter |
| **Platform** | Cross-platform (Windows, macOS, Linux) |

---

## ⚙️ Functional Description

### ✳️ Key Features
1. **Add PDFs**  
   - Browse and select multiple PDF files to include in the merge list.

2. **Reorder Files**  
   - Move selected PDFs up or down to arrange the desired merging order.

3. **Merge & Save**  
   - Merge all listed PDFs into a single output file and choose where to save it.

4. **Notifications**  
   - Get alerts for successful merges, errors, or missing files using message boxes.

---

## 🪟 GUI Design

The application features a clean and intuitive interface built with **Tkinter**:

- **Listbox** → Displays selected PDF files  
- **Buttons** →  
  - `Add PDFs` – Select and add files  
  - `Move Up` / `Move Down` – Reorder files  
  - `Merge and Save` – Merge and export final PDF  

Provides real-time feedback with message boxes for success or error notifications.

---

## 🧩 Code Structure

| Function | Description |
|-----------|-------------|
| `add_files()` | Opens file dialog to select PDFs and add them to the listbox |
| `move_up()` | Moves selected PDF file up one position |
| `move_down()` | Moves selected PDF file down one position |
| `merge_pdfs()` | Merges all PDFs in listbox order and saves output |
| **Tkinter GUI** | Listbox + Buttons + Messageboxes for interaction |

---

## 🖼️ Screenshots (Suggested)

Include screenshots such as:
- GUI before merging  
- GUI after adding PDF files  
- Merge success message box  

*(Add images in `/screenshots/` folder if available)*

---

## 🌟 Advantages

- Simple and easy-to-use interface  
- Supports reordering of PDFs  
- Provides user feedback and error handling  
- Lightweight and runs on all major platforms  

---

## 🔮 Future Enhancements

- Add **drag-and-drop** file support  
- Include **PDF preview** feature  
- Add **batch renaming** before merging  
- Implement **password protection** for output PDFs  

---

## 🏁 Conclusion

The **PDF Merger with Reorder GUI** project demonstrates solid proficiency in **Python GUI development**, **file handling**, and **PDF processing**.  
It provides a quick and efficient way for users to merge documents in any desired order, enhancing productivity and simplifying document management.

---

## 👨‍💻 Author

- **Name:** Rajumenan B  
- **Date:** 20-08-2025  
- **Project Title:** PDF Merger with Reorder  
- **Institution:** University College of Engineering, Tindivanam  

---

✨ *"Simplify your workflow — merge, reorder, and manage PDFs with ease!"*
