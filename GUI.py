import tkinter
from tkinter.ttk import Treeview

import user_management_new
from user_management_new import user_management_new
from tkinter import messagebox, END

from users import User

width = 800
height = 600


class GUI:

    def __init__(self, root, store: user_management_new):
        self.root = root
        self.store = store
        self.user_id = None
        # self.user_id = 1
        self.root.title('Two-way Street')
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


class LikeAndDislike:
    def __init__(self, gui: GUI):
        self.page = None
        self.username_input = None
        self.password_input = None
        self.gui = gui
        self.index = -1
        self.init()

    def init(self):
        self.page = tkinter.Frame(self.gui.root, width=width, height=height, bg='white')
        self.page.pack()
        self.next()

    def next(self):

        back_btn = tkinter.Button(
            self.page,
            text="Back",
            command=self.back
        )
        back_btn.place(
            width=100,
            height=40,
            x=0,
            y=0
        )

        users = []
        for index, user in self.gui.store.get_all_users().iterrows():
            users.append(user)

        if len(users) == 0 or len(users) < (self.index + 1 + 1):
            return

        self.index += 1

        like_btn = tkinter.Button(
            self.page,
            text="Like",
            command=self.like
        )
        like_btn.place(
            width=350,
            height=40,
            x=width * 0.3,
            y=height * 0.8
        )
        dislike_btn = tkinter.Button(
            self.page,
            text="Dislike",
            command=self.dislike
        )
        dislike_btn.place(
            width=350,
            height=40,
            x=width * 0.3,
            y=height * 0.9
        )

        user = users[self.index]

        y = 0.0
        for key in [['name', 'name'], ['age', 'age'], ['gender', 'gender'], ['location', 'location'],
                    ['preferred_genders', 'preferred genders'],
                    ['age_low', 'preferred age low'],
                    ['age_high', 'preferred age high']]:
            y += 0.1
            tkinter.Label(self.page, text=key[1]).place(
                width=150,
                height=30,
                x=width * 0.3,
                y=height * y
            )
            tkinter.Label(self.page, text=user[key[0]]).place(
                width=200,
                height=30,
                x=width * 0.5,
                y=height * y
            )

    def like(self):
        users = []
        for index, user in self.gui.store.get_all_users().iterrows():
            users.append(user)

        if len(users) == 0 or len(users) < (self.index + 1 + 1):
            return

        user = users[self.index]

        self.gui.store.like_profile(user['user_id'], self.gui.user_id)

        self.next()

    def dislike(self):
        users = []
        for index, user in self.gui.store.get_all_users().iterrows():
            users.append(user)

        if len(users) == 0 or len(users) < (self.index + 1 + 1):
            return

        user = users[self.index]

        self.gui.store.dislike_profile(user['user_id'], self.gui.user_id)

        self.next()

    def back(self):
        self.page.pack_forget()
        Home(self.gui)


