#from parser2 import Notice
import os
import telegram

my_token = '666407138:AAHpt3BDlWFCtHAgDG6GCxBnjJXdxHIXVaE'
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)
"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

notice = Notice()
latest = notice.simplify(notice.getNewNotice())

with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
    before = f_read.readline()
    if before != latest:
        bot.sendMessage(chat_id=chat_id, text='새 글이 올라왔어요!')
    else:  # 원래는 이 메시지를 보낼 필요가 없지만, 테스트 할 때는 봇이 동작하는지 확인차 넣어봤어요.
        bot.sendMessage(chat_id=chat_id, text='새 글이 없어요 ㅠㅠ')
    f_read.close()

with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
    f_write.write(latest)
    f_write.close()
"""
