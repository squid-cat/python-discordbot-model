# インストールした discord.py を読み込む
import discord

# botのアクセストークンをここに入力
# ex) TOKEN = 'abcdefg12345'
TOKEN = ''

# 接続に必要なオブジェクトを生成
client = discord.Client()

# メッセージが送られると動く部分
@client.event
async def on_message(message):
    # messageに色々な情報が格納されています！
    print(message)


# Botの起動とDiscordサーバーへの接続
# (必ず一番最後に書くこと！)
client.run(TOKEN)