# ---------- Hangeul Subtitle Converter ----------
*** Created By : Garry Ariel ***

# Description
The aim of this project is to create a website which will display youtube videos with Korean Romanization subtitle by replacing existing Hangeul subtitle. This will work as follows.
1. User input youtube video URL with existing Hangeul subtitle (Hangeul subtitle should be provided by author of the video, not automaticlly generated by youtube).
2. The app will get the Hangeul subtitle.
3. The app will convert that Hangeul subtitle into Korean Romanization subtitle.
4. When user play the video, the app will overwrite Hangeul subtitle by Korean Romanization subtitle.

# Technology Stack
This project use Django framework and two main modules, which are:
1. [Youtube Transcript API] (https://pypi.org/project/youtube-transcript-api/)
2. [Hangeul to Korean Romanization Converter] (https://github.com/osori/korean-romanizer)

# TODO List
1. Create a function to download the subtitle.
2. Create a function to convert the subtitle.
3. Create UI for the website.
4. Show the new subtitle on the video while user play it (user cannot pause or jump into random time while playing the video).
5. User can pause or jump into any random of time while playing the video.
6. Deploy it on Netlify and release version 1.0.
