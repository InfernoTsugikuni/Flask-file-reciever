import requests

# Replace with your server IP - Flask tells you what it is
url = 'http://YOUR SERVER IP:5000/upload'

# Path to the file you want to upload
file_path = r'C:\Users\userDocuments\FlaskWebhookSystem\New Text Document.txt'

with open(file_path, 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

print(response.text)
