import streamlit as st
import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")
conn.commit()

def create_entry(name):
    cursor.execute("INSERT INTO data (name) VALUES (?)", (name,))
    conn.commit()

def read_entries_as_df():
    return pd.read_sql_query("SELECT * FROM data", conn)

def update_entry(id, new_name):
    cursor.execute("UPDATE data SET name = ? WHERE id = ?", (new_name, id))
    conn.commit()

def delete_entry(id):
    cursor.execute("DELETE FROM data WHERE id = ?", (id,))
    conn.commit()

st.title("CRUD app with SQLite")

st.write('This is a simple CRUD (Create, Read, Update, Delete) web application built using Streamlit and SQLite. It allows users to perform CRUD operations on a SQLite database through a web interface.')

st.write('---')

action = st.selectbox("Choose action", ["Create", "Read", "Update", "Delete"])

if action == "Create":
    name = st.text_input("Enter a name to add to the database")
    if st.button("Add"):
        create_entry(name)
        st.success(f"Added {name} to the database!")

elif action == "Update":
    id = st.number_input("Enter the ID of the entry you want to update", min_value=1, value=1, step=1)
    new_name = st.text_input("Enter the new name")
    if st.button("Update"):
        update_entry(id, new_name)
        st.success(f"Updated ID {id} to {new_name}!")

elif action == "Delete":
    id = st.number_input("Enter the ID of the entry you want to delete", min_value=1, value=1, step=1)
    if st.button("Delete"):
        delete_entry(id)
        st.success(f"Deleted entry with ID {id}!")

elif action == "Read":
    id = st.number_input("Enter the ID of the entry you want to read", min_value=1, value=1, step=1)
    if st.button("Read"):
        df = read_entries_as_df()
        st.dataframe(df[df["id"] == id])

st.write('---')

st.write('All Data:')

# Display the table as a dataframe
df = read_entries_as_df()
st.dataframe(df)
