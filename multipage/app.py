import streamlit as st
from pag1 import main as  pag1
from pag2 import main as  pag2
from pag3 import main as  pag3
#from pagxx import main as pagxx

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://w.wallhaven.cc/full/nr/wallhaven-nr6xmn.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


def main():
	################ load image from web #########################
	# from PIL import Image
	# import requests
	# from io import BytesIO
	# url='https://frenzy86.s3.eu-west-2.amazonaws.com/python/swear.png'
	# response = requests.get(url)
	# image = Image.open(BytesIO(response.content))
	# st.title("My multipage APP")
	# st.image(image, caption='',use_column_width=True)

				
	pag_name = ["Classificazione Iris","EDA pinguini","pag3"]
	
	OPTIONS = pag_name
	sim_selection = st.sidebar.selectbox('Seleziona la pagina', OPTIONS)

	if sim_selection == pag_name[0]:
		pag1()
	elif sim_selection == pag_name[1]:
		pag2()
	elif sim_selection == pag_name[2]:
		pag3()
	else:
		st.markdown("Something went wrong. We are looking into it.")

	add_bg_from_url()
if __name__ == '__main__':
	main()