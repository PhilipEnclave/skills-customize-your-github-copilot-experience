import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_posts():
    """Task 1: Fetch and display all posts."""
    response = requests.get(f"{BASE_URL}/posts")
    # TODO: Check that response.status_code == 200 before continuing
    posts = response.json()
    for post in posts:
        # TODO: Print the title and body of each post
        pass


def filter_posts_by_user(user_id):
    """Task 2: Filter posts by user ID."""
    response = requests.get(f"{BASE_URL}/posts")
    posts = response.json()
    # TODO: Filter posts where post["userId"] == user_id
    filtered = []
    # TODO: Print how many posts were found, then print each title
    return filtered


def fetch_user(user_id):
    """Task 3: Fetch and display a user's profile."""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    # TODO: Check the status code; if not 200, print a friendly error and return
    user = response.json()
    # TODO: Print the user's name, email, and address["city"]


if __name__ == "__main__":
    print("=== Task 1: All Posts ===")
    fetch_posts()

    print("\n=== Task 2 & 3: Posts and Profile by User ===")
    user_id = int(input("Enter a user ID (1-10): "))
    filter_posts_by_user(user_id)
    fetch_user(user_id)
