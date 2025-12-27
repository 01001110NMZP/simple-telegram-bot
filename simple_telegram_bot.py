from telegram import Update
from telegram.ext import (Application,
                          CommandHandler,
                          MessageHandler,
                          filters,)

# video_tutorial: str = "https://youtu.be/vZtm1wuA2yc?si=iGlFM8LeinbjQ9bS"

TOKEN: str = "8292332768:AAHndDabt6_knDh2GeC4B7hYH3_olsUNjpc"

# Commands

async def start_command(update: Update, context) -> None:
    """Greets the user"""

    await update.message.reply_text("سلام!\n به بات ما خوش اومدی!")


# Response functions

async def message_handler(update: Update, context) -> None:
    """
    echos back whatever the users sends
    and logs who said what and where in the run terminal
    """

    text: str = update.message.text
    user_id: int = update.message.chat.id

    print(f"User ({user_id}) said: {text}")

    await update.message.reply_text(text)

async def error(update: Update, context) -> None:
    """in the run terminal, shows what went wrong"""
    print(f"Update {update} has caused this error {context.error}")


if __name__ == '__main__':

    print("Starting ...")

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))

    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    # Error
    app.add_error_handler(error)

    print("Polling ...")
    app.run_polling(poll_interval=4)
