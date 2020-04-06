from typing import List

from telegram import Bot, Update
from telegram.ext import run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

normiefont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
weebyfont = ['🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤',
              '🅥', '🅦', '🅧', '🅨', '🅩']


@run_async
def weebify(bot: Bot, update: Update, args: List[str]):
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


__help__ = """
 Originally Made By [Ayan Ansari](t.me/TechnoAyanOfficial)
 
 - /blackout <text>: Apply Blackout Style to your text
 """

WEEBIFY_HANDLER = DisableAbleCommandHandler("blackout", weebify, pass_args=True)

dispatcher.add_handler(WEEBIFY_HANDLER)

__mod_name__ = "Black Out"
command_list = ["weebify"]
handlers = [WEEBIFY_HANDLER]
