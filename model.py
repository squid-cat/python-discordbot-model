# インストールした discord.py を読み込む
import discord

# botのアクセストークンをここに入力
# ex) TOKEN = 'abcdefg12345'
TOKEN = ''

# 接続に必要なオブジェクトを生成
client = discord.Client()


# ----- この下に色々な処理を書きます！ --------------

# 今回はオウム返しをするコードを書いてみましょう！

# --------------------------------------------------


# Botの起動とDiscordサーバーへの接続
# (必ず一番最後に書くこと！)
client.run(TOKEN)