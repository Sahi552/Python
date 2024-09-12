from pytube import YouTube
video = YouTube('https://youtu.be/G4v_fqNPsAA?si=X0kMhzFDnjnkj-tj')
highresvid = video.streams.get_highest_resolution()
highresvid.download()
print("done")