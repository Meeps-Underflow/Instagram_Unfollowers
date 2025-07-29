from bs4 import BeautifulSoup

def get_usernames_from_html(html_file):
    file = open(html_file, 'r')
    contents = file.read()

    soup = BeautifulSoup(contents, 'lxml')
    usernames =  [username.text for username in soup.select('div a')]
    return usernames

followers_file = '/Users/Meeps-Underflow/Documents/Projects/Instagram Unfollow/Data/followers_1.html' # replace with your filename
followings_file = '/Users/Meeps-Underflow/Documents/Projects/Instagram Unfollow/Data/following.html' # same as followers


followers = get_usernames_from_html(followers_file)
followings = get_usernames_from_html(followings_file)

not_following_back = [user for user in followings if user not in followers]

print(not_following_back)
print(len(not_following_back))
