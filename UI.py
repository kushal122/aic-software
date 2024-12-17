from owlready2 import get_ontology
from tkinter import Tk, Label, Button, Listbox, Scrollbar, VERTICAL, RIGHT, Y, Frame, TOP, X, LEFT, BOTH
from tkinter import ttk

# Load the ontology
ontology_file = "EnglishLiteratureOntology.owl"  # RDF/XML format
ontology = get_ontology(ontology_file).load()

# Global variable to track the selected category
selected_category = None

# Function to fetch top-level classes
def fetch_classes():
    global selected_category
    selected_category = "classes"  # Set the category to classes
    listbox.delete(0, "end")  # Clear the listbox
    for cls in ontology.classes():
        if "Thing" in [str(parent.name) for parent in cls.is_a]:
            listbox.insert("end", f"Class: {cls.name}")

# Function to fetch subclasses only
def fetch_subclasses():
    global selected_category
    selected_category = "subclasses"  # Set the category to subclasses
    listbox.delete(0, "end")  # Clear the listbox
    for cls in ontology.classes():
        if "Thing" not in [str(parent.name) for parent in cls.is_a]:
            listbox.insert("end", f"Subclass: {cls.name}")

# Function to fetch individuals
def fetch_individuals():
    global selected_category
    selected_category = "individuals"  # Set the category to individuals
    listbox.delete(0, "end")  # Clear the listbox
    for individual in ontology.individuals():
        listbox.insert("end", f"Individual: {individual.name}")

# Function to fetch object properties
def fetch_object_properties():
    global selected_category
    selected_category = "object_properties"  # Set the category to object properties
    listbox.delete(0, "end")  # Clear the listbox
    for prop in ontology.object_properties():
        listbox.insert("end", f"Object Property: {prop.name}")

# Function to fetch data properties
def fetch_data_properties():
    global selected_category
    selected_category = "data_properties"  # Set the category to data properties
    listbox.delete(0, "end")  # Clear the listbox
    for prop in ontology.data_properties():
        listbox.insert("end", f"Data Property: {prop.name}")

# Build the enhanced UI
root = Tk()
root.title("English Literature Ontology Viewer")
root.geometry("850x600")
root.configure(bg="#404040")  # Dark grey background for better readability

# Header Label
header = Label(root, text="English Literature Ontology Viewer", font=("Helvetica", 24, "bold"), fg="white", bg="#333333", pady=20)
header.pack(fill=X)

# Frame for buttons
button_frame = Frame(root, bg="#555555", pady=15)
button_frame.pack(fill=X, padx=10)

# Styled Buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 14), padding=6, background="#4CAF50", foreground="black")

class_button = ttk.Button(button_frame, text="Show Classes", style="TButton", command=fetch_classes)
class_button.pack(side=LEFT, padx=10)

subclass_button = ttk.Button(button_frame, text="Show Subclasses", style="TButton", command=fetch_subclasses)
subclass_button.pack(side=LEFT, padx=10)

object_prop_button = ttk.Button(button_frame, text="Show Object Properties", style="TButton", command=fetch_object_properties)
object_prop_button.pack(side=LEFT, padx=10)

data_prop_button = ttk.Button(button_frame, text="Show Data Properties", style="TButton", command=fetch_data_properties)
data_prop_button.pack(side=LEFT, padx=10)

# Frame for listbox
listbox_frame = Frame(root, bg="#666666")
listbox_frame.pack(fill=BOTH, expand=True, padx=15, pady=10)

# Scrollbar and Listbox
scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(listbox_frame, yscrollcommand=scrollbar.set, font=("Courier New", 14), bg="#777777", fg="white", height=15, selectbackground="#FFC107", selectforeground="black", borderwidth=2, relief="solid")
listbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Result Label for showing selected individual's properties
result_label = Label(root, text="", font=("Arial", 14), bg="#505050", fg="white", anchor="w", justify="left", padx=10)
result_label.pack(fill=BOTH, padx=15, pady=10)

# Footer Label
footer = Label(root, text="Ontology Viewer", font=("Arial", 10), bg="#333333", fg="white", pady=10)
footer.pack(fill=X)

root.mainloop()