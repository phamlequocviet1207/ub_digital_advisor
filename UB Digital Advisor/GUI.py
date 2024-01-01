import tkinter as tk
from function import final

def display_class_list(final):
    class_list_window = tk.Tk()
    class_list_window.title("Class List")

    label = tk.Label(class_list_window, text="Classes to Take:")
    label.pack()

    for i, class_name in enumerate(final, 1):
        class_label = tk.Label(class_list_window, text=f"{i}. {class_name}")
        class_label.pack()

    class_list_window.mainloop()

if __name__ == "__main__":
    # Sample list of classes to be displayed
    sfinal = ["Class A", "Class B", "Class C", "Class D"]

    # Call the function to display the class list
    display_class_list(final)
