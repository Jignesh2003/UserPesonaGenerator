import praw

#setup Reddit api credentials
reddit = praw.Reddit(
    client_id="<your-client_id>",
    client_secret="<your-client_secret>",
    user_agent="script:reddit.persona:v1.0 (by u/YourUsername)"
)

def extract_username_from_url(url):
    return url.strip("/").split("/")[-1]

def get_user_content(username, limit=8):
    user = reddit.redditor(username)
    posts = []
    comments = []

    try:
        # Fetch user submissions (posts)
        for post in user.submissions.new(limit=limit):
            posts.append({
                "title": post.title,
                "body": post.selftext,
                "url": post.url,
                "permalink": f"https://reddit.com{post.permalink}"
            })
    except Exception as e:
        print(f"Error getting posts: {e}")

    try:
        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "permalink": f"https://reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"Error getting comments: {e}")
    
    return posts, comments

def generate_persona_file(username, posts, comments):
    filename = f"user_persona_{username}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"User Persona for Reddit User: {username}\n")
        f.write("="*50 + "\n\n")

        f.write("Sample Posts:\n")
        for post in posts[:3]:
            f.write(f"- Title: {post['title']}\n")
            f.write(f"  URL: {post['permalink']}\n")
            f.write(f"  Body: {post['body'][:200]}...\n\n")

        f.write("Sample Comments:\n")
        for comment in comments[:3]:
            f.write(f"- {comment['body'][:200]}...\n")
            f.write(f"  URL: {comment['permalink']}\n\n")
    return filename

def main():
    reddit_url = input("Enter Reddit profile URL: ").strip()
    username = extract_username_from_url(reddit_url)
    print(f"Fetching content for user: {username}")

    posts, comments = get_user_content(username)
    print(f"Collected {len(posts)} posts and {len(comments)} comments")
    filename = generate_persona_file(username, posts, comments)
    print(f"User persona saved to: {filename}")

if __name__== "__main__":
    main()
