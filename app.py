import streamlit as st
st.title("Book Recommendation System")
st.write("Search for a book to get recommendations based on your choice.")

# Input for the book title
book_title = st.text_input("Enter a book title", "")

if book_title:
    # Display recommendations if a title is entered
    recommendations = recommend(book_title, n_values=10)
    st.write("Recommended Books:")
    for rec in recommendations:
        st.write(f"- {rec}")