import requests

url = 'https://notify-api.line.me/api/notify'
token = '' #https://notify-bot.line.me/zh_TW/ ->個人頁面->發行權杖
headers = {
    'Authorization': 'Bearer ' + token    # 設定權杖
}
data = {
    'message':'Hello！',     # 設定要發送的訊息
    'stickerPackageId':'446',
    'stickerId':'1988'
}
data = requests.post(url, headers=headers, data=data)   # 使用 POST 方法