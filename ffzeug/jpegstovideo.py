import ffmpeg
input_folder = "c:/Users/Flori/Desktop/pypy/ffzeug/jpegs/"

(
    ffmpeg
    .input(input_folder + "*.jpg", pattern_type='glop', framerate=25)
    .output(input_folder + 'movie.mp4')
    .run()
)