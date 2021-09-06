from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import chipers
import tools


class Crypthon:

    def __init__(self, root):

        root.title('Crypthon')

        self.mainframe = ttk.Frame(root, padding='3 3 12 12')
        self.mainframe.grid(column=0, row=0)

        self.draw_input_frame()
        self.draw_key_frame()
        self.draw_chiper_frame()
        self.draw_task_frame()
        self.draw_action_frame()
        self.draw_output_frame()

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=4, pady=4)

    def draw_input_frame(self):

        self.input_frame = ttk.Labelframe(self.mainframe, text='Input')
        self.input_frame.grid(row=5, column=10)

        self.input_buttons_frame = ttk.Frame(self.input_frame)
        self.input_buttons_frame.grid(row=5, column=10, sticky='we')

        self.open_file_button = ttk.Button(
            self.input_buttons_frame, text="Open file...", command=self.open_file)
        self.open_file_button.grid(row=5, column=10, sticky='w')

        self.clear_input_button = ttk.Button(
            self.input_buttons_frame, text="Clear input", command=self.update_input)
        self.clear_input_button.grid(row=5, column=20, sticky='w')

        self.input_text = Text(self.input_frame, height=5, width=64)
        self.input_text.grid(row=10, column=10, sticky='we')

        for child in self.input_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def open_file(self):
        self.open_filename = filedialog.askopenfile()

        self.update_input(content=self.open_filename.read())

    def draw_key_frame(self):

        self.key_frame = ttk.Labelframe(self.mainframe, text='Key')
        self.key_frame.grid(row=7, column=10)

        self.key_text = Text(self.key_frame, height=2, width=64)
        self.key_text.grid(row=10, column=10, sticky='we')

        for child in self.key_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def draw_chiper_frame(self):

        self.chiper_frame = ttk.Labelframe(self.mainframe, text='Cipher')
        self.chiper_frame.grid(row=10, column=10)

        self.chiper_var = StringVar()
        self.chiper_var.set('vigenere')

        self.vigenere_radio = ttk.Radiobutton(
            self.chiper_frame, text='Vigenere', variable=self.chiper_var, value='vigenere')
        self.full_vigenere_radio = ttk.Radiobutton(
            self.chiper_frame, text='Full Vigenere', variable=self.chiper_var, value='full_vigenere')
        self.autokey_vigenere_radio = ttk.Radiobutton(
            self.chiper_frame, text='Auto-key Vigenere', variable=self.chiper_var, value='autokey_vigenere')
        self.extended_vigenere_radio = ttk.Radiobutton(
            self.chiper_frame, text='Extended Vigenere', variable=self.chiper_var, value='extended_vigenere')
        self.playfair_radio = ttk.Radiobutton(
            self.chiper_frame, text='Playfair', variable=self.chiper_var, value='playfair')
        self.affine_radio = ttk.Radiobutton(
            self.chiper_frame, text='Affine', variable=self.chiper_var, value='affine')

        self.vigenere_radio.grid(row=0, column=0, sticky='nw')
        self.full_vigenere_radio.grid(row=0, column=1, sticky='nw')
        self.autokey_vigenere_radio.grid(row=1, column=0, sticky='nw')
        self.extended_vigenere_radio.grid(row=1, column=1, sticky='nw')
        self.playfair_radio.grid(row=2, column=0, sticky='nw')
        self.affine_radio.grid(row=2, column=1, sticky='nw')

        self.full_vigenere_radio.state(['disabled'])
        self.affine_radio.state(['disabled'])

        for child in self.chiper_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def draw_task_frame(self):

        self.task_frame = ttk.Labelframe(self.mainframe, text='Task')
        self.task_frame.grid(row=20, column=10)

        self.task_var = StringVar()
        self.task_var.set('encrypt')

        self.encrypt_radio = ttk.Radiobutton(
            self.task_frame, text='Encrypt', variable=self.task_var, value='encrypt')
        self.decrypt_radio = ttk.Radiobutton(
            self.task_frame, text='Decrypt', variable=self.task_var, value='decrypt')

        self.encrypt_radio.grid(row=0, column=0, sticky='nw')
        self.decrypt_radio.grid(row=0, column=1, sticky='nw')

        for child in self.task_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def draw_action_frame(self):
        self.action_frame = ttk.Frame(self.mainframe)
        self.action_frame.grid(row=40, column=10)

        ttk.Separator(self.action_frame).grid(row=10, column=10, pady=16)

        self.start_button = ttk.Button(
            self.action_frame, text='START', command=self.action_start)
        self.start_button.grid(row=20, column=10)

    def draw_output_frame(self):

        self.output_frame = ttk.Labelframe(self.mainframe, text='Output')
        self.output_frame.grid(row=80, column=10)

        self.output_buttons_frame = ttk.Frame(self.output_frame)
        self.output_buttons_frame.grid(row=5, column=10, sticky='we')

        self.output_mode_var = StringVar()
        self.output_mode_var.set('nospace')

        self.no_space_radio = ttk.Radiobutton(
            self.output_buttons_frame, text="No space", variable=self.output_mode_var, value='nospace', command=self.update_output_mode)
        self.no_space_radio.grid(row=5, column=10, sticky='w')
        self.five_grouped_radio = ttk.Radiobutton(
            self.output_buttons_frame, text="5-grouped", variable=self.output_mode_var, value='five', command=self.update_output_mode)
        self.five_grouped_radio.grid(row=5, column=20, sticky='w')

        self.output_text = Text(self.output_frame, height=5, width=64)
        self.output_text.grid(row=10, column=10, sticky='we')

        for child in self.output_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def update_output_mode(self):
        mode = self.output_mode_var.get()

        if mode == 'nospace':
            self.update_output(content=self.output_content)
        elif mode == 'five':
            self.update_output(
                content=tools.string_group_five(self.output_content))

    def update_input(self, content='', enabled=True):
        self.input_text.delete('1.0', END)
        self.input_text.insert('1.0', content)

    def update_output(self, content='', enabled=True):
        self.output_text.delete('1.0', END)
        self.output_text.insert('1.0', content)

    def action_start(self):
        self.input_content = self.input_text.get('1.0', END)
        self.key = self.key_text.get('1.0', END)

        decrpyt = self.task_var.get() == 'decrypt'
        chiper = self.chiper_var.get()

        if (chiper == 'vigenere'):
            self.output_content = chipers.vigenere(
                self.input_content, self.key, decrpyt)
        elif (chiper == 'autokey_vigenere'):
            self.output_content = chipers.autokey_vigenere(
                self.input_content, self.key, decrpyt)
        elif (chiper == 'extended_vigenere'):
            self.output_content = chipers.extended_vigenere(
                self.input_content, self.key, decrpyt)
        elif (chiper == 'playfair'):
            self.output_content = chipers.playfair(
                self.input_content, self.key, decrpyt)

        self.update_output_mode()


root = Tk()
Crypthon(root)
root.mainloop()
