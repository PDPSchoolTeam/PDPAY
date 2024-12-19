#PDPAY

PDPAYBot — foydalanuvchilarga o‘z to‘lovlarini boshqarish, hisoblarni tekshirish va tranzaksiyalarni amalga oshirish imkonini beruvchi Telegram bot. Ushbu bot orqali foydalanuvchilar o‘z hisoblariga kirish, balansni tekshirish, to‘lovlarni amalga oshirish va tranzaksiyalar tarixini ko‘rishlari mumkin.
Xususiyatlar

    Hisobni boshqarish: Foydalanuvchilar o‘z hisoblariga kirishlari va ma'lumotlarini yangilashlari mumkin.
    Balansni tekshirish: Joriy balansni ko‘rish imkoniyati.
    To‘lovlarni amalga oshirish: Turli xizmatlar uchun to‘lovlarni amalga oshirish.
    Tranzaksiyalar tarixi: Oldingi tranzaksiyalarni ko‘rish va kuzatish.

O‘rnatish

Loyihani klonlash:

    git clone https://github.com/PDPSchoolTeam/PDPAY.git
    cd PDPAY

Virtual muhit yaratish (ixtiyoriy, lekin tavsiya etiladi):

    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows

Talab qilinadigan kutubxonalarni o‘rnatish:

    pip install -r requirements.txt

Sozlash

    config.py faylini tahrirlash: Bot sozlamalarini moslashtirish uchun config.py faylini o‘zgartiring.

Ma'lumotlar bazasi sozlamalari: database papkasidagi fayllarni tekshiring va kerakli sozlamalarni kiriting.

Ishga tushirish

    python main.py


Hissa qo‘shish

Hissangizni qo‘shish uchun quyidagi amallarni bajaring:

    Ushbu repozitoriyani fork qiling.
    O‘zingizning branch'ingizni yarating: git checkout -b my-feature
    O‘zgarishlarni kiriting va commit qiling: git commit -m 'Yangi xususiyat qo‘shildi'
    O‘zgarishlarni push qiling: git push origin my-feature
    Pull request yarating.

Litsenziya

Ushbu loyiha MIT litsenziyasi ostida tarqatiladi. Qo‘shimcha ma'lumot uchun LICENSE faylini ko‘ring.
Aloqa

Savollar yoki takliflar uchun loyiha mualliflariga GitHub orqali murojaat qiling.
