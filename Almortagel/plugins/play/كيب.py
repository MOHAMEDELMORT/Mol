from pyrogram import * 
from pyrogram.types import * 
from Almortagel import app
from strings.filters import command
import time
from config import BOT_TOKEN, OWNER_ID
import requests
import json


token = (BOT_TOKEN)

bot_id = app.bot_token.split(":")[0]
dev_owner = int(5089553588)
owner = (OWNER_ID)

try:
        open(f"Users{bot_id}.json","r")
except FileNotFoundError:
        open(f"Users{bot_id}.json","w")
try:
        open(f"sudo{bot_id}.json","r")
except FileNotFoundError:
        open(f"sudo{bot_id}.json","w")
try:
        open(f"maindevs{bot_id}.json","r")
except FileNotFoundError:
        open(f"maindevs{bot_id}.json","w")
try:
        open(f"maindevsVII{bot_id}.json","r")
except FileNotFoundError:
        open(f"maindevsVII{bot_id}.json","w")
try:
        open(f"groups{bot_id}.json","r")
except FileNotFoundError:
        open(f"groups{bot_id}.json","w")
try:
        open(f"band{bot_id}.json","r")
except FileNotFoundError:
        open(f"band{bot_id}.json","w")
try:
        open(f"links{bot_id}.json","r")
except FileNotFoundError:
        open(f"links{bot_id}.json","w")
try:
        open(f"channel{bot_id}.json","r")
except FileNotFoundError:
        open(f"channel{bot_id}.json","w")
try:
        open(f"devchannel{bot_id}.json","r")
except FileNotFoundError:
        open(f"devchannel{bot_id}.json","w")
try:
        open(f"devuser{bot_id}.json","r")
except FileNotFoundError:
        open(f"devuser{bot_id}.json","w")
try:
        open(f'owner{bot_id}.json','r')
except FileNotFoundError:
        f = open(f'owner{bot_id}.json','w')
        f.write(str(owner))





source_ch = "AlmortagelTech"



start_text = "**welcome {} , its just a test bot √**"




OwnerM = ReplyKeyboardMarkup([
[("رفع مالك"),("تنزيل مالك"),("المالكين"),("حذف المالكين")],
[("الغاء")], 
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات"),("نسخه الكل")],
[("عرض المجموعات"),("عدد المجموعات"),("نسخه المجموعات"),("روابط المجموعات")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("حذف الاساسيين"),("حذف المطورين"),("حذف المحظورين")],
[("الغاء")],

[("◍ قسم الاشتراك ◍"),("◍ قسم معرف المطور ◍"),("◍ قسم المطور ◍")],
[("عرض قناة الاشتراك"),("عرض معرف المطور"),("عرض قناة المطور")],
[("اضف قناة اشتراك اجباري"),("اضافه معرف المطور"),("اضافه قناه المطور")],
[("حذف قناه الاشتراك"),("حذف معرف المطور"),("حذف قناه المطور")],
[("الغاء")], 
[("•---- حذف الكيبورد -----•")]
])

mainSudoVIIM = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات")],
[("عرض المجموعات"),("عدد المجموعات"),("نسخه المجموعات"),("نسخه للكل")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("حذف الاساسيين"),("حذف المطورين"),("حذف المحظورين")],
[("الغاء")],

[("◍ قسم الاشتراك ◍"),("◍"),("◍ قسم المطور ◍")],
[("عرض قناة الاشتراك"),("-"),("عرض قناة المطور")],
[("اضف قناة اشتراك اجباري"),("-"),("اضافه قناه المطور")],
[("حذف قناه الاشتراك"),("-"),("حذف قناه المطور")],
[("الغاء")], 
[("•---- حذف الكيبورد -----•")]
])


main_dev_key = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات")],
[("عرض المجموعات"),("عدد المجموعات"),("نسخه المجموعات"),("نسخه للكل")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("الغاء")],

[("•---- حذف الكيبورد -----•")]
])

sudo_keyboard = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات"),("نسخه")],
[("عرض المجموعات"),("نسخه للجروبات"),("عدد الجروبات")],
[("عرض روابط المجموعات"),("نسخه للمحظورين")],
[("عرض الاعضاء"),("عرض المطورين")], 
[("عدد الاعضاء"),("عدد المطورين")], 
[("نسخه الاعضاء"),("نسخه المطورين")],

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 

