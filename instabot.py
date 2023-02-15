import telegram
import instaloader
from telegram.ext import CommandHandler, Updater

# Replace YOUR_API_TOKEN with your actual API token
bot = telegram.Bot(token='6292823663:AAG2ABwgjzIYDNLLAr33riNlI7LHBx7g2SQ')
updater = Updater(token='6292823663:AAG2ABwgjzIYDNLLAr33riNlI7LHBx7g2SQ', use_context=True)

# Handle /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Send me the link to an Instagram video and I'll download it for you.")

# Handle video download command
def download_video(update, context):
    # Get the URL of the Instagram video from the message
    url = update.message.text
    if 'instagram.com' not in url:
        context.bot.send_message(chat_id=update.effective_chat.id, text="That doesn't look like an Instagram video URL.")
        return

    # Download the video using instaloader
    L = instaloader.Instaloader()
    L.download_video(url)

    # Send the video to the user
    with open(f'{L.context.filename}\'s video.mp4', 'rb') as video:
        context.bot.send_video(chat_id=update.effective_chat.id, video=video)

# Set up command handlers
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(CommandHandler('download', download_video))

# Start the bot
updater.start_polling()
updater.idle()
