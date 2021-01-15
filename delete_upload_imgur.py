from imgurpython import ImgurClient

client_id = 'YOUR CLIENT ID'
client_secret = 'YOUR CLIENT SECRET'

client = ImgurClient(client_id, client_secret)

# Example request
items = client.gallery()
for item in items:
    print(item.link+",")

# Go th https://imgur.com/removalrequest to delete the image you upload
