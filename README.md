# Simple CRUD App with NiceGUI, Pydantic, and MongoDB

This is a straightforward CRUD (Create, Read, Update, Delete) application constructed using various technologies to streamline data management.

## Technologies Used

- **Pydantic**: Employs Pydantic for data validation, ensuring the integrity of the managed data.
- **NiceGUI**: Incorporates NiceGUI to create a user-friendly interface, enhancing the user experience.
- **MongoDB**: Utilizes MongoDB as the database to store and manage the application's data.
- **FastAPI**: Utilizes FastAPI to build a robust and efficient REST API for managing data operations.

## Features

- **CRUD Operations**: Provides functionalities for creating, reading, updating, and deleting data.
- **Data Validation**: Ensures the validation of data integrity using Pydantic.
- **Database Integration**: Stores and manages data within a MongoDB database.
- **REST API**: Employs FastAPI to build a performant and intuitive API for interacting with the application's data.

## License

This project is open and freely available for reuse under the [MIT License](https://opensource.org/licenses/MIT).

## Cloning Project

Here's a set of commands you can run in your terminal or command prompt to set up a virtual environment, activate it, and install the required dependencies for the project:

```bash
# Create a virtual environment named 'crud'
python3 -m venv crud

# Activate the virtual environment (for Unix-based systems)
source crud/bin/activate

# Activate the virtual environment (for Windows)
# .\crud\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install project dependencies from requirements.txt
pip install -r requirements.txt
```

These commands will:

1. Create a virtual environment named 'crud'.
2. Activate the virtual environment.
3. Upgrade `pip` within the virtual environment to the latest version.
4. Install the necessary dependencies listed in the `requirements.txt` file for the project.

This setup isolates the project dependencies within the virtual environment, ensuring they don't conflict with other projects or the system-wide Python installation. Adjust the commands as needed for your specific environment and operating system.
