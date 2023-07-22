import streamlit as st

# Set page title
st.title("My Streamlit App")

# Create a sidebar
st.sidebar.header("Sidebar")

# Add content to the sidebar
st.sidebar.subheader("Options")
option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

# Add content to the main area
st.subheader("Main Area")
st.write(f"You selected: {option}")

# Add a button
if st.button("Click Me"):
    st.write("Button clicked!")
