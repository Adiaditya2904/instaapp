import instaloader

# Creating an Instaloader() object
ig = instaloader.Instaloader()

# Taking Instagram username as input from the user
usrname = input("Enter username: ")

try:
    # Fetching the details of the provided username using Instaloader object
    profile = instaloader.Profile.from_username(ig.context, usrname)

    # Printing the fetched details
    print("Username: ", profile.username)
    print("Number of Posts Uploaded: ", profile.mediacount)
    print(profile.username + " has " + str(profile.followers) + ' followers.')
    print(profile.username + " is following " + str(profile.followees) + ' people')
    print("Bio: ", profile.biography)

    # Downloading the profile picture
    ig.download_profile(usrname, profile_pic_only=True)
    print(f"Profile picture of {usrname} has been downloaded successfully.")

except instaloader.exceptions.ProfileNotExistsException:
    print(f"Error: The profile '{usrname}' does not exist.")
except instaloader.exceptions.InstaloaderException as e:
    print(f"An error occurred: {e}")