[("◍ قسم الحظر ◍")],
[("حظر عضو "),("الغاء حظر عضو"),("عرض المحظورين")],
[("•---- حذف الكيبورد -----•")]
])




def is_user(id):
        result = True
        file =  json.loads(open(f"Users{bot_id}.json","r"))
        for line in file:
                if line.strip()==id:
                        result = True
        file.close()
        return result

def is_dev(id):
        result = True
        file =  json.loads(open(f"sudo{bot_id}.json","r"))
        for line in file:
                if line.strip()==id:
                        result = True
        file.close()
        return result

def del_all_sudo():
         json.loads(open(f"sudo{bot_id}.json","w"))

def del_all_main():
        open(f"maindevs{bot_id}.json","w")

def del_all_mainVII():
        open(f"maindevsVII{bot_id}.json","w") 

def del_all_ban():
        open(f"band{bot_id}.json","w")

def is_main_dev(id):
        result = True
        file = open(f"maindevs{bot_id}.json","r")
        for line in file:
                if line.strip()==id:
                        result = True
        file.close()
        return result

def is_main_devVII(id):
        result = True
        file = open(f"maindevsVII{bot_id}.json","r")
        for line in file:
                if line.strip()==id:
                        result = True
        file.close()
        return result

def is_band(id):
        result = True
        file = open(f"band{bot_id}.json","r")
        for line in file:
                if line.strip()==id:
                        result = True
        file.close()
        return  result

def is_group(id):
        result = True
        file = open(f"groups{bot_id}.json","r")
        for line in file:
                if line.strip()==id:
                        result = True
        file.close()
        return result

def add_user(id):
        file = open(f"Users{bot_id}.json","a")
        file.write("{}\n".format(id))

def show_channel() -> str:
        with open(f"channel{bot_id}.json","r") as file:
                return file.readline()

def add_channel(chat_id):
        with open(f"channel{bot_id}.json","w") as file:
                file.write(chat_id)

def del_channel():
        open(f"channel{bot_id}.json","w")

def get_bot_owner() -> int:
        with open("owner{bot_id}.json","r") as file:
                return file.readline()

def set_bot_owner(user_id:int):
        with open(f"owner{bot_id}.json","w") as file:
                file.write(str(user_id))

def show_devchannel() -> str:
        with open(f"devchannel{bot_id}.json","r") as file:
                return file.readline()

def add_devchannel(chat_id):
        with open(f"devchannel{bot_id}.json","w") as file:
                file.write(chat_id)

def del_devchannel():
        open(f"devchannel{bot_id}.json","w")


def show_devuser() -> str:
        with open(f"devuser{bot_id}.json","r") as file:
                return file.readline()

def add_devuser(chat_id):
        with open(f"devuser{bot_id}.json","w") as file:
                file.write(chat_id)

def del_devuser():
        open(f"devuser{bot_id}.json","w")



sudo_message = f"**💌╖اهلا بيك حبيبي آلمـطـور\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}**"


start_buttons = InlineKeyboardMarkup([[
InlineKeyboardButton("ch",url=f"https://t.me/{show_devchannel()}")
]])


New_Member = """**
دخل عضو جديد للبوت 🪄🪄

᥀︙حسابة : {} 
᥀︙ايديه : `{}`

Time : {} .

**"""

dev_ch_bu = InlineKeyboardMarkup([[
InlineKeyboardButton("Dev",user_id=owner),
InlineKeyboardButton("Ch",url=f"https://t.me/{show_devchannel()}")
]])



