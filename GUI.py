import tkinter
from tkinter.ttk import Treeview

import user_management_new
from user_management_new import user_management_new
from tkinter import messagebox, END

from users import User

width = 600
height = 600


class GUI:

    def __init__(self, root, store: user_management_new):
        self.root = root
        self.store = store
        # self.user_id = None
        self.user_id = 1
        self.root.title('GUI')
        self.root.geometry(str(width) + "x" + str(height))


class Login:
    def __init__(self, gui: GUI):
        self.page = None
        self.username_input = None
        self.password_input = None
        self.gui = gui
        self.init()

    def init(self):
        self.page = tkinter.Frame(self.gui.root, width=width, height=height, bg='white')
        self.page.pack()

        username = tkinter.Label(self.page, text="Username")
        username.place(
            width=100,
            height=30,
            x=width * 0.2,
            y=height * 0.3
        )

        self.username_input = tkinter.Entry(self.page)
        self.username_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.3
        )

        password = tkinter.Label(self.page, text="Password")
        password.place(
            width=100,
            height=30,
            x=width * 0.2,
            y=height * 0.45
        )

        self.password_input = tkinter.Entry(self.page)
        self.password_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.45
        )

        login_btn = tkinter.Button(
            self.page,
            text="Login",
            command=self.login,
        )
        login_btn.place(
            width=200,
            height=50,
            x=(width - 200) / 2,
            y=height * 0.6
        )

        register_btn = tkinter.Button(
            self.page,
            text="Register",
            command=self.register,
        )
        register_btn.place(
            width=200,
            height=50,
            x=(width - 200) / 2,
            y=height * 0.7
        )

    def login(self):
        if self.username_input is None:
            messagebox.showerror("ERROR", "username is None")
            return
        if self.password_input is None:
            messagebox.showerror("ERROR", "password is None")
            return
        if self.username_input.get().strip() == "":
            messagebox.showerror("ERROR", "username is Empty")
            return
        if self.password_input.get().strip() == "":
            messagebox.showerror("ERROR", "password is Empty")
            return
        try:
            password = self.gui.store.get_user_password(self.username_input.get().strip())
            self.gui.user_id = self.gui.store.get_user_id(self.username_input.get().strip())
        except Exception:
            password = None
            self.gui.user_id = None
        if password is None:
            messagebox.showerror("ERROR", "username is ERROR")
            return
        if password.strip() != self.password_input.get().strip():
            messagebox.showerror("ERROR", "password is ERROR")
            return

        self.page.pack_forget()
        Home(self.gui)

    def register(self):
        self.page.pack_forget()
        Register(self.gui)


