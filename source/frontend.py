import streamlit as st
from backend import (create_user, validate_user, get_parks, get_park_details, add_review, 
                    add_park, delete_park, modify_park, delete_user, delete_review, is_admin)


# ---------------------------
# Section 1: Signup / Signin Page
# ---------------------------

def display_auth_page():
    st.title("Authentication")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if create_user(username, password):
            st.success("User created successfully.")
            st.session_state['current_page'] = 'parks'  # Direct to parks page after signup
        else:
            st.error("Username already exists. Try another.")

    if st.button("Sign In"):
        if validate_user(username, password):
            st.session_state['logged_in'] = True  # Update logged_in state
            if is_admin(username):
                st.session_state['is_admin'] = True
                st.session_state['current_page'] = 'admin'  # Direct to admin page
            else:
                st.session_state['is_admin'] = False
                st.session_state['current_page'] = 'parks'  # Direct to parks page
        else:
            st.error("Invalid username or password.")


# ---------------------------
# Section 2: Parks List Page
# ---------------------------

def display_parks_page():
    st.title("Parks")
    parks = get_parks()
    for park in parks:
        # Define columns with spacers for dividers
        col1, spacer1, col2, spacer2, col3, spacer3, col4 = st.columns([2, 0.1, 1, 0.1, 4, 0.1, 2])
        
        with col1:
            st.subheader(park[3])  # Name of the park

        with col2:
            st.write(park[2])  # Location of the park

        with col3:
            # Ratings
            st.write(f"Overall: {park[6]}/5   Hiking: {park[5]}/5   Camping: {park[4]}/5")
        
        with col4:
            if st.button("View", key=str(park[0])):
                st.session_state['current_page'] = 'single_park'
                st.session_state['selected_park_id'] = park[0]

        # Optionally, you can add a horizontal line after each park's info
        st.markdown("---")

        
        
        # if st.button("View", key=park['park_id']):
        #     display_park_page(park['park_id'])

# ---------------------------
# Section 3: Single Park Page
# ---------------------------

def display_park_page(park_id):
    park_details = get_park_details(park_id)
    st.title(park_details[3])
    st.write("Location:", park_details[2])
    st.write("Description:", park_details[1])
    # Display reviews
    # Add review functionality
    

# ---------------------------
# Section 4: Admin Page
# ---------------------------

def display_admin_page():
    st.title("Admin Dashboard")
    # Admin functionalities to manage parks, users, and reviews
    # ...

def main():
    # Initialize current_page in session_state
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'auth'

    # Display the appropriate page based on current_page
    if st.session_state['current_page'] == 'auth':
        display_auth_page()
    elif st.session_state['current_page'] == 'parks':
        display_parks_page()
    elif st.session_state['current_page'] == 'admin':
        display_admin_page()
    elif st.session_state['current_page'] == 'single_park':
        display_park_page(st.session_state['selected_park_id'])


if __name__ == "__main__":
    main()
