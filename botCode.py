# Old Code: botCode.py
"""
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5131166217:AAE8tAgK0J-O8gk_1CMTF7INSaC-Mlqapvo", use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text("Welcome to ACVRCT Bot! I'm here to help you create VRChat links or find information about VRChat users!")

def about(update: Update, context: CallbackContext):
	update.message.reply_text("This bot was created by LyzCoote, a Italian developer in Rome that very like VRChat and wants to make some useful tools for VRChat users.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("This will be the help message")

def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	# Filters out unknown commands
	Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

def main():
    updater.start_polling()
"""

# New Code: botCode.py
"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import apiHandler as VRChatAPI

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

"""Start the bot."""
# Create the Updater and pass it your bot's token.
# Make sure to set use_context=True to use the new context based callbacks
# Post version 12 this will no longer be necessary
updater = Updater("5131166217:AAE8tAgK0J-O8gk_1CMTF7INSaC-Mlqapvo", use_context=True)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Welcome to ACVRCT Bot! I'm here to help you create VRChat links or find information about VRChat users!")

def getUserInfo(update, context):
	user = update.message.from_user
	try:
		logger.log('You talk with user {} and his user ID: {} '.format(user['username'], user['id']))
	except:
		logger.error('Something went wrong while trying to get user info')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help message here!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def unknown_text(update, context):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)

def unknown(update, context):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)

def getAPIKey(update, context):
	update.message.reply_text("The API Key is: " + VRChatAPI.getCachedAPIKey())

def getUserInfo(update, context):
	userInfo = VRChatAPI.getUserInfo(VRChatAPI.getCachedAPIKey(), str(context.args[0]))
	update.message.reply_text("User info".join(userInfo))

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def exit(update, context):
	update.message.reply_text("Bye!")
	updater.stop()

# Get the dispatcher to register handlers
dp = updater.dispatcher
# on different commands - answer in Telegram
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(CommandHandler("getAPIKey", getAPIKey))
dp.add_handler(CommandHandler("getUserInfo", getUserInfo))
dp.add_handler(CommandHandler("exit", exit))

dp.add_handler(MessageHandler(Filters.text, unknown))
dp.add_handler(MessageHandler(
	# Filters out unknown commands
	Filters.command, unknown))

# Filters out unknown messages.
dp.add_handler(MessageHandler(Filters.text, unknown_text))

# log all errors
dp.add_error_handler(error)

def main():
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()