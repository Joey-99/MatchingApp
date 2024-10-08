import tkinter
from tkinter.ttk import Treeview

import user_management_new
from user_management_new import user_management_new
from tkinter import messagebox, END

from users import User

width = 800
height = 600

ontario_cities = [
    "Toronto",
    "Ottawa",
    "Mississauga",
    "Brampton",
    "Hamilton",
    "London",
    "Markham",
    "Vaughan",
    "Kitchener",
    "Windsor",
    "Richmond Hill",
    "Burlington",
    "Oshawa",
    "Greater Sudbury",
    "Barrie",
    "Guelph",
    "Cambridge",
    "St. Catharines",
    "Waterloo",
    "Thunder Bay",
    "Brantford",
    "Pickering",
    "Niagara Falls",
    "Peterborough",
    "Sault Ste. Marie",
    "Sarnia",
    "Norfolk County",
    "Welland",
    "Belleville",
    "North Bay"
]

# manage main window and navigations to login and register
class GUI:

    def __init__(self, root, store: user_management_new):
        self.root = root
        self.store = store
        self.user_id = None
        # self.user_id = 10
        self.root.title('Two-way Street')
        self.root.geometry(str(width) + "x" + str(height))

# logic and interface for login window
class Login:
    def __init__(self, gui: GUI):
        self.page = None # hold login page
        self.username_input = None
        self.password_input = None
        self.gui = gui
        self.init()

    def init(self):
        self.page = tkinter.Frame(self.gui.root, width=width, height=height, bg='white')
        self.page.pack() # create and display the frame
        # display application title
        image_label = tkinter.Label(self.page, text='TWO-WAY STREET <3', font=("Helvetica", 36), anchor='n', width=width, height=int(height*0.5))
        image_label.pack()
        # username input label and field
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
        # password input label and field
        password = tkinter.Label(self.page, text="Password")
        password.place(
            width=100,
            height=30,
            x=width * 0.2,
            y=height * 0.45
        )

        self.password_input = tkinter.Entry(self.page, show='*')
        self.password_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.45
        )
        # login button
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
        # register button to navigate to registeration screen
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
    # login logic when click the login button
    def login(self):
        # validate username and password
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
        # retrieve user data based on the provided username
        try:
            password = self.gui.store.get_user_password(self.username_input.get().strip())
            self.gui.user_id = self.gui.store.get_user_id(self.username_input.get().strip())
        except Exception:
            password = None
            self.gui.user_id = None
        # verify the retrieved password against the input password
        if password is None:
            messagebox.showerror("ERROR", "username is ERROR")
            return
        if password.strip() != self.password_input.get().strip():
            messagebox.showerror("ERROR", "password is ERROR")
            return
        # if the login is successful, navigate to the main menu screen
        self.page.pack_forget()
        Menu(self.gui)
    # navigate to the registration window when click "Register" button
    def register(self):
        self.page.pack_forget()
        Register(self.gui)

# for browsing profiles and choose like or dislike
class LikeAndDislike:
    def __init__(self, gui: GUI):
        self.page = None
        self.username_input = None
        self.password_input = None
        self.gui = gui
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

        users = self.gui.store.get_potentials(self.gui.user_id)
        if len(users) == 0:
            messagebox.showerror("ERROR", " there are no users to view")

            return

        # like button
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
        # dislike button
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

        user = users.loc[users.index[0]]

        y = 0.0
        for key in [
            ['name', 'name'],
            ['age', 'age'],
            ['gender', 'gender'],
            ['location', 'location'],
            ['education', 'education'],
            ['interests', 'interests'],
            ['politics', 'politics'],
            ['intentions', 'intentions'],
            ['preferred_genders', 'preferred genders'],
            ['age_low', 'preferred age low'],
            ['age_high', 'preferred age high']
        ]:
            y += 0.065
            tkinter.Label(self.page, text=key[1]).place(
                width=150,
                height=30,
                x=width * 0.2,
                y=height * y
            )
            text = user[key[0]]
            tkinter.Label(self.page, text=text).place(
                width=350,
                height=30,
                x=width * 0.4,
                y=height * y
            )

    def like(self):
        users = self.gui.store.get_potentials(self.gui.user_id)
        if len(users) == 0:
            messagebox.showerror("ERROR", " there are no users to view")
            return

        user = users.loc[users.index[0]]

        matches_before = self.gui.store.number_of_matches(self.gui.user_id)
        self.gui.store.like_profile(self.gui.user_id, user['user_id'])
        matches_after = self.gui.store.number_of_matches(self.gui.user_id)
        if matches_after > matches_before:
            messagebox.showerror("Congratulations!!", "You have found a new match!")

        self.next()

    def dislike(self):
        users = self.gui.store.get_potentials(self.gui.user_id)
        if len(users) == 0:
            messagebox.showerror("ERROR", " there are no users to view")
            return

        user = users.loc[users.index[0]]

        self.gui.store.dislike_profile(self.gui.user_id, user['user_id'])

        self.next()

    def back(self):
        self.page.pack_forget()
        Menu(self.gui)

