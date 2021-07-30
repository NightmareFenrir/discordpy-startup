from discord.ext import commands
from discord.ext import tasks
import os
from datetime import datetime 

client = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
channel_id = 870490482415915008

# ================================================================================
# 定時タスク
# ================================================================================
EVENT_TIME_TABLE = {
    # 月曜日
    0: {
        '00:00': [
            {'message': '【イベント終了】イグドラシル防衛線(ペア)が終了しました！'}
        ],
        '20:45': [
            {'message': '【イベント予告】リングが5分後に開始します！'}
        ],
        '20:50': [
            {'message': '【イベント開始】リングが開始しました！'}
        ],
        '21:30': [
            {'message': '【イベント終了】リングが終了しました！'}
        ],
        '23:55': [
            {'message': '【イベント予告】エクストラチャレンジが5分後に開始します！'}
        ]
    },
    # 火曜日
    1: {
        '00:00': [
            {'message': '【イベント開始】エクストラチャレンジが開始しました！'}
        ],
        '20:55': [
            {'message': '【イベント予告】ギルド集会が5分後に開始します！'}
        ],
        '21:00': [
            {'message': '【イベント開始】ギルド集会が開始しました！'}
        ],
        '21:20': [
            {'message': '【イベント終了】ギルド集会が終了しました！'}
        ]
    },
    # 水曜日
    2: {
        '00:00': [
            {'message': '【イベント終了】エクストラチャレンジが終了しました！'}
        ],
        '04:55': [
            {'message': '【イベント予告】ファッション週刊誌が5分後に開始します！'}
        ],
        '05:00': [
            {'message': '【イベント開始】ファッション週刊誌が開始しました！'}
        ],
        '20:25': [
            {'message': '【イベント予告】ギルドマッチング大会が5分後に開始します！'}
        ],
        '20:30': [
            {'message': '【イベント開始】ギルドマッチング大会が開始しました！'}
        ],
        '21:20': [
            {'message': '【イベント終了】ギルドマッチング大会が終了しました！'}
        ],
        '23:55': [
            {'message': '【イベント予告】エクストラチャレンジが5分後に開始します！'}
        ]
    },
    # 木曜日
    3: {
        '00:00': [
            {'message': '【イベント終了】ファッション週刊誌が終了しました！'},
            {'message': '【イベント開始】エクストラチャレンジが開始しました！'}
        ],
        '20:55': [
            {'message': '【イベント予告】ギルド集会が5分後に開始します！'}
        ],
        '21:00': [
            {'message': '【イベント開始】ギルド集会が開始しました！'}
        ],
        '21:20': [
            {'message': '【イベント終了】ギルド集会が終了しました！'}
        ]
    },
    # 金曜日
    4: {
        '00:00': [
            {'message': '【イベント終了】エクストラチャレンジが終了しました！'}
        ],
        '20:45': [
            {'message': '【イベント予告】リングが5分後に開始します！'}
        ],
        '20:50': [
            {'message': '【イベント開始】リングが開始しました！'}
        ],
        '21:30': [
            {'message': '【イベント終了】リングが終了しました！'}
        ],
        '18:25': [
            {'message': '【イベント終了】リングが終了しました！'}
        ]
    },
    # 土曜日
    5: {
        '09:55': [
            {'message': '【イベント予告】イグドラシル防衛線(ペア)が5分後に開始します！'}
        ],
        '10:00': [
            {'message': '【イベント開始】イグドラシル防衛線(ペア)が開始しました！'}
        ],
        '20:55': [
            {'message': '【イベント予告】週末集会が5分後に開始します！'}
        ],
        '21:00': [
            {'message': '【イベント開始】週末集会が開始しました！'}
        ],
        '21:20': [
            {'message': '【イベント終了】週末集会が終了しました！'}
        ]
    },
    # 日曜日
    6: {
        '00:00': [
            {'message': '【イベント終了】イグドラシル防衛線(ペア)が終了しました！'}
        ],
        '09:55': [
            {'message': '【イベント予告】イグドラシル防衛線(ペア)が5分後に開始します！'}
        ],
        '10:00': [
            {'message': '【イベント開始】イグドラシル防衛線(ペア)が開始しました！'}
        ],
        '19:55': [
            {'message': '【イベント予告】テーマパーティーが5分後に開始します！'}
        ],
        '20:00': [
            {'message': '【イベント開始】テーマパーティーが開始しました！'}
        ],
        '20:30': [
            {'message': '【イベント終了】テーマパーティーが終了しました！'}
        ]
    }
}

@tasks.loop(seconds = 5, reconnect = True)
async def loop():
    # 現在の時刻
    now = datetime.now()
    time = now.strftime('%H:%M')
    table = EVENT_TIME_TABLE[now.weekday()]
    channel = client.get_channel(channel_id)

    if channel is None:
        return

    if time in table:   
        for msg in table[time]:
            message = time + msg['message']
            await channel.send(message)

#ループ処理実行
loop.start()
# ================================================================================

# Botの起動とDiscordサーバーへの接続
client.run(token)
