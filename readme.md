

## Project Overview
**Two-way Street** is a dating/matching app developed by Team 9. This program utilizes SQLite databases and Object-Oriented Programming (OOP) throughout. While command line interfaces can be used to access full functionality, a fully functioning user-friendly GUI is also included.

Users are ranked with each other based on several factors and are matched when both users have “liked” each other.

## Installation

1. **Download the entire repository** and place it in your desired folder.
2. **Prerequisite**: Python 3.x
3. **Required Packages**: requirements.txt

### Files

- **`main_new.py`**: This is the main program file that integrates all other files. It contains the core program and functions that prompt user input while leveraging functions from other classes such as `user_management_new` and `user`. It also includes the algorithm used for our matching mechanism. This file is later used by `GUI.py` to produce the user interface for the program.

- **`GUI.py`**: This file contains all the necessary code to produce a graphical user interface. It utilizes the Python library Tkinter and is based solely on the logic, algorithm, and program contained in `Main_new.py`.

- **`user_management_new.py`**: This file primarily manages the user database. It contains all the necessary code to connect Python with SQLite, such as establishing user tables, as well as functions to create, edit, delete, and update user records.

- **`User.py`**: This file sets up the necessary information needed for a user profile, which will be used later in other classes.

- **`matching_helpers.py`**: This file includes two functions that are used to calculate the interest score and the age score for our matching algorithm.

- **`test_create_users.py`**: This file contains code to quickly create up to 20(changeable) random users for testing purposes.

## Usage

### 2.1 Running the Program

After downloading the repository, you can:

- Run the main_new.py file
  - **Run the GUI**: Type `gui` in the main_new program
  - **Use the command line**: Interact with the command line prompts in the main_new program
    
### 2.2 User Manual/GUI

#### 2.2.1 Managing Account

- **Creating Account/Registering**:
  - As the GUI prompts, enter the necessary info, such as username, password, etc. Click "Next" and select custom weights from 1 to 10, which represent how much you value certain factors. Click "Submit" to complete the process.

- **Edit Account**:
  - After logging in, click the "Edit" button to edit your demographic information and weights.

- **Login/Logout**:
  - **Login**: Enter your user ID and password.
  - **Logout**: After logging in, click the "Logout" button.

- **Delete Account**:
  - After logging in, click the "Delete" button, follow the prompt, and click "Y" to delete the account.

#### 2.2.2 Likes/Dislikes/Match

- After logging in, click on the "Browse Profile" button to like/dislike user profiles.

## Additional Documentation

### 4.1 Matching Algorithm

Our matching algorithm utilizes a compound compatibility score that considers a total of 7 factors: age preferences, common interests, geographic location, education level, political views, and dating intentions. These factors are assigned weights by the user or set to default weights and are used to rank and push profiles to the user.

### 4.2 SQLite Databases

We have established 3 tables in our SQLite database:
- **`users`**: Stores user-related information such as user ID, interests, etc.
- **`likes`** and **`dislikes`**: These tables record interactions between users and are used in the matching process.

### 4.3 Calculating Distance

Due to slow real-time processing caused by the OpenCage API, we use a dictionary of location and distance obtained via OpenCage API, stored in a JSON file for calculating distances in the algorithm.