# register window both for creating and editing profiles
class Register:
    # initialize the registration window
    def __init__(self, gui: GUI):
        self.political_orientation_input = None
        self.dating_intentions_input = None
        self.interests_input = None
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

        # 2 is change
        self.state = 1
        self.oldUsername = None
        self.user = None

    # change to edit current user
    def change(self, user: User):
        self.user = user
        self.oldUsername = user.username
        self.state = 2

        self.username_input.insert(0, user.username)
        self.password_input.insert(0, user.password)
        self.name_input.insert(0, user.name)
        self.age_input.insert(0, user.age)
        self.location_input.set(user.location)
        self.gender_input.set(user.gender[0])
        self.preferred_age_low_input.insert(0, user.age_low)
        self.preferred_age_high_input.insert(0, user.age_high)
        self.education_level_input.set(user.education)

        for value in user.interests:
            for interests in self.interests_input:
                if value == interests['value']:
                    interests['select'].set(1)

        if 'M' in user.preferred_genders:
            self.preferred_gender_m_input.set(1)
        if 'F' in user.preferred_genders:
            self.preferred_gender_f_input.set(1)
        if 'O' in user.preferred_genders:
            self.preferred_gender_o_input.set(1)

        self.political_orientation_input.set(user.politics)
        self.dating_intentions_input.set(user.intentions)

    # fill current user info for user to edit
    def callback(self, user: User, state,
                 username, password, name, age, gender, location, education, interests, politics,
                 intentions, preferred_genders, age_low, age_high):
        self.user = user
        self.state = state
        self.username_input.insert(0, username)
        self.password_input.insert(0, password)
        self.name_input.insert(0, name)
        self.age_input.insert(0, age)
        self.location_input.set(location)
        self.gender_input.set(gender[0])
        self.preferred_age_low_input.insert(0, age_low)
        self.preferred_age_high_input.insert(0, age_high)
        self.education_level_input.set(education)

        for value in interests:
            for interests in self.interests_input:
                if value == interests['value']:
                    interests['select'].set(1)

        if 'M' in preferred_genders:
            self.preferred_gender_m_input.set(1)
        if 'F' in preferred_genders:
            self.preferred_gender_f_input.set(1)
        if 'O' in preferred_genders:
            self.preferred_gender_o_input.set(1)

        self.political_orientation_input.set(politics)
        self.dating_intentions_input.set(intentions)

    def init(self):
        self.page = tkinter.Frame(self.gui.root, width=width, height=height, bg='white')
        self.page.pack()

        username = tkinter.Label(self.page, text="Username")
        username.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0
        )
        self.username_input = tkinter.Entry(self.page)
        self.username_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0
        )

        password = tkinter.Label(self.page, text="Password")
        password.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0.06
        )
        self.password_input = tkinter.Entry(self.page, show='*')
        self.password_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.06
        )

        name = tkinter.Label(self.page, text="Name")
        name.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0.12
        )
        self.name_input = tkinter.Entry(self.page)
        self.name_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.12
        )

        age = tkinter.Label(self.page, text="Age")
        age.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0.18
        )
        self.age_input = tkinter.Entry(self.page)
        self.age_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.18
        )

        location = tkinter.Label(self.page, text="Location")
        location.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0.24
        )

        self.location_input = tkinter.ttk.Combobox(self.page, state='readonly')
        self.location_input['values'] = ontario_cities
        self.location_input.set(self.location_input['values'][0])
        self.location_input.place(
            width=width * 0.3,
            height=30,
            x=width * 0.4,
            y=height * 0.24
        )

        gender = tkinter.Label(self.page, text="Gender")
        gender.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0.3
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
            y=height * 0.3
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
            y=height * 0.3
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
            y=height * 0.3
        )
        other_radio.select()

        preferred_age = tkinter.Label(self.page, text="Preferred Age")
        preferred_age.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0.36
        )
        self.preferred_age_low_input = tkinter.Entry(self.page)
        self.preferred_age_low_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.4,
            y=height * 0.36
        )
        preferred_age_ = tkinter.Label(self.page, text="-")
        preferred_age_.place(
            width=20,
            height=30,
            x=width * 0.55 - 10,
            y=height * 0.36
        )
        self.preferred_age_high_input = tkinter.Entry(self.page)
        self.preferred_age_high_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.6,
            y=height * 0.36
        )

        education_level = tkinter.Label(self.page, text="Education Level")
        education_level.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0.42
        )

        self.education_level_input = tkinter.StringVar()
        education_level_highschool_input = tkinter.Radiobutton(
            self.page,
            text="highschool",
            variable=self.education_level_input,
            value="highschool"
        )
        education_level_highschool_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.4,
            y=height * 0.42
        )
        education_level_college_input = tkinter.Radiobutton(
            self.page,
            text="college",
            variable=self.education_level_input,
            value="college"
        )
        education_level_college_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.5,
            y=height * 0.42
        )
        education_level_bachelor_input = tkinter.Radiobutton(
            self.page,
            text="bachelor",
            variable=self.education_level_input,
            value="bachelor"
        )
        education_level_bachelor_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.6,
            y=height * 0.42
        )
        education_level_master_input = tkinter.Radiobutton(
            self.page,
            text="master",
            variable=self.education_level_input,
            value="master"
        )
        education_level_master_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.7,
            y=height * 0.42
        )
        education_level_phd_input = tkinter.Radiobutton(
            self.page,
            text="phd",
            variable=self.education_level_input,
            value="phd"
        )
        education_level_phd_input.place(
            width=width * 0.1,
            height=30,
            x=width * 0.8,
            y=height * 0.42
        )
        education_level_highschool_input.select()

        interests = tkinter.Label(self.page, text="Interests")
        interests.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0.48
        )

        interests = [
            "music", "movies", "sports", "reading", "travel",
            "hiking", "cooking", "gaming", "gardening"
        ]
        index = -1
        line = -1
        self.interests_input = []
        for interest in interests:
            index += 1
            if index % 5 == 0:
                line += 1

            self.interests_input.append({'value': interest, 'select': tkinter.IntVar()})
            temp = tkinter.Checkbutton(
                self.page,
                text=interest,
                variable=self.interests_input[-1]['select']
            )
            temp.place(
                width=width * 0.11,
                height=30,
                x=width * (0.4 + 0.11 * (index % 5)),
                y=height * 0.48 + line * 30
            )

        preferred_gender = tkinter.Label(self.page, text="Preferred Gender")
        preferred_gender.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0.6
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
            y=height * 0.6
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
            y=height * 0.6
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
            y=height * 0.6
        )

        political_orientation = tkinter.Label(self.page, text="Political orientation")
        political_orientation.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0.66
        )
        self.political_orientation_input = tkinter.StringVar()
        political_orientation_input_l_radio = tkinter.Radiobutton(
            self.page,
            text="Liberal",
            variable=self.political_orientation_input,
            value="L"
        )
        political_orientation_input_l_radio.place(
            width=width * 0.1,
            height=30,
            x=width * 0.4,
            y=height * 0.66
        )
        political_orientation_input_c_radio = tkinter.Radiobutton(
            self.page,
            text="Conservative",
            variable=self.political_orientation_input,
            value="C"
        )
        political_orientation_input_c_radio.place(
            width=width * 0.15,
            height=30,
            x=width * 0.5,
            y=height * 0.66
        )
        political_orientation_input_n_radio = tkinter.Radiobutton(
            self.page,
            text="Neutral",
            variable=self.political_orientation_input,
            value="N"
        )
        political_orientation_input_n_radio.place(
            width=width * 0.1,
            height=30,
            x=width * 0.65,
            y=height * 0.66
        )
        political_orientation_input_n_radio.select()

        dating_intentions = tkinter.Label(self.page, text="Dating orientation")
        dating_intentions.place(
            width=150,
            height=30,
            x=width * 0.2,
            y=height * 0.72
        )
        self.dating_intentions_input = tkinter.StringVar()
        dating_intentions_input_s_radio = tkinter.Radiobutton(
            self.page,
            text="Short-term",
            variable=self.dating_intentions_input,
            value="S"
        )
        dating_intentions_input_s_radio.place(
            width=width * 0.12,
            height=30,
            x=width * 0.4,
            y=height * 0.72
        )
        dating_intentions_input_l_radio = tkinter.Radiobutton(
            self.page,
            text="Long-term",
            variable=self.dating_intentions_input,
            value="L"
        )
        dating_intentions_input_l_radio.place(
            width=width * 0.12,
            height=30,
            x=width * 0.52,
            y=height * 0.72
        )
        dating_intentions_input_c_radio = tkinter.Radiobutton(
            self.page,
            text="Casual",
            variable=self.dating_intentions_input,
            value="C"
        )
        dating_intentions_input_c_radio.place(
            width=width * 0.12,
            height=30,
            x=width * 0.64,
            y=height * 0.72
        )
        dating_intentions_input_lp_radio = tkinter.Radiobutton(
            self.page,
            text="Life partner",
            variable=self.dating_intentions_input,
            value="LP"
        )
        dating_intentions_input_lp_radio.place(
            width=width * 0.15,
            height=30,
            x=width * 0.76,
            y=height * 0.72
        )
        dating_intentions_input_lp_radio.select()

        # final submit and return button
        submit_btn = tkinter.Button(
            self.page,
            text="Back",
            command=self.back,
        )
        submit_btn.place(
            width=200,
            height=50,
            x=(width - 200) / 2,
            y=height * 0.9 - 60
        )
        submit_btn = tkinter.Button(
            self.page,
            text="Next",
            command=self.submit,
        )
        submit_btn.place(
            width=200,
            height=50,
            x=(width - 200) / 2,
            y=height * 0.9
        )

    # validate the input data from user and handle register or update
    def submit(self):

        if self.username_input.get().strip() == "":
            messagebox.showerror("ERROR", "username is Empty")
            return
        if self.state != 2 or self.oldUsername != self.user.username:
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
        if age is None or age <= 18 or age > 100:
            messagebox.showerror("ERROR", "age is ERROR")
            return

        if self.gender_input.get().strip() == "":
            messagebox.showerror("ERROR", "gender is Empty")
            return

        interests = []
        for interest in self.interests_input:
            if interest['select'].get() == 1:
                interests.append(interest['value'])
        if len(interests) == 0:
            messagebox.showerror("ERROR", "interests is Empty")
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

        username = self.username_input.get().strip()
        password = self.password_input.get().strip()
        name = self.name_input.get().strip()
        age = int(self.age_input.get().strip())
        gender = self.gender_input.get().strip()
        location = self.location_input.get().strip()
        education = self.education_level_input.get().strip()
        interests = interests
        politics = self.political_orientation_input.get().strip()
        intentions = self.dating_intentions_input.get().strip()
        preferred_genders = preferred_gender
        age_low = int(self.preferred_age_low_input.get().strip())
        age_high = int(self.preferred_age_high_input.get().strip())

        self.page.pack_forget()
        changePage = RegisterNext(self.gui,
                                  username, password, name, age, gender, location, education, interests, politics,
                                  intentions, preferred_genders, age_low, age_high
                                  )
        if self.state == 2:
            changePage.change(self.user)

    def back(self):
        self.page.pack_forget()
        if self.state == 2:
            Menu(self.gui)
        else:
            Login(self.gui)

