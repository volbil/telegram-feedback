from telegram.utils.helpers import escape_markdown
from webargs.flaskparser import use_args
from ..models import Message
from flask import Blueprint
from .args import form_args
from telegram import Bot
from pony import orm
import config

blueprint = Blueprint("feedback", __name__)

@blueprint.route("/submit", methods=["POST"])
@use_args(form_args, location="json")
@orm.db_session
def form(args):
    message = Message(**args)
    bot = Bot(config.bot_key)

    sent = message.created.strftime("%m/%d/%Y, %H:%M:%S (UTC)")
    text = f"*Email*: {escape_markdown(message.email, version=2)}\n"
    text += f"*Sent*: {escape_markdown(sent, version=2)}\n"
    text += f"*Message:* {escape_markdown(message.message, version=2)}\n"
    text += f"*Offers*: {message.offers}"

    bot.send_message(
        chat_id=config.chat_id, text=text,
        parse_mode="MarkdownV2"
    )

    return {
        "error": None, "result": {
            "success": True
        }
    }
