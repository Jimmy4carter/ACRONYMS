# Developer: Jimmy Carter
# Contact: jimmy4carter@gmail.com
# Phone: +2348038660259
# GitHub: https://github.com/Jimmy4carter
 
import tkinter as tk

def generate_acronym():
    phrase = entry.get()
    acronym_style = style_var.get()

    if not phrase.strip():
        result_label.config(text="Please enter a valid phrase.")
        return
    
    words = phrase.split()
    acronym = ""
    
    for word in words:
        acronym += word[0].upper()
    
    if acronym_style == 'Camel Case':
        acronym = acronym[0].upper() + acronym[1:].lower()
    elif acronym_style == 'Custom Separator':
        separator = separator_entry.get()
        acronym = separator.join(acronym)
    
    result_label.config(text=f"Generated Acronym: {acronym}")
    display_stats(phrase, acronym)

def display_stats(phrase, acronym):
    words_count = len(phrase.split())
    phrase_length = len(phrase)
    acronym_length = len(acronym)
    
    stats = f"Original Phrase Length: {phrase_length} characters\nNumber of Words: {words_count}\nAcronym Length: {acronym_length} characters"
    stats_label.config(text=stats)

# Create the main window
root = tk.Tk()
root.title("Acronym Generator")

# Create input label and entry
input_label = tk.Label(root, text="Enter a phrase:")
input_label.pack()
entry = tk.Entry(root)
entry.pack()

# Acronym style selection
style_label = tk.Label(root, text="Choose acronym style:")
style_label.pack()

style_var = tk.StringVar(root)
style_var.set("Traditional")

style_option = tk.OptionMenu(root, style_var, "Traditional", "Camel Case", "Custom Separator")
style_option.pack()

separator_entry = tk.Entry(root)
separator_entry.pack()
separator_entry.config(state=tk.DISABLED)

def toggle_separator_entry(*args):
    if style_var.get() == "Custom Separator":
        separator_entry.config(state=tk.NORMAL)
    else:
        separator_entry.config(state=tk.DISABLED)

style_var.trace("w", toggle_separator_entry)

# Generate button
generate_button = tk.Button(root, text="Generate Acronym", command=generate_acronym)
generate_button.pack()

# Display result
result_label = tk.Label(root, text="")
result_label.pack()

# Display stats
stats_label = tk.Label(root, text="")
stats_label.pack()

root.mainloop()