# next page in registration
class RegisterNext:
    def __init__(self, gui: GUI,
                 username, password, name, age, gender, location, education, interests, politics,
                 intentions, preferred_genders, age_low, age_high):
        self.variables = None
        self.gui = gui
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.education = education
        self.interests = interests
        self.politics = politics
        self.intentions = intentions
        self.preferred_genders = preferred_genders
        self.age_low = age_low
        self.age_high = age_high
        self.init()

        # 2 is change
        self.state = 1
        self.user = None

    def change(self, user: User):
        self.user = user
        self.state = 2

        # insert weights user want
        index = -1
        for variable in self.variables:
            index += 1
            if index + 1 <= len(self.user.weights):
                variable.set(self.user.weights[index])

    def init(self):
        self.page = tkinter.Frame(self.gui.root, width=width, height=height, bg='white')
        self.page.pack()

        self.variables = []

        features = ['Age', 'Interests', 'Location', 'Education', 'Politics', 'Dating Intentions']

        index = -1
        line = -1
        # create features and sliders
        for feature in features:
            line += 1
            index += 1
            label = tkinter.Label(self.page, text=feature)
            label.place(
                width=150,
                height=50,
                x=width * 0.2,
                y=height * 0 + line * 60
            )

            self.variables.append(tkinter.IntVar())

            self.location_input = tkinter.Scale(
                self.page, from_=1, to=10,
                orient=tkinter.HORIZONTAL,
                variable=self.variables[index]
            )
            self.location_input.place(
                width=width * 0.3,
                height=50,
                x=width * 0.4,
                y=height * 0 + line * 60
            )
        # back button to return last page
        submit_btn = tkinter.Button(
            self.page,
            text="Back",
            command=self.back,
        )
        submit_btn.place(
            width=200,
            height=50,
            x=(width - 200) / 2,
            y=height * 0.9 - 60
        )
        # submit button
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
        # save the weights
        weights = []

        for variable in self.variables:
            weights.append(variable.get())
        weights.append(max(weights))
        # create or update user profiles
        if self.state == 2:
            self.user.username = self.username
            self.user.password = self.password
            self.user.name = self.name
            self.user.age = self.age
            self.user.gender = self.gender
            self.user.location = self.location
            self.user.education = self.education
            self.user.interests = self.interests
            self.user.politics = self.politics
            self.user.intentions = self.intentions
            self.user.preferred_genders = self.preferred_genders
            self.user.age_low = self.age_low
            self.user.age_high = self.age_high
            self.user.weights = weights
            if self.gui.store.update_user_info(self.user) == False:
                messagebox.showerror("ERROR", "update ERROR")
            else:
                messagebox.showinfo("SUCCESS", "update SUCCESS")
                self.page.pack_forget()
                Login(self.gui)

        else:
            user: User = self.gui.store.create_user(
                username=self.username,
                password=self.password,
                name=self.name,
                age=self.age,
                gender=self.gender,
                location=self.location,
                education=self.education,
                interests=self.interests,
                politics=self.politics,
                intentions=self.intentions,
                preferred_genders=self.preferred_genders,
                age_low=self.age_low,
                age_high=self.age_high,
                weights=weights
            )

            if self.gui.store.add_user_to_db(user) == False:
                messagebox.showerror("ERROR", "register ERROR")
            else:
                messagebox.showinfo("SUCCESS", "register SUCCESS")
                self.page.pack_forget()
                Login(self.gui)
    # back to last page
    def back(self):
        self.page.pack_forget()
        Register(self.gui).callback(
            self.user,
            self.state,
            self.username, self.password, self.name, self.age, self.gender, self.location,
            self.education, self.interests, self.politics,
            self.intentions, self.preferred_genders, self.age_low, self.age_high
        )

