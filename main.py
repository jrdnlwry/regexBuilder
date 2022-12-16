import streamlit as st
import streamlit.components.v1 as components
import re


header = st.container()
explanation = st.container()
model = st.container()
cta = st.container()

# hide the hamburger menu

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# H1 Project Title Simple Regex Builder for Google Suite

with header:
    st.title('Super Simple Regex Builder')
    st.subheader('for the Google Marketing Platform.')

# text explanation on how to use it
with explanation:
    st.subheader("How to use the app:")
    st.markdown('Step 1. Select your TLD extension for your domain')
    st.markdown('Step 2. Review and confirm you selected the right extension')
    st.markdown('Step 3. Input your URLs')
    st.markdown('Step 4. Copy the regex output from the tool')
    st.markdown('Step 5. Enjoy! :)')


# model and return regex string to use

# Code that takes a list of URLs and a branded domain name to generate regex code

# need to update code to accept a user pasted input

def regex_generator():

  u_list = []
  
  tld = st.text_input("Please type your TLD extension: ")
  
  # prompt one domain input
  # prompt two sub domain input
  #domain = st.text_input("Input the domain with no trailing slash:", 'https://example.com')
  #subDomain = st.text_input("Input the sub domain with no trailing slash:", 'https://example.com')
  
  url = st.text_input("Input the URLs to build the regex (space separated): ", '/page-path/')
  # split the string inputs by whitespace & convert to list
  urls = list(url.split(" "))
  for url in urls:
    i = re.sub(f".*\{tld}",'',url)
    u_syntax = ".\*" + i + ".\*"
    u_list.append(u_syntax)

    r_syntax = '|'.join(u_list)  
  
  return r_syntax


# output the model
with model:
    st.write("Copy the below to use in your dashboard:`")
    try:
        st.write(regex_generator())
    except:
        print()



# footer section

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with 💪 by <a style='display: block; text-align: center;' href="https://tatelowry.com/?utm_source=regexBuilder" target="_blank">Jordan Lowry</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
