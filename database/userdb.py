import aiosqlite
from random import *

DATABASE = 'users.db'

async def setup_database():
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Foydalanuvchi uchun unikal identifikator
                chat_id INTEGER NOT NULL,               -- Foydalanuvchi ID si
                name TEXT NOT NULL,                      -- Ismi
                surname TEXT NOT NULL,                   -- Familyasi
                age INTEGER NOT NULL,                    -- Yoshi
                phone_number TEXT,                       -- Telefon raqami
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        await db.execute('''
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Karta uchun unikal identifikator
                user_id INTEGER NOT NULL,                -- `users` jadvaliga tashqi kalit
                card_number TEXT UNIQUE,                 -- Karta raqami
                card_pin TEXT NOT NULL,                  -- Karta PIN kodi
                balance DECIMAL(15, 2) DEFAULT 0.00,     -- Karta balans summasi
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')

        await db.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,      -- Transaksiya uchun unikal identifikator
                sender_card_number INTEGER NOT NULL,           -- `cards` jadvaliga tashqi kalit
                receiver_card_number INTEGER NOT NULL,         -- `cards` jadvaliga tashqi kalit
                amount DECIMAL(15, 2) NOT NULL,            -- Transaksiya summasi
                description TEXT,                          -- To'lov izohi
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Yaratilgan vaqt
                FOREIGN KEY (sender_card_number) REFERENCES cards(card_number), -- Jo'natuvchi karta uchun bog'lash
                FOREIGN KEY (receiver_card_number) REFERENCES cards(card_number) -- Qabul qiluvchi karta uchun bog'lash
            )
        ''')


        await db.execute('''
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,    -- Xizmat uchun unikal identifikator
                user_id INTEGER NOT NULL,                -- Foydalanuvchi identifikatori
                receiver_phone_number TEXT NOT NULL,     -- Qabul qiluvchining telefon raqami
                amount DECIMAL(15, 2) NOT NULL,          -- Miqdor
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Yaratilgan sana
            )
        ''')

        await db.execute('''
            CREATE TABLE IF NOT EXISTS utilities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,    -- Yozuv uchun unikal identifikator
                user_id INTEGER NOT NULL,               -- Foydalanuvchi identifikatori
                komunal_name TEXT NOT NULL,             -- Kommunal to'lov turi (masalan, "Elektr", "Gaz", "Suv")
                account_number TEXT NOT NULL,           -- Komunal hisob raqami
                summa DECIMAL(15, 2) NOT NULL,          -- To'lov summasi
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Yaratilgan sana
            )
        ''')

        await db.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,    -- To'lov uchun unikal identifikator
                card_id INTEGER NOT NULL,                 -- `cards` jadvaliga tashqi kalit
                service_id INTEGER NOT NULL,              -- `services` jadvaliga tashqi kalit
                amount DECIMAL(15, 2) NOT NULL,           -- To'lov summasi
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (card_id) REFERENCES cards(id),
                FOREIGN KEY (service_id) REFERENCES services(id)
            )
        ''')

        print("Database and tables setup complete!")

async def create_user(chat_id, name, surname, age, number):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute(
            "INSERT INTO users (chat_id, name, surname, age, phone_number) VALUES (?, ?, ?, ?, ?)",
            (chat_id, name, surname, age, number)
        )
        await db.commit()


async def get_user(chat_id):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT * FROM users WHERE chat_id = ?", (chat_id,)) as cursor:
            user = await cursor.fetchall()
            return user 


async def get_cards(chat_id):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT * FROM cards WHERE user_id =?", (chat_id,)) as cursor:
            cards = await cursor.fetchall()
            return cards


async def get_card_by_number(card_number):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT * FROM cards WHERE card_number = ?", (card_number,)) as cursor:
            return await cursor.fetchone()


async def get_card_by_user(chat_id):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT * FROM cards WHERE user_id = ?", (chat_id,)) as cursor:
            return await cursor.fetchone()  # faqat bitta kartani qaytaradi
        

async def get_user_by_phone_number(phone_number):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT * FROM users WHERE phone_number =?", (phone_number,)) as cursor:
            user = await cursor.fetchall()
            return user


async def create_card(user_id, card_number, card_pin, balance=0.00):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("""INSERT INTO cards (user_id, card_number, card_pin, balance) VALUES (?, ?, ?, ?)""",
            (user_id, card_number, card_pin, balance)
        )
        await db.commit()
        print("Card created successfully!")


async def create_transaction(sender_card_number, receiver_card_number, amount, description):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute('''INSERT INTO transactions (sender_card_number, receiver_card_number, amount, description) VALUES (?, ?, ?, ?)''', 
            (sender_card_number, receiver_card_number, amount, description)
        )
        await db.commit()
        print("Transaction completed successfully!")


async def create_services(user_id, receiver_phone_number, amount):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("""INSERT INTO services (user_id, receiver_phone_number, amount) VALUES (?, ?, ?)""",
            (user_id, receiver_phone_number, amount)
        )
        await db.commit()
        print("Service created successfully!")


async def create_utilities(user_id, komunal_name, account_number, amount):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("""INSERT INTO utilities (user_id, komunal_name, account_number, summa) VALUES (?, ?, ?, ?)""",
            (user_id, komunal_name, account_number, amount)
        )
        await db.commit()
        print("Utility created successfully!")

async def user_exists(chat_id):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT * FROM users WHERE chat_id = ?", (chat_id,)) as check_user:
            user = await check_user.fetchone()
        async with db.execute("SELECT * FROM cards WHERE user_id = ?", (chat_id,)) as check_card:
            card = await check_card.fetchone()
        
        return user is not None and card is not None


async def change_password(user_id, now_password, new_password, again_enter_password):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT card_pin FROM cards WHERE user_id = ?", (user_id,)) as cursor:
            user = await cursor.fetchone()
            if user is not None:
                if new_password == again_enter_password:
                    await db.execute("UPDATE cards SET card_pin = ? WHERE user_id = ?", (new_password, user_id))
                    await db.commit()
                    return "Parol muvaffaqiyatli yangilandi!"
                else: 
                    return "Kiritilgan parollar mos kelmadi."
            else:
                return "Eski parol noto‘g‘ri kiritildi."
        

async def update_balance(card_id, new_balance):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("UPDATE cards SET balance = ? WHERE id = ?", (new_balance, card_id))
        await db.commit()
        return "Balans muvaffaqiyatli yangilandi!"