# display homepage
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
            text="Back",
            command=self.back
        )
        like_btn.place(
            width=100,
            height=30,
            x=10,
            y=10
        )

    def reload(self):
        if self.treeview != None:
            for child in self.treeview:
                self.treeview.delete(child)
        else:
            columns = ("name", "age", "gender", "location", "education", "interests", "politics", "intentions")
            self.treeview = Treeview(self.excel_page, show="headings", columns=columns, height=25)

            self.treeview.heading("name", text="name")
            self.treeview.column('name', width=int(width * 0.1))
            self.treeview.heading("age", text="age")
            self.treeview.column('age', width=int(width * 0.05))
            self.treeview.heading("gender", text="gender")
            self.treeview.column('gender', width=int(width * 0.1))
            self.treeview.heading("location", text="location")
            self.treeview.column('location', width=int(width * 0.1))
            self.treeview.heading("education", text="education")
            self.treeview.column('education', width=int(width * 0.1))
            self.treeview.heading("interests", text="interests")
            self.treeview.column('interests', width=int(width * 0.35))
            self.treeview.heading("politics", text="politics")
            self.treeview.column('politics', width=int(width * 0.1))
            self.treeview.heading("intentions", text="intentions")
            self.treeview.column('intentions', width=int(width * 0.1))
            

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
                user['name'],
                user['age'],
                user['gender'],
                user['location'],
                user['education'],
                user['interests'],
                user['politics'],
                user['intentions']
            ))

        self.treeview.pack()

    def back(self):
        self.excel_page.pack_forget()
        self.page.pack_forget()
        Menu(self.gui)

