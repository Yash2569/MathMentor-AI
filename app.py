
import streamlit as st

st.set_page_config(
    page_title="MathMentor AI",
    page_icon="📐",
    layout="centered"
)

st.title("📐 MathMentor AI")

st.subheader("Your personal mathematics tutor")

st.markdown(
    """
    Upload a mathematical problem and let MathMentor
    help you understand it through detailed explanations.
    
    **From Class 1 to Class 10 and beyond.**
    """
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload your mathematics problem",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    st.image(
        uploaded_file,
        caption="Your uploaded mathematics problem",
        use_container_width=True
    )

    st.success("Image uploaded successfully!")

    st.info(
        "Our mathematical analysis engine "
        "will be available in the next development stage."
    )