class Register:
    def __init__(self, gui: GUI):
        self.preferred_gender_m_input = None
        self.preferred_gender_f_input = None
        self.preferred_gender_o_input = None
        self.page = None
        self.username_input = None
        self.password_input = None
        self.name_input = None
        self.age_input = None
        self.gender_input = None
        self.location_input = None
        self.preferred_age_low_input = None
        self.preferred_age_high_input = None
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

        preferred_age = tkinter.Label(self.page, text="Preferred Age")
        preferred_age.place(
            width=100,
            height=30,
            x=width * 0.2,
            y=height * 0.7
        )
        self.preferred_age_low_input = tkinter.Entry(self.page)
        self.preferred_age_low_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.4,
            y=height * 0.7
        )
        preferred_age_ = tkinter.Label(self.page, text="-")
        preferred_age_.place(
            width=20,
            height=30,
            x=width * 0.55 - 10,
            y=height * 0.7
        )
        self.preferred_age_high_input = tkinter.Entry(self.page)
        self.preferred_age_high_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.6,
            y=height * 0.7
        )

        preferred_gender = tkinter.Label(self.page, text="Preferred Gender")
        preferred_gender.place(
            width=100,
            height=30,
            x=width * 0.2,
            y=height * 0.8
        )

        self.preferred_gender_m_input = tkinter.IntVar()
        preferred_gender_m_input = tkinter.Checkbutton(
            self.page,
            text="Male",
            variable=self.preferred_gender_m_input
        )
        preferred_gender_m_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.4,
            y=height * 0.8
        )
        self.preferred_gender_f_input = tkinter.IntVar()
        preferred_gender_f_input = tkinter.Checkbutton(
            self.page,
            text="Female",
            variable=self.preferred_gender_f_input
        )
        preferred_gender_f_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.5,
            y=height * 0.8
        )
        self.preferred_gender_o_input = tkinter.IntVar()
        preferred_gender_o_input = tkinter.Checkbutton(
            self.page,
            text="Other",
            variable=self.preferred_gender_o_input
        )
        preferred_gender_o_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.6,
            y=height * 0.8
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
            y=height * 0.9
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
        if self.preferred_age_low_input is None:
            messagebox.showerror("ERROR", "preferred age low is None")
            return
        if self.preferred_age_high_input is None:
            messagebox.showerror("ERROR", "preferred age high is None")
            return
        if self.preferred_gender_m_input is None:
            messagebox.showerror("ERROR", "preferred gender is None")
            return
        if self.preferred_gender_f_input is None:
            messagebox.showerror("ERROR", "preferred gender is None")
            return
        if self.preferred_gender_o_input is None:
            messagebox.showerror("ERROR", "preferred gender is None")
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

        try:
            preferred_age_low = int(self.preferred_age_low_input.get().strip())
        except Exception:
            preferred_age_low = None
        if preferred_age_low is None or preferred_age_low <= 0 or preferred_age_low > 100:
            messagebox.showerror("ERROR", "preferred age low is ERROR")
            return
        if preferred_age_low is None or preferred_age_low <= 0 or preferred_age_low > 100:
            messagebox.showerror("ERROR", "preferred age low is ERROR")
            return

        try:
            preferred_age_high = int(self.preferred_age_high_input.get().strip())
        except Exception:
            preferred_age_high = None
        if preferred_age_high is None or preferred_age_high <= 0 or preferred_age_high > 100:
            messagebox.showerror("ERROR", "preferred age high is ERROR")
            return
        if preferred_age_high is None or preferred_age_high <= 0 or preferred_age_high > 100:
            messagebox.showerror("ERROR", "preferred age high is ERROR")
            return

        if preferred_age_high < preferred_age_low:
            messagebox.showerror("ERROR", "The preferred age high cannot be less than the preferred age low.")
            return

        if (self.preferred_gender_m_input.get() == 0
                and self.preferred_gender_f_input.get() == 0
                and self.preferred_gender_o_input.get() == 0):
            messagebox.showerror("ERROR", "preferred gender is Empty")
            return

        preferred_gender = ''
        if (self.preferred_gender_m_input.get() == 1):
            preferred_gender = preferred_gender + 'M'
        if (self.preferred_gender_f_input.get() == 1):
            preferred_gender = preferred_gender + 'F'
        if (self.preferred_gender_o_input.get() == 1):
            preferred_gender = preferred_gender + 'O'

        user: User = self.gui.store.create_user(
            self.username_input.get().strip(),
            self.password_input.get().strip(),
            self.name_input.get().strip(),
            int(self.age_input.get().strip()),
            self.gender_input.get().strip(),
            self.location_input.get().strip(),
            [],
            preferred_gender,
            int(self.preferred_age_low_input.get().strip()),
            int(self.preferred_age_high_input.get().strip())
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
            text="Like/Dislike",
            command=self.likeAndDislike
        )
        like_btn.place(
            width=100,
            height=30,
            x=10,
            y=10
        )

        # dislike_btn = tkinter.Button(
        #     self.page,
        #     text="Dislike",
        #     command=self.dislike
        # )
        # dislike_btn.place(
        #     width=50,
        #     height=30,
        #     x=80,
        #     y=10
        # )

        show_like_dislike_btn = tkinter.Button(
            self.page,
            text="See Who Like Or Dislike Me",
            command=self.show_like_dislike
        )
        show_like_dislike_btn.place(
            width=180,
            height=30,
            x=140,
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
            columns = ("id", "username", "name", "age", "gender", "location", "preferred_genders", "preferred_age")
            self.treeview = Treeview(self.excel_page, show="headings", columns=columns, height=25)

            self.treeview.heading("id", text="id")
            self.treeview.column('id', width=int(width * 0.05))
            self.treeview.heading("username", text="username")
            self.treeview.column('username', width=int(width * 0.1))
            self.treeview.heading("name", text="name")
            self.treeview.column('name', width=int(width * 0.1))
            self.treeview.heading("age", text="age")
            self.treeview.column('age', width=int(width * 0.05))
            self.treeview.heading("gender", text="gender")
            self.treeview.column('gender', width=int(width * 0.1))
            self.treeview.heading("location", text="location")
            self.treeview.column('location', width=int(width * 0.2))
            self.treeview.heading("preferred_genders", text="preferred genders")
            self.treeview.column('preferred_genders', width=int(width * 0.2))
            self.treeview.heading("preferred_age", text="preferred age")
            self.treeview.column('preferred_age', width=int(width * 0.2))

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
                user['preferred_genders'],
                str(user['age_low']) + '-' + str(user['age_high']),
            ))

        self.treeview.pack()

    # def like(self):
    #     selected_items = self.treeview.selection()
    #     for item in selected_items:
    #         user_id = self.treeview.item(item, 'values')[0]
    #         self.gui.store.like_profile(user_id, self.gui.user_id)

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

    # def dislike(self):
    #     selected_items = self.treeview.selection()
    #     for item in selected_items:
    #         user_id = self.treeview.item(item, 'values')[0]
    #         self.gui.store.dislike_profile(user_id, self.gui.user_id)

    def likeAndDislike(self):
        self.excel_page.pack_forget()
        self.page.pack_forget()
        LikeAndDislike(self.gui)

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
