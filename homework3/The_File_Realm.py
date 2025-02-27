# Dictionary of liked songs (title: artist)
liked_songs = {
    'Bad Habits': 'Ed Sheeran',
    "I'm Just Ken": 'Ryan Gosling',
    'Mastermind': 'Taylor Swift',
    'Uptown Funk': 'Mark Ronson ft. Bruno Mars',
    'Ghost': 'Justin Bieber'
}

# Function to write liked songs to a file
def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        file.write("Liked Songs:\n")
        for title, artist in liked_songs.items():
            file.write(f"{title} by {artist}\n")

# Write to liked_songs.txt
write_liked_songs_to_file(liked_songs, 'liked_songs.txt')

# Read and print the file contents
with open('liked_songs.txt', 'r') as file:
    print(file.read())
