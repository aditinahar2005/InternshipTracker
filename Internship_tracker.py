import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def save_to_csv(data):
    # Absolute path to the CSV file
    filename = r'C:\Users\aditi\InternTracking\Internship Tracker.csv'
    print(f"Saving file to: {filename}")  # Confirm the file path

    # Check if the file exists and read it if it does
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        print("CSV file found. Reading existing data.")
    else:
        # Create a new DataFrame with column headers
        df = pd.DataFrame(columns=["Company", "Position", "Date Applied", "Term", "Status"])
        print("CSV file not found. Creating a new file.")

    # Debug: Print DataFrame before appending
    print("DataFrame before appending:")
    print(df)

    # Convert the input data to a DataFrame
    new_data_df = pd.DataFrame([data])

    # Append the new data
    df = pd.concat([df, new_data_df], ignore_index=True)

    # Debug: Print DataFrame after appending
    print("DataFrame after appending:")
    print(df)
    
    # Save the DataFrame to CSV
    df.to_csv(filename, index=False)
    print("File saved successfully!")  # Confirm that the file has been saved

def submit_data(action):
    company = company_var.get()
    position = position_var.get()
    term = term_var.get()
    date_applied = date_applied_var.get()
    status = status_var.get()

    if company and position and term and date_applied and status:
        data = {"Company": company, "Position": position, "Term": term, "Date Applied": date_applied, "Status": status}
        print("Data collected:")
        print(data)  # Debug: Print the data to be saved
        save_to_csv(data)
        messagebox.showinfo("Success", "Data added successfully!")
        if action == "save_and_close":
            root.quit()  # Close the application if "Save and Close" was selected
        elif action == "save_and_add":
            clear_fields()  # Clear the fields for new input if "Save and Add Another" was selected
    else:
        messagebox.showerror("Error", "All fields are required!")

def clear_fields():
    company_var.set("")
    position_var.set("")
    term_var.set("")
    date_applied_var.set("")
    status_var.set("")

def create_form():
    global company_var, position_var, term_var, date_applied_var, status_var, root

    root = tk.Tk()
    root.title("Add Internship Application")
    
    # Set background color of the window
    root.configure(bg='skyblue')

    # Define variables for user input
    company_var = tk.StringVar()
    position_var = tk.StringVar()
    term_var = tk.StringVar()
    date_applied_var = tk.StringVar()
    status_var = tk.StringVar()
    
    # Create a frame for the form with sky blue background
    frame = ttk.Frame(root, padding="10", style='TFrame')
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    # Create form fields with color customization
    fields = ["Company", "Position", "Term", "Date Applied", "Status"]
    for index, field in enumerate(fields):
        label = ttk.Label(frame, text=field + ":", font=('Helvetica', 10, 'bold'), background='skyblue', foreground='black')
        label.grid(row=index, column=0, sticky=tk.W, pady=2)
        entry = ttk.Entry(frame, textvariable=eval(field.lower().replace(" ", "_") + "_var"))
        entry.grid(row=index, column=1, sticky=(tk.W, tk.E), pady=2)

    # Create buttons with color customization
    button_frame = ttk.Frame(root, padding="10", style='TFrame')
    button_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
    
    save_and_add_button = ttk.Button(button_frame, text="Save and Add Another", command=lambda: submit_data("save_and_add"), style='TButton')
    save_and_add_button.grid(row=0, column=0, padx=5)
    
    save_and_close_button = ttk.Button(button_frame, text="Save and Close", command=lambda: submit_data("save_and_close"), style='TButton')
    save_and_close_button.grid(row=0, column=1, padx=5)
    
    cancel_button = ttk.Button(button_frame, text="Cancel", command=root.quit, style='TButton')
    cancel_button.grid(row=0, column=2, padx=5)

    # Define styles for frame and buttons
    style = ttk.Style()
    style.configure('TFrame', background='skyblue')
    style.configure('TButton', background='lightgreen', foreground='black')

    root.mainloop()

if __name__ == '__main__':
    create_form()
