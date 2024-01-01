import tkinter as tk

selected_year = None
selected_semester = None
user_classes_list = []  # List to store the classes entered by the user

def select_year(year):
    global selected_year
    selected_year = year
    show_result()

def select_semester(semester):
    global selected_semester
    selected_semester = semester
    show_result()

def show_result():
    result_label.config(text=f"Selected Year {selected_year}, Semester {selected_semester}")
    display_classes()

def display_classes():
    user_classes = classes_entry.get()
    if user_classes:
        user_classes_list.append(user_classes)
        classes_entry.delete(0, 'end')  # Clear the entry field
        result_label.config(text=result_label.cget("text") + f"\nClass Taken: {user_classes}")
        

def end_program():
    app.quit()  # Close the main window and end the program
    #print(f"Year: {selected_year}, Semester: {selected_semester}")
    #print("Classes Taken:")
    #print(user_classes_list)
    #for i, user_class in enumerate(user_classes_list, 1):
        #print(f"{i}. {user_class}")

app = tk.Tk()
app.title("Class Scheduler")

year1_button = tk.Button(app, text="Year 1", command=lambda: select_year(1))
year2_button = tk.Button(app, text="Year 2", command=lambda: select_year(2))
year3_button = tk.Button(app, text="Year 3", command=lambda: select_year(3))
year4_button = tk.Button(app, text="Year 4", command=lambda: select_year(4))

semester1_button = tk.Button(app, text="Semester 1", command=lambda: select_semester(1))
semester2_button = tk.Button(app, text="Semester 2", command=lambda: select_semester(2))

classes_label = tk.Label(app, text="Enter Class Taken:")
classes_entry = tk.Entry(app)
submit_button = tk.Button(app, text="Submit", command=display_classes)
end_button = tk.Button(app, text="End", command=end_program)
result_label = tk.Label(app, text="")

year1_button.pack()
year2_button.pack()
year3_button.pack()
year4_button.pack()
semester1_button.pack()
semester2_button.pack()
classes_label.pack()
classes_entry.pack()
submit_button.pack()
end_button.pack()
result_label.pack()

app.mainloop()

