import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
post_response = requests.get(blog_url)
all_posts = post_response.json()
print(all_posts)


