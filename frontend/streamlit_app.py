# frontend/streamlit_app.py
import streamlit as st
import sys
sys.path.append("..")  # Add the parent directory to the sys.path
from backend.text_extraction import process_uploaded_file

def main():
    st.title("Question Paper Examination Tool")

    # Sidebar for uploading PDF and images
    uploaded_file = st.sidebar.file_uploader("Upload PDF or Image File", type=["pdf", "jpg", "jpeg", "png"])

    # Main area for user input
    st.header("User Input")
    user_input = st.text_input("Enter your question:")

    # Separate buttons for processing PDF and taking user input after processing
    with st.sidebar:
        if st.button("Process File") and uploaded_file:
            with st.spinner("Processing file..."):

                # st.write(f"Processing file: {uploaded_file.name}")

                # Process uploaded file using the backend
                extracted_text = process_uploaded_file(uploaded_file)

                st.write("Text extracted:")
                st.write(extracted_text)
                
            # Display success message after processing
            st.success("File uploaded successfully!")


    if st.button("Submit User Query") and user_input:
        st.write(f"Processing user input: {user_input}")
        # Add user input processing logic in llm

if __name__ == "__main__":
    main()
