import streamlit as st

st.set_page_config(page_title="Sparking Stars", layout="wide", page_icon="✨")

if __name__ == "__main__":
    st.sidebar.title("Sparking Stars")
    video_url = "/Users/ronny/Downloads/videoplayback.mp4"
    video_html = """
        <video autoplay muted loop id="myVideo">
          <source src="https://www.youtube.com/watch?v=E0EyWtsnPns">
        </video>
    """

    st.markdown(video_html, unsafe_allow_html=True)
    st.title('Video page')

    st.markdown("This text is written on top of the background video! 😁")
