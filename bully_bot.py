from telegram.ext import * 
import constant as key
import response as k
print("Bot started..")
def start_command(update,context):
    update.message.reply_text("Hello, welcome to Profanity detection bot. Please write /help to see commands available")
def help_command(update,context):
    update.message.reply_text("""This bot is made to detect offensive messages, and there is no command as such""")
def handle_message(update,context):
    text=str(update.message.text).lower()
    responses=k.sample_response(text)

    update.message.reply_text(responses)
def error(update,context):
    print(f"Update {update} caused error {context.error} ")

def main():
    updater=Updater(key.API_KEY,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()

main()