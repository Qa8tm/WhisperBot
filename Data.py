from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
اهلا {}.
مرحبا بك في {}

انا بوت همسه 

يمكنك ارسال همسة لأي شخص في القنوات والكروبات (حتى وان لم اكن في القناة).
فقط الشخص الذي تم ارسال اليه الهمسه يمكنه رؤيتها. 

لرؤيه كيفيه الاستخدام اضغط 'كيف اكتب همسه' في الاسفل.

المطور @K_8_U
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 كتابه همسه 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 رجوع 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 كتابه همسه 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("كيف اكتتب همسه ❔", callback_data="help"),
            InlineKeyboardButton("🎪 حول البوت 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("🎨 قناة السورس 🎨", url="https://t.me/ADWSL")],
    ]

    # Help Message
    HELP = """
فقط اكتب الرساله كالنمط في الاسفل.

`@azkarkbot رسالتك + يوزر `
    """

    # About Message
    ABOUT = """
**حول البوت** 

البوت  @azkarkbot

قناة السورس : [اضغط هنا](t.me/ADWSL)

المكتبه : [Pyrogram](docs.pyrogram.org)

لغه البرمجه : [Python](www.python.org)

المطور : @K_8_U
    """
