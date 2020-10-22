from pyrogram import Client
from pyrogram.raw import functions
from time import sleep

api_id =                                                 # api_id  
api_hash =                                               # api_hash

app=  Client("my_account",api_id,api_hash)
app.start()
count = app.get_chat_members_count("get_member_Group_id")
print(count)
for i in range(count):
    id = app.get_chat_members("get_member_Group_id")[i].user

    app.add_chat_members('add_member_Group_id', id.id)



