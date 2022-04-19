from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
start_time = 0
end_time = 5
ffmpeg_extract_subclip("tobi_clip.mp4", start_time, end_time, targetname="clip.mp4")