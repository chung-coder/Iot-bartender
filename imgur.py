from imgurpython import ImgurClient

client_id = '45849270466ce78'
client_secret = 'cf68a47ba667c2a519bb5575ab015555ea7149d5'

client = ImgurClient(client_id, client_secret)

# Example request
items = client.gallery()
for item in items:
    print(item.link)
