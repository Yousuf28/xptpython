#!/usr/bin/env python.exe
# from tkinter import *
# rows = []
# for i in range(5):
#     cols = []
#     for j in range(4):
#         e = Entry(relief=GROOVE)
#         e.grid(row=i, column=j, sticky=NSEW)
#         e.insert(END, '%d.%d' % (i, j))
#         cols.append(e)
#     rows.append(cols)
#     mainloop()

# import tkinter as tk
# from tkinterdnd2 import DND_FILES, TkinterDnD
# from pandastable import Table
# import pandas as pd

# class CSVViewer(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("CSV Viewer")
#         self.geometry("800x600")

#         # Create a label for instructions
#         self.label = tk.Label(self, text="Drag and drop a CSV file here:")
#         self.label.pack(pady=10)

#         # Create a drop target frame
#         self.drop_target = tk.Frame(self, bg="lightgray", width=400, height=400)
#         self.drop_target.pack(pady=10)

#         # Bind the drop event to handle dropped files
#         self.drop_target.drop_target_register(DND_FILES)
#         self.drop_target.dnd_bind('<<Drop>>', self.load_csv)

#         # Create a PandasTable instance to display the data
#         self.pt = None

#     def load_csv(self, event):
#         file_path = event.data
#         if file_path.endswith('.csv'):
#             try:
#                 df = pd.read_csv(file_path)
#                 self.display_table(df)
#             except Exception as e:
#                 self.label.config(text=f"Error: {str(e)}")

#     def display_table(self, data_frame):
#         if self.pt:
#             self.pt.destroy()
#         self.pt = Table(self, dataframe=data_frame, showtoolbar=True, showstatusbar=True)
#         self.pt.show()
#         self.label.config(text="CSV file loaded successfully!")

# if __name__ == "__main__":
#     app = CSVViewer()
#     app.mainloop()
# import tkinter as tk
# from tkinter import filedialog
# import pandas as pd
# from pandastable import Table

# class CSVViewerApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("CSV Viewer")
#         self.geometry("800x600")

#         # Create a label for instructions
#         self.label = tk.Label(self, text="Upload a CSV file:")
#         self.label.pack(pady=10)

#         # Create an "Upload" button
#         self.upload_button = tk.Button(self, text="Upload CSV", command=self.upload_csv)
#         self.upload_button.pack()

#         # Create a PandasTable instance to display the data
#         self.pt = None

#     def upload_csv(self):
#         file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
#         if file_path:
#             try:
#                 df = pd.read_csv(file_path)
#                 self.display_table(df)
#             except Exception as e:
#                 self.label.config(text=f"Error: {str(e)}")

#     def display_table(self, data_frame):
#         if self.pt:
#             self.pt.destroy()
#         self.pt = Table(self, dataframe=data_frame, showtoolbar=True, showstatusbar=True)
#         self.pt.show()
#         self.label.config(text="CSV file loaded successfully!")

# if __name__ == "__main__":
#     app = CSVViewerApp()
#     app.mainloop()
import pandas as pd
from pandasgui import show
df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]})
show(df)
