import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

def create_media_container(user_id, access_token, media_type, text, image_url=None, video_url=None):
    url = f"https://graph.threads.net/v1.0/{user_id}/threads"
    payload = {
        'media_type': media_type,
        'text': text,
        'access_token': access_token
    }
    if image_url:
        payload['image_url'] = image_url
    if video_url:
        payload['video_url'] = video_url

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json().get('id')
    else:
        print(f"Error creating media container: {response.text}")
        return None

def publish_media_container(user_id, access_token, container_id):
    url = f"https://graph.threads.net/v1.0/{user_id}/threads_publish"
    payload = {
        'creation_id': container_id,
        'access_token': access_token
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json().get('id')
    else:
        print(f"Error publishing media container: {response.text}")
        return None

def main():
    user_id = os.getenv('USER_ID')
    access_token = os.getenv('ACCESS_TOKEN')
    media_type = 'IMAGE'
    text = 'Hello, this is a test post with an image!'
    image_url = 'https://www.example.com/images/test-image.jpg'
    
    container_id = create_media_container(user_id, access_token, media_type, text, image_url=image_url)
    if container_id:
        print(f"Media container created with ID: {container_id}")
        time.sleep(30)  # Wait 30 seconds before publishing
        media_id = publish_media_container(user_id, access_token, container_id)
        if media_id:
            print(f"Media published with ID: {media_id}")

if __name__ == "__main__":
    main()
