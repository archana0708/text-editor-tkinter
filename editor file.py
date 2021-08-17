import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog
from tkinter.ttk import *
import os

main_application = tk.Tk()
main_application.geometry('800x500')
main_application.title('My Text Editor')
main_application.iconbitmap('icons/text_editor_main_icon (1).ico')
# ********************************* MAIN MENU *********************************


main_menu = tk.Menu()
# ************** All icons OF MENU BAR***************
# file icons
new_icon = tk.PhotoImage(file='icons/new_icon.png')
open_f_icon = tk.PhotoImage(file='icons/open.png')
save_icon = tk.PhotoImage(file='icons/save_icon.png')
save_as_icon = tk.PhotoImage(file='icons/save_as_icon.png')
exit_icon = tk.PhotoImage(file='icons/exit_icon.png')

# edit icons
cut_icon = tk.PhotoImage(file='icons/cut.png')
copy_icon = tk.PhotoImage(file='icons/copy_icon.png')
paste_icon = tk.PhotoImage(file='icons/paste_icon.png')
find_icon = tk.PhotoImage(file='icons/find_icon.png')
clearAll_icon = tk.PhotoImage(file='icons/clear_all_icon.png')

# view icons
toolbar_icon = tk.PhotoImage(file='icons/toolbar.png')
statusbar_icon = tk.PhotoImage(file='icons/statusbar.png')

# colour theme icons
light_theme = tk.PhotoImage(file='icons/light.png')
dark_theme = tk.PhotoImage(file='icons/dark.png')

# ************************* MENU BAR ************************


file1 = tk.Menu(main_menu, tearoff=False)
edit = tk.Menu(main_menu, tearoff=False)
view = tk.Menu(main_menu, tearoff=False)
colour_theme = tk.Menu(main_menu, tearoff=False)
theme_choice = tk.StringVar()

# cascade
main_menu.add_cascade(label='File', menu=file1)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Colour theme', menu=colour_theme)

# ------------------------------- END MAIN MENU -------------------------------


# ********************************* TOOL BAR *********************************
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)
# size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=30, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(0, 81, 2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

# bold button
bold_icon = tk.PhotoImage(file='icons/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=3, padx=5)

# italic button
italic_icon = tk.PhotoImage(file='icons/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=4, padx=5)

# underline
underline_icon = tk.PhotoImage(file='icons/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=5, padx=5)

# font color
fontcolour_icon = tk.PhotoImage(file='icons/fontcolour.png')
fontcolour_btn = ttk.Button(tool_bar, image=fontcolour_icon)
fontcolour_btn.grid(row=0, column=6, padx=5)

# alignment
#  left
left_align_icon = tk.PhotoImage(file='icons/leftalign.png')
left_align_btn = ttk.Button(tool_bar, image=left_align_icon)
left_align_btn.grid(row=0, column=7, padx=5)
# center
center_icon = tk.PhotoImage(file='icons/center.png')
center_btn = ttk.Button(tool_bar, image=center_icon)
center_btn.grid(row=0, column=8, padx=5)
# right
right_icon = tk.PhotoImage(file='icons/right.png')
right_btn = ttk.Button(tool_bar, image=right_icon)
right_btn.grid(row=0, column=9, padx=5)
# ------------------------------- END TOOL BAR -------------------------------

# ********************************* TEXT EDITOR *********************************

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)
# config is used to access an object's attributes after its initialisation.
# The relief style of a widget refers to certain simulated 3-D effects around the outside of the widget.
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# ********************** FUNCTIONALITY ********************

# FONT SIZE AND FONT FAMILY FUNCTIONALITY
current_font_family = 'Arial'
current_font_size = 16


def change_font(main_application):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_fontsize(main_application):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)


######## buttons functionality #########
# bold functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    else:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


bold_btn.configure(command=change_bold)


# italic functionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    else:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


italic_btn.configure(command=change_italic)


# underline
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    else:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


underline_btn.configure(command=change_underline)


#  colour editor
def colour_editor():
    colour_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=colour_var[1])


fontcolour_btn.configure(command=colour_editor)


# ----- ALIGN -----
# LEFT ALIGN
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')


left_align_btn.configure(command=align_left)


# RIGHT ALIGN
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')


right_btn.configure(command=align_right)


# CENTRE ALIGN
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')


center_btn.configure(command=align_center)

# --------------------- END FUNCTIONALITY  ----------------

text_editor.configure(font=['Arial', 12])
# ------------------------------- END TEXT EDITOR -------------------------------


# ********************************* STATUS BAR *********************************
status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False


def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters:{characters}  Words:{words}')
        text_editor.edit_modified(False)


text_editor.bind('<<Modified>>', changed)

# ------------------------------- END STATUS BAR -------------------------------

# ********************************* MAIN MENU FUNCTIONALITY *********************************
#  ****** FILE MENU functionality ******
url = ''


#  -- NEW --
def new_file(event=None):
    global url
    text_editor.delete(1.0, tk.END)


file1.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)


# ---- OPEN ----
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='select file',
                                     filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except:
        return
    main_application.title(os.path.basename(url))


file1.add_command(label='Open', image=open_f_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)

file1.add_separator()


# ---- save  ------

def save_file(event=None):
    global url




file1.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S',command=save_file)
file1.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file1.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q')

# edit menu commands
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl + X')
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl + C')
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl + V')
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl + F')
edit.add_command(label='Clear All', image=clearAll_icon, compound=tk.LEFT, accelerator='Ctrl +Alt+ X')

# view menu commands
view.add_checkbutton(label='Tool Bar', image=toolbar_icon, compound=tk.LEFT)
view.add_checkbutton(label='Status Bar', image=statusbar_icon, compound=tk.LEFT)

# colour theme menu commands
colour_theme.add_radiobutton(label='Light Theme', image=light_theme, variable=theme_choice, compound=tk.LEFT)
colour_theme.add_radiobutton(label='Dark Theme', image=dark_theme, variable=theme_choice, compound=tk.LEFT)

# ------------------------------- END MAIN MENU FUNCTIONALITY -------------------------------


main_application.config(menu=main_menu)
main_application.mainloop()