# display matched users profiles
class HomeMatch:
    def __init__(self, gui: GUI, ids):
        self.scrollbar = None
        self.excel_page = None
        self.page = None
        self.gui = gui
        self.treeview = None
        self.ids = ids
        self.init()

    def init(self):
        self.excel_page = tkinter.Frame(self.gui.root, width=width, height=height * 0.8, bg='white')
        self.page = tkinter.Frame(self.gui.root, width=width, height=height * 0.2, bg='white')

        self.excel_page.pack()
        self.page.pack()

        self.reload()

        like_btn = tkinter.Button(
            self.page,
            text="Back",
            command=self.back
        )
        like_btn.place(
            width=100,
            height=30,
            x=10,
            y=10
        )

    def reload(self):
        if self.treeview != None:
            for child in self.treeview:
                self.treeview.delete(child)
        else:
            columns = ("name", "age", "gender", "location", "education", "interests", "politics", "intentions")
            self.treeview = Treeview(self.excel_page, show="headings", columns=columns, height=25)

            self.treeview.heading("name", text="name")
            self.treeview.column('name', width=int(width * 0.1))
            self.treeview.heading("age", text="age")
            self.treeview.column('age', width=int(width * 0.05))
            self.treeview.heading("gender", text="gender")
            self.treeview.column('gender', width=int(width * 0.1))
            self.treeview.heading("location", text="location")
            self.treeview.column('location', width=int(width * 0.1))
            self.treeview.heading("education", text="education")
            self.treeview.column('education', width=int(width * 0.1))
            self.treeview.heading("interests", text="interests")
            self.treeview.column('interests', width=int(width * 0.35))
            self.treeview.heading("politics", text="politics")
            self.treeview.column('politics', width=int(width * 0.1))
            self.treeview.heading("intentions", text="intentions")
            self.treeview.column('intentions', width=int(width * 0.1))

            self.scrollbar = tkinter.Scrollbar(
                self.excel_page,
                orient='vertical',
                command=self.treeview.yview
            )

            self.scrollbar.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
            self.treeview.configure(yscrollcommand=self.scrollbar.set)
        # get all user data and display user we want to show based the id
        users = self.gui.store.get_all_users()
        for index, user in users.iterrows():
            if user['user_id'] in self.ids:
                self.treeview.insert('', 'end', values=(
                user['name'],
                user['age'],
                user['gender'],
                user['location'],
                user['education'],
                user['interests'],
                user['politics'],
                user['intentions']
            ))

        self.treeview.pack()

    def back(self):
        self.excel_page.pack_forget()
        self.page.pack_forget()
        Menu(self.gui)

