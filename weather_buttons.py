from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

city = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Navoiy", callback_data="погода-навои"),],
        [InlineKeyboardButton(text="Toshkent", callback_data="погода-ташкент"),],
        [InlineKeyboardButton(text="Samarqand", callback_data="погода-самарканд"),],
        [InlineKeyboardButton(text="Buxoro", callback_data="погода-бухара"),],
        [InlineKeyboardButton(text="Andijon", callback_data="погода-андижан"),],
        [InlineKeyboardButton(text="Guliston", callback_data="погода-гулистан"),],
        [InlineKeyboardButton(text="Qarshi", callback_data="погода-карши"),]
        
        
    ]
    
)

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ortga", callback_data='back')]
        
    ]
    
)