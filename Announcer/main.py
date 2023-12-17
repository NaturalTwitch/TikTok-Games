from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent, ShareEvent, LikeEvent, JoinEvent, DisconnectEvent
import pyttsx3

lang = 'en'
engine = pyttsx3.init()
engine.setProperty('language', lang)
engine.setProperty('rate', 150)

tiktok_username = 'naturaltwitch'

client: TikTokLiveClient = TikTokLiveClient(unique_id=f"@{tiktok_username}")


@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Streamer:", tiktok_username)


@client.on("disconnect")
async def on_disconnect(event: DisconnectEvent):
    print('Disconnected')


@client.on("join")
async def on_join(event: JoinEvent):
    engine.say(f"{event.user.unique_id} Welcome to the Stream!")
    engine.runAndWait()


@client.on("share")
async def on_share(event: ShareEvent):
    print(f"@{event.user.unique_id} shared the stream!")
    engine.say(f"{event.user.unique_id} Thanks for sharing the Live.")
    engine.runAndWait()
    return


@client.on("gift")
async def on_gift(event: GiftEvent):
    # Streakable gift & streak is over
    if event.gift.streakable and not event.gift.streaking:
        print(f"{event.user.unique_id} sent {event.gift.count}x \"{event.gift.info.name}\"")

        engine.say(f"Thanks for the {event.gift.info.name} {event.user.nickname}")
        engine.runAndWait()

    elif not event.gift.streakable:
        print(f"{event.user.unique_id} sent \"{event.gift.info.name}\"")


async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")
    engine.say(f"{event.user.unique_id} said {event.comment}")
    engine.runAndWait()

client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()