# display and manage main menu
class Menu:
    def __init__(self, gui: GUI):
        self.page = None
        self.gui = gui
        self.init()

    def init(self):
        self.page = tkinter.Frame(self.gui.root, width=width, height=height, bg='white')
        self.page.pack()
        # get all username and welcome
        name = self.gui.store.get_user_info(self.gui.user_id).name
        image_label = tkinter.Label(self.page, text=f'Welcome {name}! Please select an option from the below menu:', font=("Helvetica", 20), anchor='n', 
                                    width=width,
                                    height=int(height * 0.1))
        image_label.pack()
        # view all user profiles
        like_btn = tkinter.Button(
            self.page,
            text="View all profiles",
            command=self.gotoAll
        )
        like_btn.place(
            width=width * 0.2,
            height=height * 0.1,
            x=width * 0.4,
            y=height * 0.1
        )
        # browse profiles
        like_btn = tkinter.Button(
            self.page,
            text="Browse Profiles",
            command=self.likeAndDislike
        )
        like_btn.place(
            width=width * 0.2,
            height=height * 0.1,
            x=width * 0.4,
            y=height * 0.25
        )
        # view matched user profiles
        show_like_dislike_btn = tkinter.Button(
            self.page,
            text="View Matches",
            command=self.show_like_dislike
        )
        show_like_dislike_btn.place(
            width=width * 0.2,
            height=height * 0.1,
            x=width * 0.4,
            y=height * 0.40
        )
        # logout
        logout_btn = tkinter.Button(
            self.page,
            text="Logout",
            command=self.logout
        )
        logout_btn.place(
            width=width * 0.2,
            height=height * 0.1,
            x=width * 0.4,
            y=height * 0.87
        )
        # delete user profiles
        logout_btn = tkinter.Button(
            self.page,
            text="Delete Profiles",
            command=self.deleteProfiles
        )
        logout_btn.place(
            width=width * 0.2,
            height=height * 0.1,
            x=width * 0.4,
            y=height * 0.55
        )
        # edit user profiles
        logout_btn = tkinter.Button(
            self.page,
            text="Edit Profile",
            command=self.editProfiles
        )
        logout_btn.place(
            width=width * 0.2,
            height=height * 0.1,
            x=width * 0.4,
            y=height * 0.7
        )
    # reload table
    def reload(self):
        if self.treeview != None:
            for child in self.treeview:
                self.treeview.delete(child)
        else:
            columns = ("name", "age", "gender", "location", "education", "interests", "politics", "intentions")
            self.treeview = Treeview(self.excel_page, show="headings", columns=columns, height=25)

            self.treeview.heading("name", text="name")
            self.treeview.column('name', width=int(width * 0.1))
            self.treeview.heading("age", text="age")
            self.treeview.column('age', width=int(width * 0.05))
            self.treeview.heading("gender", text="gender")
            self.treeview.column('gender', width=int(width * 0.1))
            self.treeview.heading("location", text="location")
            self.treeview.column('location', width=int(width * 0.1))
            self.treeview.heading("education", text="education")
            self.treeview.column('education', width=int(width * 0.1))
            self.treeview.heading("interests", text="interests")
            self.treeview.column('interests', width=int(width * 0.35))
            self.treeview.heading("politics", text="politics")
            self.treeview.column('politics', width=int(width * 0.1))
            self.treeview.heading("intentions", text="intentions")
            self.treeview.column('intentions', width=int(width * 0.1))

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
                user['name'],
                user['age'],
                user['gender'],
                user['location'],
                user['education'],
                user['interests'],
                user['politics'],
                user['intentions']
            ))

        self.treeview.pack()

    def show_like_dislike(self):
        like_userids = self.gui.store.evaluate_matches(self.gui.user_id)
        msg = 'user_id is '
        fist = True
        ids = []
        for index, user in like_userids.iterrows():
            if fist is True:
                fist = False
            else:
                msg = msg + ", "
            msg = msg + str(user['user_id'])
            ids.append(user['user_id'])
    
        if fist is True:
            msg = "Empty"
            messagebox.showinfo("See matchs", msg)
            return
        self.page.pack_forget()
        HomeMatch(self.gui, ids)


    def likeAndDislike(self):
        self.page.pack_forget()
        LikeAndDislike(self.gui)

    def logout(self):
        self.page.pack_forget()
        Login(self.gui)

    def browseProfiles(self):
        user = self.gui.store.get_user_info(self.gui.user_id)
        msg = ''
        msg += 'user_id:' + str(user.user_id) + '\n'
        msg += 'username:' + str(user.username) + '\n'
        msg += 'password:' + str(user.password) + '\n'
        msg += 'name:' + str(user.name) + '\n'
        msg += 'age:' + str(user.age) + '\n'
        msg += 'gender:' + str(user.gender) + '\n'
        msg += 'location:' + str(user.location) + '\n'
        msg += 'education:' + str(user.education) + '\n'
        msg += 'interests:' + str(user.interests) + '\n'
        msg += 'politics:' + str(user.politics) + '\n'
        msg += 'intentions:' + str(user.intentions) + '\n'
        msg += 'preferred_genders:' + str(user.preferred_genders) + '\n'
        msg += 'age_low:' + str(user.age_low) + '\n'
        msg += 'age_high:' + str(user.age_high) + '\n'
        msg += 'weights:' + str(user.weights) + '\n'
        messagebox.showinfo("Info", msg)

    def deleteProfiles(self):
        delete = (messagebox.askokcancel('Delete', 'Delete?'))
        if delete:
            self.gui.store.delete_user_from_db(self.gui.user_id)
            self.logout()

    def gotoAll(self):
        self.page.pack_forget()
        Home(self.gui)

    def editProfiles(self):
        user = self.gui.store.get_user_info(self.gui.user_id)
        self.page.pack_forget()
        Register(self.gui).change(user)


def start():
    root = tkinter.Tk()
    store = user_management_new()
    gui = GUI(root, store)
    Login(gui)
    # Menu(gui)
    # RegisterNext(
    #     gui,
    #     None, None, None, None, None,
    #     None, None, None, None, None, None,
    #     None, None,
    # )
    root.mainloop()


if __name__ == '__main__':
    start()
