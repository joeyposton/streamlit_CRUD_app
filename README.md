
# CRUD App with SQLite and Streamlit

This is a simple CRUD (Create, Read, Update, Delete) web application built using Streamlit and SQLite. It allows users to perform CRUD operations on a SQLite database through a web interface.

## Features

- **Create**: Add a new name to the database.
- **Read**: View a specific entry based on its ID.
- **Update**: Modify an existing entry based on its ID.
- **Delete**: Remove an entry from the database based on its ID.
- **View All Data**: See all entries in the database at once.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python
- Streamlit
- SQLite
- Pandas

You can install the necessary packages using pip:

```bash
pip install –r requirements.txt
```

### Running the App

To run the app, navigate to the directory containing the script and execute:

```bash
streamlit run your_script_name.py
```

Replace `your_script_name.py` with the name you saved the provided code under.

## Usage

1. Choose the desired action (Create, Read, Update, Delete) from the dropdown menu.
2. For Create:
    - Enter the name you want to add.
    - Click the "Add" button.
3. For Read:
    - Enter the ID of the entry you want to view.
    - Click the "Read" button.
4. For Update:
    - Enter the ID of the entry you want to modify.
    - Enter the new name.
    - Click the "Update" button.
5. For Delete:
    - Enter the ID of the entry you want to remove.
    - Click the "Delete" button.
6. Scroll down to view all entries in the database.

## Database Structure

The SQLite database (`data.db`) contains a table named `data` with the following columns:

- `id`: A unique identifier for each entry (Integer, Primary Key).
- `name`: The name associated with the entry (Text).

## Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open source. Feel free to use and modify, but please give credit where it's due.
