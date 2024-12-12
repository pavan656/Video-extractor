import streamlit as st 
from streamlit_option_menu import option_menu
from moviepy.editor  import VideoFileClip
import os
import shutil

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.sidebar:
            selected = option_menu(
                menu_title="Menu",  
                options=["Extractor", "About", "Contact Us",],  
                icons=["camera","book", "envelope",],  
                menu_icon="cast",  
                default_index=0,  
            )

if selected == "Extractor":
    
    st.markdown(
    "<h1 style='font-size: 5em;text-align: center; border: solid #2B1B3D; border-radius: 10px;'>Audio Extractor</h1>",
    unsafe_allow_html=True,
    )
    st.write("")
    st.write("")
    st.write(
        """	📺 A Video to Audio Extractor is a software or tool designed to convert the audio track from video files into standalone audio formats such as MP3, WAV, or AAC. It's ideal for creating music playlists, extracting sound effects, or saving lectures, podcasts, or voiceovers for offline use. With features like batch processing, high-quality output, and support for various video formats (e.g., MP4, AVI, MOV), these tools are user-friendly and efficient."""
    )

    st.write("---")

    st.write("## 📂 Choose an video file")


    video = st.file_uploader("",type=["mp3","mp4","mov"])
    save_path =""
    if not os.path.exists("download_video"):
        os.makedirs("download_video")

    if video is not None :
        st.write("please wait a moment")
        save_path = os.path.join("download_video",video.name)
        with open(save_path,"wb") as file : 
            shutil.copyfileobj(video,file)
    
    try : 
        audio_file_path = "download_video/extraction_audio.mp3"
        movie_video = VideoFileClip(save_path)
        audio = movie_video.audio
        audio_file = audio.write_audiofile(audio_file_path) 

        with open(audio_file_path,'rb') as folder :
            st.audio(folder,format='audio/mp3')

        with open(audio_file_path,'rb') as folder :
            st.write("---")

            st.write("## 📥 Download your export file")

            st.write("")

            st.download_button(
                          label='Download file',
                           data=folder,
                           file_name="extracted_audio.mp3",
                           mime="audio/mp3")
    except Exception as e :
        st.write('')


if selected == "About":
    st.markdown(
    "<h1 style='font-size: 5em;text-align: center; border: solid #2B1B3D; border-radius: 10px;'>About</h1>",
    unsafe_allow_html=True,
    )
    st.write("")
    st.write("---")
    st.write("")
    st.write("## 📽️ Audio Extractor : ")
    st.write("##### The Audio Extractor app is a versatile and user-friendly tool designed to help you extract audio from videos with ease. Whether you’re a content creator, a music enthusiast, or someone looking to save the audio from memorable moments in videos, this app simplifies the process and delivers high-quality audio outputs tailored to your needs.")
    st.write("#### 🗒️ Troubleshooting Common Issues :")
    st.write("##### 1 .Audio Quality Issues ")
    st.write(" ##### Solution: Ensure the original video has high-quality audio. Use the app’s advanced settings to adjust the bitrate or choose a lossless format like WAV for better quality.")
    st.write("##### 2 .Unsupported File Formats ")
    st.write(" ##### Solution: Convert the video to a supported format using a compatible video converter or ensure your app is updated to support the latest formats.")
    st.write("##### 3 .Incomplete Audio Files ")
    st.write(" ##### Solution: Check if the original video file is intact and not corrupted. Use the app’s trimming tool to manually verify the extracted duration.")
    st.write("---")


if selected == "Contact Us":
    st.markdown(
    "<h1 style='font-size: 5em;text-align: center; border: solid #2B1B3D; border-radius: 10px;'>Contact Us</h1>",
    unsafe_allow_html=True,
    )
    st.write("")
    st.write("---")
    st.header(":mailbox: Get In Touch With Us..!")
    st.write("")

    contact_form = """
        <form action="https://formsubmit.co/pavan.s.diwakar@gmail.com" method="POST">
            <input type="hidden" name="_autoresponse" value="Your Message has been recorded.">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Details about the issue"></textarea>
            <button type="submit">Send</button>
        </form>
        """
    
    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
         with open(file_name) as f:
              st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    local_css("assets/style.css")


     
    