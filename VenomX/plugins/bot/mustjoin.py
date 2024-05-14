
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from VenomX import app

#--------------------------

MUST_JOIN = "RBGOFFICIAL1"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/5a37d74a59f00043d64f9.jpg", caption=f"ᴏʏʏ ᴘᴀʜʟᴇ [ sᴜᴘᴘᴏʀᴛ ]({link}) ɢʀᴏᴜᴘ ᴊᴏɪɴ ᴋᴀʀᴏ...[ sᴜᴘᴘᴏʀᴛ ]({link}) ᴊᴏɪɴ ᴋᴀʀɴᴇ ᴋᴇ ʙᴀsᴅ ʜɪ ʙᴏᴛ sᴛᴀʀᴛ ʜᴏɢᴀ ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