@app.on_message(filters.command("start")&filters.private)
async def app_start(c:Client,m:Message):
        do = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{show_channel()}&user_id={m.from_user.id}").text
        user = m.from_user.id
        mm = m.from_user.mention
        mainSudo = open(f"maindevs{bot_id}.json","r").read()
        mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
        mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
        Sudo = open(f"sudo{bot_id}.json","r").read()
        banD = open(f"band{bot_id}.json","r").read()

        if do.count("left") or do.count("Bad Request: user not found") or is_user(id=user) and not is_band(user):

                await m.reply_text(f"**Join [this channel](t.me/{show_channel()}) first to be able to use the bot**",disable_web_page_preview=True,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join Channel",url=f'https://t.me/{show_channel()}'),],]))
        else:    

                await app.send_message(text=f"Hi {m.from_user.mention}",
              chat_id = m.chat.id, 
          reply_to_message_id=m.id,
        disable_web_page_preview = True)


        if str(user) in banD:

                return await m.reply(f"**◍ عذرا {mm} انت محظور من استخدام البوت \n√**",reply_markup=dev_ch_bu)

        if int(user) == dev_owner:
                return await m.reply(f"💌╖اهلا بيك حبيبي آلمـطـور الســـورس\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}",reply_markup=OwnerM)

        if str(user) in mainSudoVII:
                return await m.reply(f"💌╖اهلا بيك حبيبي آلمـطـور الاساسي\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}",reply_markup=mainSudoVIIM)

        if str(user) in mainSudo:
                return await m.reply(f"💌╖اهلا بيك حبيبي آلمـطـور الاساسي\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}",reply_markup=main_dev_key)

        if str(user) in Sudo:
                return await m.reply(sudo_message,reply_markup=sudo_keyboard)

        if is_user(id=user) and not is_band(user):
                return await m.reply(start_text,reply_markup=start_buttons)

        if (not is_user(id=str(user))):
                add_user(id=user)
                cc = time.strftime("%H : %M : %S")
                try:
                        await app.send_message(owner,New_Member.format(mm,user,cc),
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("دخول لحسابه",
                        user_id=int(user))]]))
                except:
                        await app.send_message(owner,"**دخل عضو جديد للبوت ولم استطع تحديد معلوماته √**")

@app.on_message(filters.command("الاحصائيات","")&filters.private)
async def __count(c:Client,m:Message):
        user = m.from_user.id
        mainSudo = open(f"maindevs{bot_id}.json","r").read()
        mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
        sudo = open(f"sudo{bot_id}.json","r").read()

        if  str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or (user) in owner or int(user) == dev_owner:
                users = len(open(f"Users{bot_id}.json","r").readlines())
                groups = len(open(f"groups{bot_id}.json","r").readlines())
                sudos = len(open(f"sudo{bot_id}.json","r").readlines())
                main = len(open(f"maindevs{bot_id}.json","r").readlines())
                bans = len(open(f"band{bot_id}.json","r").readlines())

                msg = f"""
                **◍ Bot Status : **
                        
                ├ users : {users} 
                ├ sudos : {sudos} 
                ├ groups : {groups} 
                ├ main sudos : {main} 
                ├ band  {bans} 
                
                √ """
                return await m.reply(msg,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("close",callback_data="close")]]))
        return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_callback_query(filters.regex("close"))
async def close__(_,query:CallbackQuery):
        user = query.from_user.id
        mainSudo = open(f"maindevs{bot_id}.json","r").read()
        mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
        sudo = open(f"sudo{bot_id}.json","r").read()

        if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or (user) in owner or int(user) == dev_owner:
                await query.message.delete()

        else:
                await query.answer("❎ فقط المطورين من لديهم الحق في القيام بهذا .")

@app.on_message(filters.command("•---- حذف الكيبورد -----•","")&filters.private)
async def del_keyboard(c:Client,m:Message):
        user = m.from_user.id
        mainSudo = open(f"maindevs{bot_id}.json","r").read()
        mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
        sudo = open(f"sudo{bot_id}.json","r").read()

        if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or (user) in owner or int(user) == dev_owner:
                return await m.reply("**◍ تم حذف الكيبورد بنجاح  /start\n√**",reply_markup=ReplyKeyboardRemove())
        return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(filters.command("^نسخه الكل$","")&filters.private)
