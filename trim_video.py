from moviepy.video.io.VideoFileClip import VideoFileClip

# Path to the input video file
input_path = "Practical_Task.mp4"

# Path to the output video file
output_path = "output_video.mp4"

# Open the video file
clip = VideoFileClip(input_path)

# Trim the video (e.g., from 10 seconds to 20 seconds)
start_time = 0  # in seconds
end_time = 43    # in seconds
trimmed_clip = clip.subclip(start_time, end_time)

# Save the trimmed clip
trimmed_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

print("The video has been successfully trimmed!")
