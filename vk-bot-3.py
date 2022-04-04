import vk_api
from loggin_password import login, password
from pprint import pprint


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = False

    return key, remember_device


def main():
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)
    try:
        vk_session.auth()
    except vk_api.VkApiError as error_msg:
        print(error_msg)
        return
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_wall(['antoshka.jpg'])
    vk_foto_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"
    vk = vk_session.get_api()
    vk.wall.post(message="Это мы не проходили...", attachmants=[vk_foto_id])


if __name__ == "__main__":
    main()
