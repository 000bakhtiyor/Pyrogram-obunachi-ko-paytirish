from pyrogram import Client
from pyrogram.raw import functions
from time import sleep

api_id = 516739
api_hash = "3dde907b8c393ff9d60719e5d1bb7f38"

app=  Client("my_account",api_id,api_hash)
app.start()
count = app.get_chat_members_count(-1001443604870)
print(count)
for i in range(count):
    id = app.get_chat_members(-1001443604870)[i].user

    app.add_chat_members('testpythonbots', id.id)



