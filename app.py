from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('qIMmUZ026N+gmu/8nIYVp9W2aGcIpyAIET+6NJABHmwDdOs7tkTx6xIjV3IlO9VEsYftfDO3kldLzeTUgPbvTUTK9tQaSJZXFBAHibt6GuFWMPNjkWxKjEEmq45kbqpwKO3d5mDRm+rnD2t1f50afgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bbbd2cdcd841e1af8d95d2067d1bdfed')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	msg = event.message.text
	s = '朱鴻埕好帥'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()

