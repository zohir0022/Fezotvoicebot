import telebot
from telebot import types
import os

TOKEN = "8720001305:AAEoKRzIvJd9KS_hJpBHELQqcsFGf0NmFPg"

bot = telebot.TeleBot(TOKEN)

voices = {
    "qondaye":"AwACAgQAAxkBAAIBR2o4R75h3VJdMFyBgKNGwpSkQvxAALzCQACaPSEUoHqz6uoyqGPAQ",
    "reyboy":"AwACAgQAAxkBAAIBSWo4SKeX-n3Zj_RAv0K5A89dwBXRAAIZCQACI--NUscRmLOULtwAATwE"
}

@bot.inline_handler(func=lambda query: True)
def inline(query):

    results = []

    for name, fileid in voices.items():

        results.append(
            types.InlineQueryResultCachedVoice(
                id=name,
                voice_file_id=fileid,
                title=name
            )
        )

    bot.answer_inline_query(
        query.id,
        results,
        cache_time=1
    )

bot.infinity_polling()
