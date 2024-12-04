import asyncio
import json
from twitchio.ext import commands
from obswebsocket import obsws, requests as obs_requests

print("Добро пожаловать в программу для работы с Twitch и OBS!")
OBS_HOST = input("Введите хост OBS (например, localhost): ").strip()
OBS_PORT = int(input("Введите порт OBS (например, 4444): ").strip())
OBS_PASSWORD = input("Введите пароль OBS: ").strip()
ACCESS_TOKEN = input("Введите Twitch Access Token: ").strip()
CHANNEL_NAME = input("Введите имя канала Twitch: ").strip()

SUBSCRIPTIONS_FILE = "subscriptions.json"

def connect_to_obs():
    ws = obsws(OBS_HOST, OBS_PORT, OBS_PASSWORD)
    try:
        ws.connect()
        print("Успешно подключено к OBS")
    except Exception as e:
        print(f"Ошибка подключения к OBS: {e}")
    return ws

def load_subscriptions():
    try:
        with open(SUBSCRIPTIONS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            print("Подписки успешно загружены.")
            return data
    except FileNotFoundError:
        print("Файл с подписками не найден, создается новый.")
        return {}
    except json.JSONDecodeError:
        print("Ошибка чтения файла подписок, создается новый.")
        return {}

def save_subscriptions(subscriptions):
    try:
        with open(SUBSCRIPTIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(subscriptions, f, ensure_ascii=False, indent=4)
            print("Подписки успешно сохранены.")
    except Exception as e:
        print(f"Ошибка сохранения подписок: {e}")

async def update_obs_text(ws, text):
    try:
        ws.call(obs_requests.SetTextFreetype2Properties(source="SubText", text=text))
        print(f"Текст обновлен: {text}")
    except Exception as e:
        print(f"Ошибка обновления текста: {e}")
        ws = connect_to_obs()
        await update_obs_text(ws, text)

def update_subscription_text():
    sorted_subs = sorted(subscriptions.items(), key=lambda x: x[1], reverse=True)[:15]  # Топ-15
    text = " | ".join([f"{nick} - {subs}" for nick, subs in sorted_subs])
    return text


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix="!", initial_channels=[CHANNEL_NAME])
        self.ws = connect_to_obs()

    async def event_ready(self):
        print(f"Бот подключен как {self.nick}")

    async def event_usernotice_subscription(self, metadata):
        user = metadata["msg-param-displayName"]
        print(f"Новая подписка от {user}!")

        if user in subscriptions:
            subscriptions[user] += 1
        else:
            subscriptions[user] = 1

        save_subscriptions(subscriptions)
        text = update_subscription_text()
        await update_obs_text(self.ws, text)

    @commands.command(name="test_sub")
    async def test_sub(self, ctx):
        user = ctx.author.name
        print(f"Тестовая подписка от {user}")

        if user in subscriptions:
            subscriptions[user] += 1
        else:
            subscriptions[user] = 1

        save_subscriptions(subscriptions)
        text = update_subscription_text()
        await update_obs_text(self.ws, text)

    @commands.command(name="test_multiple_subs")
    async def test_multiple_subs(self, ctx, count: int):
        user = ctx.author.name
        print(f"Тестовое добавление {count} подписок от {user}")

        if user in subscriptions:
            subscriptions[user] += count
        else:
            subscriptions[user] = count

        save_subscriptions(subscriptions)
        text = update_subscription_text()
        await update_obs_text(self.ws, text)

subscriptions = load_subscriptions()

if __name__ == "__main__":
    bot = Bot()
    bot.run()
