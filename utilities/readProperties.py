import configparser

config = configparser.RawConfigParser()

config.read("./Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def get_user_name():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_user_password():
        password = config.get('common info', 'password')
        return password
