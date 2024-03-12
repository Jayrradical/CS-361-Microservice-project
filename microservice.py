import time
import os

def get_last_processed_line_number():
    try:
        with open("last_line.txt", "r") as file:
            return int(file.read().strip() or 0)
    except FileNotFoundError:
        return 0

def update_last_processed_line_number(line_number):
    with open("last_line.txt", "w") as file:
        file.write(str(line_number))

def process_commands(starting_line=0):
    line_number = 0
    new_lines = []
    with open("input.txt", "r") as input_file:
        for line_number, line in enumerate(input_file, 1):
            if line_number > starting_line:
                new_lines.append(line.strip())

    if new_lines:
        with open("output.txt", 'a') as output_file:
            for line in new_lines:
                if "get spotify" in line:
                    print("Input received for Spotify.")
                    output_file.write("Link to Spotify for artists: https://artists.spotify.com/home?ref=logo\n")
                if "get soundcloud" in line:
                    print("Input received for SoundCloud.")
                    output_file.write("Link to SoundCloud upload: https://soundcloud.com/upload\n")
                if "get apple music" in line:
                    print("Input received for Apple Music.")
                    output_file.write("Link to Apple Music for artists: https://artists.apple.com/support/1108-get-your-next-release-on-apple-music\n")
                if "get pandora" in line:
                    print("Input received for Pandora.")
                    output_file.write("Link to Pandora: https://help.pandora.com/s/article/Information-for-Artists-Submitting-to-Pandora-1519949298669?language=en_US\n")
                if "get tidal" in line:
                    print("Input received for Tidal.")
                    output_file.write("Link for artists to Tidal: https://tidal.com/forartists\n")
                if "get youtube music" in line:
                    print("Input received for YouTube Music.")
                    output_file.write("Link to YouTube Music for artists: https://support.google.com/youtubemusic/answer/9716522?hl=en\n")
                    

    # Update the last processed line number
    if line_number >= 0:
        update_last_processed_line_number(line_number)

while True:
    time.sleep(1)  # Check for new input every second
    last_processed_line_number = get_last_processed_line_number()
    process_commands(last_processed_line_number)
