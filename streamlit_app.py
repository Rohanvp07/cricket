import streamlit as st

# Set the title of the application
#st.title("Fullscreen iFrame Stream")

# Embed the iframe HTML code directly into Streamlit using markdown
iframe_code = """
    <iframe src='https://embedsports.me/cricket-world-cup/icc-champions-trophy-final-india-vs-new-zealand-stream-2'
            allowfullscreen="true" allowtransparency="true" 
            width="100%" height="100%" frameborder="0">
    </iframe>
"""

# Display the iframe in the Streamlit app using markdown with raw HTML
st.markdown(iframe_code, unsafe_allow_html=True)