class Register:
    def __init__(self, gui: GUI):
        self.page = None
        self.username_input = None
        self.password_input = None
        self.name_input = None
        self.age_input = None
        self.gender_input = None
        self.location_input = None
        self.gui = gui
        self.init()

    def init(self):
        self.page = tkinter.Frame(self.gui.root, width=width, height=height, bg='white')
        self.page.pack()

        username = tkinter.Label(self.page, text="Username")
        username.place(
            width=100,
            height=30,
            x=width * 0.2,
            y=height * 0.1
        )
        self.username_input = tkinter.Entry(self.page)
        self.username_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.1
        )

        password = tkinter.Label(self.page, text="Password")
        password.place(
            width=100,
            height=30,
            x=width * 0.2,
            y=height * 0.2
        )
        self.password_input = tkinter.Entry(self.page)
        self.password_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.2
        )

        name = tkinter.Label(self.page, text="Name")
        name.place(
            width=100,
            height=30,
            x=width * 0.2,
            y=height * 0.3
        )
        self.name_input = tkinter.Entry(self.page)
        self.name_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.3
        )

        age = tkinter.Label(self.page, text="Age")
        age.place(
            width=100,
            height=30,
            x=width * 0.2,
            y=height * 0.4
        )
        self.age_input = tkinter.Entry(self.page)
        self.age_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.4
        )

        gender = tkinter.Label(self.page, text="Gender")
        gender.place(
            width=100,
            height=30,
            x=width * 0.2,
            y=height * 0.5
        )

        self.gender_input = tkinter.StringVar()
        male_radio = tkinter.Radiobutton(
            self.page,
            text="Male",
            variable=self.gender_input,
            value="M"
        )
        male_radio.place(
            width=width * 0.1,
            height=30,
            x=width * 0.4,
            y=height * 0.5
        )
        female_radio = tkinter.Radiobutton(
            self.page,
            text="Female",
            variable=self.gender_input,
            value="F"
        )
        female_radio.place(
            width=width * 0.1,
            height=30,
            x=width * 0.5,
            y=height * 0.5
        )
        other_radio = tkinter.Radiobutton(
            self.page,
            text="Other",
            variable=self.gender_input,
            value="O"
        )
        other_radio.place(
            width=width * 0.1,
            height=30,
            x=width * 0.6,
            y=height * 0.5
        )
        other_radio.select()

        location = tkinter.Label(self.page, text="Location")
        location.place(
            width=100,
            height=30,
            x=width * 0.2,
            y=height * 0.6
        )
        self.location_input = tkinter.Entry(self.page)
        self.location_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.6
        )

        submit_btn = tkinter.Button(
            self.page,
            text="Submit",
            command=self.submit,
        )
        submit_btn.place(
            width=200,
            height=50,
            x=(width - 200) / 2,
            y=height * 0.7
        )

    def submit(self):
        if self.username_input is None:
            messagebox.showerror("ERROR", "username is None")
            return
        if self.password_input is None:
            messagebox.showerror("ERROR", "password is None")
            return
        if self.name_input is None:
            messagebox.showerror("ERROR", "name is None")
            return
        if self.age_input is None:
            messagebox.showerror("ERROR", "age is None")
            return
        if self.gender_input is None:
            messagebox.showerror("ERROR", "gender is None")
            return
        if self.location_input is None:
            messagebox.showerror("ERROR", "location is None")
            return

        if self.username_input.get().strip() == "":
            messagebox.showerror("ERROR", "username is Empty")
            return
        if self.gui.store.check_valid_username(self.username_input.get().strip()) == False:
            messagebox.showerror("ERROR", "username already exists")
            return
        if self.name_input.get().strip() == "":
            messagebox.showerror("ERROR", "name is Empty")
            return

        try:
            age = int(self.age_input.get().strip())
        except Exception:
            age = None
        if age is None or age <= 0 or age > 100:
            messagebox.showerror("ERROR", "age is ERROR")
            return

        if self.gender_input.get().strip() == "":
            messagebox.showerror("ERROR", "gender is Empty")
            return
        if self.location_input.get().strip() == "":
            messagebox.showerror("ERROR", "location is Empty")
            return

        user: User = self.gui.store.create_user(
            self.username_input.get().strip(),
            self.password_input.get().strip(),
            self.name_input.get().strip(),
            int(self.age_input.get().strip()),
            self.gender_input.get().strip(),
            self.location_input.get().strip(),
            [],
            'O'
        )

        if self.gui.store.add_user_to_db(user) == False:
            messagebox.showerror("ERROR", "register ERROR")
        else:
            messagebox.showinfo("SUCCESS", "register SUCCESS")
            self.page.pack_forget()
            Login(self.gui)


