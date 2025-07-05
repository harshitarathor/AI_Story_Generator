import streamlit as st
from transformers import pipeline, set_seed

# Set Streamlit page config
st.set_page_config(page_title="AI Story Generator", page_icon="📖")

# Custom CSS for beautiful background and styling
st.markdown("""
    <style>
    /* Full app background with soft blue gradient */
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #2a5298, #a1c4fd);
        background-attachment: fixed;
        color: white;
        padding: 2rem;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Text input box styling */
    textarea {
        background-color: rgba(0, 0, 0, 0.3) !important;
        color: white !important;
        font-size: 16px !important;
        border-radius: 6px;
    }

    /* Button styling */
    .stButton button {
        background-color: #ffffff;
        color: #1e3c72;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-size: 16px;
        transition: all 0.3s ease-in-out;
        border: none;
    }

    .stButton button:hover {
        background-color: #2a5298;
        color: white;
        transform: scale(1.05);
    }

    /* Subheader text */
    .stMarkdown h2 {
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.title("📖 AI Story Generator")
st.write("Enter a creative prompt and let AI continue the story!")

# Prompt input
prompt = st.text_area("Your story prompt:", "Once upon a time in a faraway land,")

# Generate story on button click
if st.button("Generate Story"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt!")
    else:
        with st.spinner("Generating story..."):
            # Load GPT-2 model
            generator = pipeline('text-generation', model='gpt2')
            set_seed(42)

            # Generate text
            result = generator(prompt, max_length=100, num_return_sequences=1)
            story = result[0]['generated_text']

            # Display result
            st.subheader("Generated Story:")
            st.write(story)
