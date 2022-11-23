import random
import streamlit
from PIL import Image
streamlit.title("David's Website")
streamlit.subheader("This is basically where I just link my other projects")
tab1, tab2, tab3, tab4, tab5 = streamlit.tabs(["League 1v1 Maker", "WC Predictions", "Info", "3D Object Code", "Project Poker"])
with tab1:
    streamlit.subheader("League 1v1 Generator Thing")
    streamlit.success("See it here : https://davidadroit-leagueonevone-leagueapp-oh25hy.streamlit.app/")
    streamlit.text("IMPORTANT: Decide who is player A and player B before clicking generate")
    image2 = Image.open('growing_flower.png')
    streamlit.image(image2, caption='Flower I created on pov-ray')

with tab2:
    streamlit.subheader("World Cup Predictions Thing")
    streamlit.success("See it here : https://davidadroit-world-cup-personalproject2-i0jds3.streamlit.app/")
with tab3:
    streamlit.text("I'm a 22 year old CS student in my senior year.")
    streamlit.text("I am in the Greater Boston Area")
    streamlit.text("This is basically just where I test and put my webapps I'm making")
    streamlit.info("Discord : airpodenjoyer#9126")
    streamlit.info("IG: @davidmeltsyou")
    streamlit.info("Hive : @davidx")
    streamlit.info("Github : @davidAdroit")
    image = Image.open('backgroundimage.jpg')
    streamlit.image(image, caption='')
with tab4:
    streamlit.subheader("Pov-Ray Stuff")
    image3 = Image.open('3dcode_1.png')
    streamlit.image(image3, caption='code to the rose seen on the first page')
    streamlit.text('-------------------------------------------------------')
    image4 = Image.open('3dcode_2.png')
    streamlit.image(image4, caption ='code to rose scaled to normal size then falling over, animation over 1 second')
    
    


