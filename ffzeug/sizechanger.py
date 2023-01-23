# import ffmpeg 
import ffmpeg
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# print the size of the EXPAND.webm
path_to_file = "c:\\Users\\Flori\\Desktop\\pypy\\ffzeug\\luca.webm"
folder = "c:\\Users\\Flori\\Desktop\\pypy\\ffzeug\\"
# split the video into two parts
# start time = half of the video length
video_length = float(ffmpeg.probe(path_to_file)["streams"][1]["tags"]["DURATION"].split(":")[-1])
start_time = video_length / 2
end_time = video_length

print("video length: " + str(video_length))
print("start time: " + str(start_time))
print("end time: " + str(end_time))

i = 0
#ffmpeg_extract_subclip(path_to_file, start_time, end_time, targetname=folder + "luca" +str(i)+".webm")
i += 1
#ffmpeg_extract_subclip(path_to_file, 0, start_time, targetname=folder + "luca" +str(i)+".webm")

# get the video stream 
stream1 = ffmpeg.input(folder + "luca0.webm")
stream2 = ffmpeg.input(folder + "luca1.webm")
# concat the two parts
ffmpeg.concat(stream1, stream2 , v=1, a=1, vcodec='copy', acodec='copy', r=25, s=1, n=folder + "luca3.webm")

