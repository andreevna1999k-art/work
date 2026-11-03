import os
H = os.path.dirname(os.path.abspath(__file__))
cfg = dict(
    dir=H, site='profconsulting.com.ua', live_id=576, hub_id=917, preview_id=918,
    logo='Алексєєв О. М.', full_name='Алексєєв Олег Михайлович', role='Юрист з кредитних спорів,<br>реструктуризації та банкрутства',
    tg='https://t.me/urist_oleg_alekseev', phone='+38 (050) 940 00 26', tel='+380509400026', hours='Пн–Пт<br>9:00 — 18:00',
    socials=[('Instagram', 'https://www.instagram.com/yrist_alekseev/'), ('Facebook', 'https://www.facebook.com/profile.php?id=100092597117337')],
    useful=[('Нелегальні МФО: повний список та як перевірити легальність', '/nelehalni-mfo-povnyi-spysok-ta-yak-pereviryty-lehalnist/'),
            ('Що робити, якщо колектори подали в суд: алгоритм захисту боржника', '/shcho-robyty-yakshcho-kolektory-podaly-v-sud/')],
    portrait='https://profconsulting.com.ua/wp-content/uploads/2025/07/alekseev-oleg-mykhailovych-yuryst-po-kredytam.jpg',
    lead='Пояснюю питання кредитних спорів, МФО, реструктуризації, банкрутства та боротьби з колекторами простою мовою: що каже закон і що варто зробити в першу чергу.',
    nav=[('Освіта', 'about'), ('Досвід', 'experience'), ('Результати', 'results'), ('Відгуки', 'reviews'), ('Блог', 'blog'), ('Контакти', 'contacts')],
    btn_style='solid', btn_radius='5px', photo_radius='20px', card_radius='14px', shadow='rgba(15,23,42,.12)', placeholders=12, articles=[],
    fonts=dict(head="Poppins,sans-serif", head_weight='700', body="Poppins,sans-serif",
               **{'import': 'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap'}),
    colors=dict(hero_left='#FFFFFF', hero_right='#EDFBE2', hero_text='#0F172A', sec_bg='#EDFBE2', sec_title='#0F172A', sec_text='#2F3B40',
                card_bg='#FFFFFF', card_title='#0F172A', card_text='#2F3B40', card_meta='#379237', tag_bg='#54B435', tag_fg='#FFFFFF',
                cover_a='#54B435', cover_b='#1E5A1E', btn_bg='#54B435', btn_fg='#FFFFFF', btn_hover='#379237', accent='#54B435',
                header_bg='#0F172A', header_text='#FFFFFF', footer_bg='#D5EAD8', footer_text='#2F3B40', footer_title='#0F172A', footer_link='#379237',
                footer_hover='#0F172A', footer_line='rgba(15,23,42,.2)'),
)
