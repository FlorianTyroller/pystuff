# open the midi file
from mido import MidiFile

mid = MidiFile('osustuff/paragon.midi')


for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    c = 0
    r = 0
    for msg in track:
        # if the velocity is less than 60 remove the msg from the track
        try:
            if msg.velocity < 90:
                track.remove(msg)
                r += 1
        except:
            pass
        c += 1
        if c % 1000 == 0:
            print(c,r)
    
    track.save('osustuff/paragon2.midi')
        