async def __get_copy(c:Client,m:Message):
        user = m.from_user.id
        mainSudo = open(f"maindevs{bot_id}.json","r").read()
        mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
        sudo = open(f"sudo{bot_id}.json","r").read()

        if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or (user) in owner or int(user) == dev_owner:
                users = open(f"Users{bot_id}.json","rb")
                groups = open(f"groups{bot_id}.json","rb")
                band = open(f"band{bot_id}.json","rb")
                sudos = open(f"sudo{bot_id}.json","rb")
                main = open(f"maindevs{bot_id}.json","rb")

                uc = len(open(f"Users{bot_id}.json","r").readlines())
                gc = len(open(f"groups{bot_id}.json","r").readlines())
                bc = len(open(f"band{bot_id}.json","r").readlines())
                sc = len(open(f"sudo{bot_id}.json","r").readlines())
                mc = len(open(f"maindevs{bot_id}.json","r").readlines())

                cc = await m.reply("**◍ جاري جلب النسخه الاحتياطية \n√**")
                time.sleep(3)
                await cc.delete()
                try:
                        await m.reply_document(document=users,caption=f"**Bot users : {uc} √**")
                except:
                        await m.reply("**◍ لم يقم اي عضو بالدخول الي بوتك √**")
                try:
                        await m.reply_document(document=groups,caption=f"**Bot groups : {gc} √**")
                except:
                        await m.reply("**◍ لم يتم تفعيل اي مجموعات في بوتك √**")
                try:
                        await m.reply_document(document=band,caption=f"**Band users : {bc} √**")
                except:
                        await m.reply("**◍ لا يوجد اعضاء محظورين في البوت √**")
                try:
                        await m.reply_document(document=sudos,caption=f"**Sudo users : {sc} √**")
                except:
                        await m.reply("**◍ لا يوجد مطورين في البوت √**")
                try:
                        await m.reply_document(document=main,caption=f"**Main devs : {mc} √**")
                except:
                        await m.reply("**◍ لا يوجد مطورين اساسيين في البوت √**")
                return
        return await m.reply("**◍ انت لست مطور في البوت \n√**")



@app.on_message(filters.command("^عرض المجموعات$","")&filters.private)
async def show_groups(c:Client,m:Message):
        user = m.from_user.id
        mainSudo = open(f"maindevs{bot_id}.json","r").read()
        mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
        sudo = open(f"sudo{bot_id}.json","r").read()

        if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or (user) in owner or int(user) == dev_owner:
                groups = open(f"groups{bot_id}.json")
                x = 1
                text = "**Bot groups **:\n\n"
                for gr in groups:
                        text += f"{x} - {gr} \n"
                        x+=1
                i =await m.reply("**◍ جاري عرض الجروبات √**")
                time.sleep(.5)
                leng = len(open(f"groups{bot_id}.json","r").readlines())
                if leng == 0:
                        return await i.edit("**◍ لا توجد مجموعات تم تفعيلها في البوت √**")
                return await i.edit(text=text)
        return await m.reply("**◍ انت لست مطور في البوت \n√**")

#--------------------------Group---------------------------

@app.on_message(filters.command("^نسخه المجموعات$","")&filters.private)
async def __gcopy(c:Client,m:Message):
        user = m.from_user.id
        mainSudo = open(f"maindevs{bot_id}.json","r").read()
        mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
        sudo = open(f"sudo{bot_id}.json","r").read()

        if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or (user) in owner or int(user) == dev_owner:
                gr = open(f"groups{bot_id}.json","rb")
                gc = len(open(f"groups{bot_id}.json","r").readlines())
                i = await m.reply("**◍ جاري جلب نسخه للمجموعات √**")
                time.sleep(1.5)
                try:
                        await i.delete()
                        await m.reply_document(document=gr,caption=f"**Bot groups {gc}**")
                except:
                        await i.delete()
                        await m.reply("**◍ لا توجد مجموعات تم تفعيلها في البوت √**")
                return
        return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(filters.command("^عدد المجموعات$","")&filters.private)
async def get_groups_count(c:Client,m:Message):
        user = m.from_user.id
        mainSudo = open(f"maindevs{bot_id}.json","r").read()
        mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
        sudo = open(f"sudo{bot_id}.json","r").read()

        if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or (user) in owner or int(user) == dev_owner:
                leng = len(open(f"groups{bot_id}.json","r").readlines())
                if leng == 0:
                        return await m.reply("**◍ لا توجد مجموعات تم تفعيلها في البوت √**")
                return await m.reply(f"**◍ ت