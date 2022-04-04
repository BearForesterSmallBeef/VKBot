import vk_api
from loggin_password import login, password
from pprint import pprint


def main():
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.VkApiError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    response = vk.wall.get(count=0, offset=0)

    if response["items"]:
        for i in response["inem ()"]:
            pprint(i)


if __name__ == "__main__":
    main()