class Home:
    def __init__(self, gui: GUI):
        self.scrollbar = None
        self.excel_page = None
        self.page = None
        self.gui = gui
        self.treeview = None
        self.init()

    def init(self):
        self.excel_page = tkinter.Frame(self.gui.root, width=width, height=height * 0.8, bg='white')
        self.page = tkinter.Frame(self.gui.root, width=width, height=height * 0.2, bg='white')

        self.excel_page.pack()
        self.page.pack()

        self.reload()

        like_btn = tkinter.Button(
            self.page,
            text="Like",
            command=self.like
        )
        like_btn.place(
            width=50,
            height=30,
            x=10,
            y=10
        )

        dislike_btn = tkinter.Button(
            self.page,
            text="Dislike",
            command=self.dislike
        )
        dislike_btn.place(
            width=50,
            height=30,
            x=80,
            y=10
        )

        show_like_dislike_btn = tkinter.Button(
            self.page,
            text="Show Like and Dislike List",
            command=self.show_like_dislike
        )
        show_like_dislike_btn.place(
            width=180,
            height=30,
            x=150,
            y=10
        )

        logout_btn = tkinter.Button(
            self.page,
            text="Logout",
            command=self.logout
        )
        logout_btn.place(
            width=50,
            height=30,
            x=350,
            y=10
        )

    def reload(self):
        if self.treeview != None:
            for child in self.treeview:
                self.treeview.delete(child)
        else:
            columns = ("id", "username", "name", "age", "gender", "location")
            self.treeview = Treeview(self.excel_page, show="headings", columns=columns, height=25)

            self.treeview.heading("id", text="id")
            self.treeview.column('id', width=int(width * 0.1))
            self.treeview.heading("username", text="username")
            self.treeview.column('username', width=int(width * 0.2))
            self.treeview.heading("name", text="name")
            self.treeview.column('name', width=int(width * 0.2))
            self.treeview.heading("age", text="age")
            self.treeview.column('age', width=int(width * 0.1))
            self.treeview.heading("gender", text="gender")
            self.treeview.column('gender', width=int(width * 0.1))
            self.treeview.heading("location", text="location")
            self.treeview.column('location', width=int(width * 0.3))

            self.scrollbar = tkinter.Scrollbar(
                self.excel_page,
                orient='vertical',
                command=self.treeview.yview
            )

            # self.treeview.place(relx=0.004, rely=0.028, relwidth=0.964, relheight=1)
            # self.treeview.place(height = 100,relx=0.004, rely=0.028, relwidth=0.964, relheight=1)
            self.scrollbar.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
            self.treeview.configure(yscrollcommand=self.scrollbar.set)

        users = self.gui.store.get_all_users()
        for index, user in users.iterrows():
            self.treeview.insert('', 'end', values=(
                user['user_id'],
                user['username'],
                user['name'],
                user['age'],
                user['gender'],
                user['location'],
            ))

        self.treeview.pack()

    def like(self):
        selected_items = self.treeview.selection()
        for item in selected_items:
            user_id = self.treeview.item(item, 'values')[0]
            self.gui.store.like_profile(user_id, self.gui.user_id)

    def show_like_dislike(self):
        like_userids = self.gui.store.get_liked_profiles(self.gui.user_id)
        like_str = "liked:"
        fist = True
        for userid in like_userids:
            if fist is True:
                fist = False
            else:
                like_str = like_str + ", "
            like_str = like_str + str(userid)
        if fist is True:
            like_str = like_str + "Empty"
        dislike_userids = self.gui.store.get_disliked_profiles(self.gui.user_id)
        dislike_str = "disliked:"
        fist = True
        for userid in dislike_userids:
            if fist is True:
                fist = False
            else:
                dislike_str = dislike_str + ", "
            dislike_str = dislike_str + str(userid)
        if fist is True:
            dislike_str = dislike_str + "Empty"
        messagebox.showinfo("Like and Dislike List", like_str + "\n" + dislike_str)

    def dislike(self):
        selected_items = self.treeview.selection()
        for item in selected_items:
            user_id = self.treeview.item(item, 'values')[0]
            self.gui.store.dislike_profile(user_id, self.gui.user_id)

    def logout(self):
        self.excel_page.pack_forget()
        self.page.pack_forget()
        Login(self.gui)

def start():
    root = tkinter.Tk()
    store = user_management_new()
    gui = GUI(root, store)
    Login(gui)
    # Home(gui)
    root.mainloop()

if __name__ == '__main__':
    start()
