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

line_bot_api = LineBotApi('GTlOAYvr3rP9/O8KFCWYOpBvcWKkZ9pgMKz4LY+UH25qAq16pqJEEA60lemV9ajHWKySDIIUaD3nK3Pak/h1fOMrOWYFI77xqjM8zonLMM7LoW8p8FJM4v4UuT6SJPv6IDA/RxoVJWRbFdvzeYnggAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('36d86887eff5c9fd4acddc59940c1650')  # 해킹방지 암호화


@app.route('/callback', methods=['POST'])
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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == '__main__':
    app.run()