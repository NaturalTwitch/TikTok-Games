from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent, ShareEvent, LikeEvent
import pyautogui
import time
import PySimpleGUI as sg
import pyttsx3
import configparser
import os

lang = 'en'
engine = pyttsx3.init()
engine.setProperty('language', lang)
engine.setProperty('rate', 150)

config = configparser.ConfigParser()

# Check if the config.txt file exists
if not os.path.exists('config.txt'):
    # The file does not exist, create it with predefined settings
    sg.Popup("Warn", "No Config.txt Found. Making One")
    print(f'No Config.txt found. Making One')

    config.read_dict({'TikTok': {'username': 'your_username'}})

    with open('config.txt', 'w') as configfile:
        config.write(configfile)

config.read('config.txt')

tiktok_username = config.get('TikTok', 'username')

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id=f"@{tiktok_username}")


# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Streamer:", tiktok_username)


@client.on("like")
async def on_like(event: LikeEvent):
    print(f"@{event.user.unique_id} liked the stream! {event.likes} Times")

    if event.likes > 14:
        pyautogui.keyDown("w")
        time.sleep(2)
        pyautogui.keyUp('w')
        return


@client.on("share")
async def on_share(event: ShareEvent):
    print(f"@{event.user.unique_id} shared the stream!")
    pyautogui.keyDown("w")
    time.sleep(2)
    pyautogui.keyUp('w')
    return


@client.on("gift")
async def on_gift(event: GiftEvent):
    # Streakable gift & streak is over
    if event.gift.streakable and not event.gift.streaking:
        print(f"{event.user.unique_id} sent {event.gift.count}x \"{event.gift.info.name}\"")

        engine.say(f"Thanks for the {event.gift.info.name} {event.user.nickname}")
        engine.runAndWait()

        if event.gift.info.name == "Rose":
            pyautogui.keyDown("w")
            time.sleep(event.gift.count + 5)
            pyautogui.keyUp('w')
            return

        if event.gift.info.name == "TikTok":
            pyautogui.keyDown('s')
            time.sleep(event.gift.count + 5)
            pyautogui.keyUp('s')
            return

        if event.gift.info.name == "Ice Cream Cone":
            pyautogui.keyDown('a')
            time.sleep(event.gift.count + 5)
            pyautogui.keyUp('a')
            return

        if event.gift.info.name == "GG":
            pyautogui.keyDown('d')
            time.sleep(event.gift.count + 5)
            pyautogui.keyUp('d')
            return

        if event.gift.info.name == "Finger Heart":
            pyautogui.mouseDown(button='left')
            time.sleep(2)
            pyautogui.mouseUp(button='left')
            return
        if event.gift.info.name == "Fire":
            pyautogui.mouseDown(button='right')
            time.sleep(10)
            pyautogui.mouseUp(button='right')
            return

    # Non-streakable gift
    elif not event.gift.streakable:
        print(f"{event.user.unique_id} sent \"{event.gift.info.name}\"")


async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")

    if event.comment == "1":
        pyautogui.press("1")
        return

    if event.comment == "2":
        pyautogui.press("2")
        return

    if event.comment == "3":
        pyautogui.press("3")
        return

    if event.comment == "4":
        pyautogui.press("4")
        return

    if event.comment == "5":
        pyautogui.press("5")
        return

    if event.comment == "6":
        pyautogui.press("6")
        return

    if event.comment == "7":
        pyautogui.press("7")
        return

    if event.comment == "8":
        pyautogui.press("8")
        return

    if event.comment == "9":
        pyautogui.press("9")
        return

    if event.comment == "jump":
        pyautogui.keyDown('space')
        time.sleep(1)
        pyautogui.keyUp('space')
        return

    if event.comment == "up":
        pyautogui.move(0, -10, 2)
        return

    if "down" in event.comment:
        pyautogui.move(0, 10, 2)
        return

    if event.comment == "left":
        pyautogui.move(-10, 0, 2)
        return

    if event.comment == "right":
        pyautogui.move(10, 0, 2)
        return

    if event.comment == "e":
        pyautogui.press('e')
        return

    engine.say(f"{event.user.unique_id} said {event.comment}")
    engine.runAndWait()


# Define handling an event via a "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()
