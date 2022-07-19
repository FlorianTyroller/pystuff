from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
start_time = 1.5
end_time = 2
ffmpeg_extract_subclip("s.webm", start_time, end_time, targetname="sss.webm")


# concat:    ffmpeg -f concat -i mylist.txt -c copy movesO.webm
# get size: ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 s.webm
# sclae up: ffmpeg -i moves3.webm -vf "scale=1280:720" moves4.webm