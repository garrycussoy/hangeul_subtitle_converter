# Import django related tools
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Import youtube API
from youtube_transcript_api import YouTubeTranscriptApi

# Import converter module
from korean_romanizer.romanizer import Romanizer

# Import other needed modules
from urllib.parse import urlparse, parse_qs

"""
Following function will take youtube video URL and extract the video ID from it.
If it's not in full format, then this function will return the string as is (assuming that user pass in an video ID instead of full URL).
"""
def get_video_id(url):
  """
  Examples of youtube URL video that will be covered in this function:
  - http://youtu.be/CGnc553-ttg
  - http://www.youtube.com/watch?v=CGnc553-ttg&feature=feedu
  - http://www.youtube.com/embed/CGnc553-ttg
  - http://www.youtube.com/v/CGnc553-ttg?version=3&amp;hl=en_US
  """

  # Extract video ID from many variations of youtube video URL
  query = urlparse(url)
  if query.hostname == 'youtu.be':
    return query.path[1:]
  if query.hostname in ('www.youtube.com', 'youtube.com'):
    if query.path == '/watch':
      p = parse_qs(query.query)
      return p['v'][0]
    if query.path[:7] == '/embed/':
      return query.path.split('/')[2]
    if query.path[:3] == '/v/':
      return query.path.split('/')[2]

  # Case when it has been a video ID
  return url

"""
Following function will get Hangeul subtitle based on a given youtube video URL.
It can take full youtube URL or just the ID of the video.
This function then will return a list contains pairs of Hangeul subtitle and the time when it appears on the video.

"""
def get_transcript(url):
  # Prepare response
  response = {
    'status': '',
    'message': '',
    'detail': []
  }

  # Extract video ID
  vid_id = get_video_id(url)

  # Check whether the video exists or not
  try:
    YouTubeTranscriptApi.list_transcripts(vid_id)
  except:
    response['status'] = 'FAILED'
    response['message'] = 'The video with ID ' + vid_id + ' doesn\'t exist'
    return response
  
  # Try to fetch Hangeul subtitle
  try:
    transcript = YouTubeTranscriptApi.get_transcript(vid_id, languages = ['ko'])
    response['status'] = 'SUCCESS'
    response['message'] = 'Success fetching Hangeul subtitle'
    response['detail'] = transcript
    return response
  except:
    response['status'] = 'FAILED'
    response['message'] = 'The video with ID ' + vid_id + ' doesn\'t have Hangeul subtitle'
    return response

"""
Following function will convert Hangeul subtitle into Korean Romanization subtitle.
It takes detail field from get_transacipt function's response.
"""
def hangeul_to_romanization(transcript):
  # Convert each text in the list
  for sub in transcript:
    sub['text'] = Romanizer(sub['text']).romanize()
  
  return transcript
