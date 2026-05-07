# 📘 Assignment: Consuming REST APIs

## 🎯 Objective

Use Python's `requests` library to fetch data from a public REST API, parse the JSON responses, and filter or display the results in a meaningful way.

## 📝 Tasks

### 🛠️ Fetch and Display Posts

#### Description
Make a GET request to the JSONPlaceholder API to retrieve a list of posts and print each post's title and body to the console.

#### Requirements
Completed program should:

- Use `requests.get()` to fetch all posts from `https://jsonplaceholder.typicode.com/posts`
- Check that the response status code is `200` before processing
- Print the `title` and `body` of every post

### 🛠️ Filter Posts by User

#### Description
Extend your program to accept a user ID from the user and display only the posts written by that user.

#### Requirements
Completed program should:

- Prompt the user to enter a user ID (1–10)
- Filter the list of posts to only those where `userId` matches the input
- Print how many posts were found and display each post's title

Example output:
```
Enter a user ID: 3
Found 10 posts by user 3:
- sunt aut facere repellat provident occaecati excepturi optio reprehenderit
- ...
```

### 🛠️ Look Up a User's Details

#### Description
For the user ID entered above, fetch that user's profile from the API and display their name, email, and city.

#### Requirements
Completed program should:

- Make a GET request to `https://jsonplaceholder.typicode.com/users/<id>` using the same user ID
- Display the user's `name`, `email`, and `address.city`
- Handle the case where the user is not found (status code is not `200`) with a friendly error message

Example output:
```
User profile:
  Name:  Clementine Bauch
  Email: Nathan@yesenia.net
  City:  McKenziehaven
```
