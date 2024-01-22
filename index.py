import streamlit as st
st.set_page_config(page_title="Joe's baller burgers", page_icon="🍔", initial_sidebar_state="expanded")
st.title("Joe's baller burgers")
burgers_str = st.text_input("How many burgers do you want? Each burger is 5.50$.")
xcc = st.radio("do you want extra cheese on your burgers? (25 cents extra per burger)", ["no", "yes"])
if xcc == "no":
    xc = 0
else:
    xc = .25
hotdogs_str = st.text_input("How many hotdogs do you want? Each burger is 2.25$.")
tip = st.slider("How much do you want to tip?", 0.0, 100.0, 2.0,step=0.1,format="$%.2f")
burgers = int(burgers_str) if burgers_str.isdigit() else 0
hotdogs = int(hotdogs_str) if hotdogs_str.isdigit() else 0
bc = burgers * (5.50 + xc)
hc = hotdogs * 2.25
st.write(f"Number of burgers: {burgers}")
st.write(f"Number of hotdogs: {hotdogs}")
st.write(f"Cost of burgers: ${bc:.2f}")
st.write(f"Cost of hotdogs: ${hc:.2f}")
st.write(f"Cost of tip: ${tip:.2f}")
st.write(f"Total Cost: ${bc+hc+tip:.2f}")