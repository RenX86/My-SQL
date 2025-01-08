import tkinter as tk
import mysql.connector
from tkinter import messagebox

connection = None
cursor = None
current_artitst_id = None

# Create the main application window
root = tk.Tk()
root.title("SQL GUI")  # Set the window title

# Set the window size
root.geometry("600x600") 

username_var = tk.StringVar()
password_var = tk.StringVar()
database_var = tk.StringVar()

def restore_last_values():
    username_var.set(username_var.get())
    password_var.set(password_var.get())
    database_var.set(database_var.get())


border_frame = tk.LabelFrame(root, bd=2, text="Database Information", relief="groove")
border_frame.place(x=100, y=20, width=400, height=110)

# Create a label for "Username" and place it at specific coordinates
username_label = tk.Label(root, text="Username:")
username_label.place(x=170, y=40)  

# Create an entry field for "Username" and place it below the label
username_entry = tk.Entry(root, textvariable=username_var)
username_entry.place(x=240, y=40)  

# Create a label for "Password" and place it
password_label = tk.Label(root, text="Password:")
password_label.place(x=170, y=70)

# Create an entry field for "Password" and place it
password_entry = tk.Entry(root, textvariable=password_var, show="*")
password_entry.place(x=240, y=70) 

database_label = tk.Label(root, text="Database:")
database_label.place(x=170, y=100)

database_entry = tk.Entry(root, textvariable=database_var)
database_entry.place(x=240, y=100)

restore_last_values()

def connect_to_mysql():

    global connection, cursor

    username = username_entry.get()
    password = password_entry.get()
    database = database_entry.get()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database=database  
        )
        cursor = connection.cursor()
        messagebox.showinfo("Connection Successful", "Connected to MySQL Database")
    except mysql.connector.Error as err:
        messagebox.showerror("Connection Error", f"Error: {err}")
        connection, cursor = None, None

def on_close():
    if connection:
        connection.close()
        print("MySQL connection is closed")
    root.destroy()

connect_button = tk.Button(root, text="Connect", command=connect_to_mysql)
connect_button.place(x=400, y=60)

artist_data_frame = tk.LabelFrame(root, bd=2,text="Artist Information", relief="groove")
artist_data_frame.place(x=100, y=130, width=400, height=100)

artist_name = tk.Label(root, text="Artist Name:")
artist_name.place(x=160, y=150)

artist_name_entry = tk.Entry(root)
artist_name_entry.place(x=240, y=150, width=150)

date = tk.Label(root, text="Date(YYYY-MM-DD):")
date.place(x=120, y=180)

date_entry = tk.Entry(root)
date_entry.place(x=240, y=180, width=150)

def add_artist():
    global current_artist_id
    name = artist_name_entry.get().strip()
    date = date_entry.get().strip()

    if not name or not date:
        messagebox.showerror("Input Error", "Artist Name and Date are required.")
        return

    try:
        query = "INSERT INTO artist (Artist_Name, Up_Date) VALUES (%s, %s)"
        cursor.execute(query, (name, date))
        connection.commit()
        current_artist_id = cursor.lastrowid
        messagebox.showinfo("Success", f"Artist '{name}' added with ID {current_artist_id}.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

add_artist_button = tk.Button(root, text="Add Artist", command=add_artist)
add_artist_button.place(x=400, y=170)

def add_work():
    global current_artist_id
    if not current_artist_id:
        messagebox.showerror("Input Error", "Add an artist first.")
        return

    title = work_title_entry.get().strip()
    rating = work_rating_entry.get().strip()
    code = work_code_entry.get().strip()
    source = work_source_entry.get().strip()

    if not title or not rating or not code or not source:
        messagebox.showerror("Input Error", "All fields are required for works.")
        return

    try:
        query = "INSERT INTO works (Artist_ID, Title, Rating, Code, Source) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (current_artist_id, title, float(rating), code, source))
        connection.commit()
        messagebox.showinfo("Success", f"Work '{title}' added for Artist ID {current_artist_id}.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def fetch_artist_and_works():

    if not cursor:
        messagebox.showerror("Connection Error", "No connection to MySQL Database")
        return
    
    query = """
            SELECT artist.Artist_ID, artist.Artist_Name, artist.Up_Date,
                   works.Title, works.Rating, works.Code, works.Source
            FROM artist
            LEFT JOIN works ON artist.Artist_ID = works.Artist_ID
            """
    try:
        cursor.execute(query)
        records = cursor.fetchall()

        display_window = tk.Toplevel(root)
        display_window.title("Records")
        display_window.geometry("1600x600")

        text_area = tk.Text(display_window, wrap=tk.WORD)
        text_area.pack(expand=True, fill=tk.BOTH)

        for record in records:
            text_area.insert(tk.END, f"{record}\n")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

connect_button = tk.Button(root, text="Display Records", command=fetch_artist_and_works)
connect_button.place(x=250, y=500)

border_frame = tk.LabelFrame(root, bd=2, text="Work Information", relief="groove")
border_frame.place(x=100, y=235, width=400, height=150)

work_title = tk.Label(root, text="Work Title:")
work_title.place(x=130, y=260)

work_title_entry = tk.Entry(root)
work_title_entry.place(x=200, y=260, width=280)

work_rating = tk.Label(root, text="Rating (0-10):")
work_rating.place(x=115, y=290)

work_rating_entry = tk.Entry(root)
work_rating_entry.place(x=200, y=290, width=120)

work_code = tk.Label(root, text="Code:")
work_code.place(x=150, y=320)

work_code_entry = tk.Entry(root)
work_code_entry.place(x=200, y=320, width=120)

work_source = tk.Label(root, text="Source:")
work_source.place(x=140, y=350)

work_source_entry = tk.Entry(root)
work_source_entry.place(x=200, y=350, width=120)

add_work_button = tk.Button(root, text="Add Work", command=add_work)
add_work_button.place(x=400, y=300)

root.protocol("WM_DELETE_WINDOW", on_close)
# Run the Tkinter event loop
root.mainloop()
