class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    @staticmethod
    def send_massage(massage):
        print(massage)


bot = Bot("Julia")
bot.say_name()
bot.send_massage("srhdgfadlfhveasswj")


class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        super().__init__(name)
        self.url = url
        self.chat_id = chat_id

    def set_url(self, new_url):
        self.url = new_url

    def chat_id(self, new_chat_id):
        self.chat_id = new_chat_id

    def send_massage(self, massage):
        print(f"Your {massage} have url {self.url}  and chat_id {self.chat_id} ")


telegram_bot = TelegramBot("Andriy", 243242, 1)

telegram_bot.say_name()
telegram_bot.send_massage("srhdgfadlfhveasswj")