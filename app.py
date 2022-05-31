import streamlit as st

from bbquote.lib import get_quote

quote = get_quote()  # assuming the function returns an author and a quote

st.write(quote)
print(f"{quote}")
