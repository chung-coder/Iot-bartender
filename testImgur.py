from imgurpython import ImgurClient
from datetime import datetime


def upload(client_data, album, name='test-name!', title='test-title'):
    config = {
        'album':  album,
        'name': name,
        'title': title,
        'description': f'test-{datetime.now()}'
    }

    print("Uploading image... ")
    image = client_data.upload_from_path(
        'test.jpg', config=config, anon=False)
    print("Done")

    return image


if __name__ == "__main__":
    client_id = '45849270466ce78'
    client_secret = '3f9cf8c30851ba87718f8eb8c811d21789ce091d'
    access_token = "8f8935816169978dfda72b5116791294e64f2f59"
    refresh_token = "d17374e06ca5dd4f996bfe7f016b411dbe0646ef"
    album = "a/zLzObDC"
    local_img_file = "test.jpg"

    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    image = upload(client, local_img_file, album)
    print(f"圖片網址: {image['link']}")
