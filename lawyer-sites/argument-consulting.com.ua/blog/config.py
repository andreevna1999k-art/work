import os
H = os.path.dirname(os.path.abspath(__file__))
cfg = dict(
    dir=H, site='argument-consulting.com.ua', live_id=1287, hub_id=1522, preview_id=1523,
    logo='Бойчук Т. О.', full_name='Бойчук Тетяна Олегівна', role='Юрист відділу супроводу<br>кредитних операцій',
    tg='https://t.me/tatiana_yrist', phone='+38 (075) 492 19 80', tel='+380754921980', hours='Пн–Пт<br>9:00 — 18:00',
    socials=[('Telegram', 'https://t.me/tatiana_yrist')],
    useful=[('Антиколектор МФО: як захистити себе від колекторів та МФО', '/antykollektor-mfo-yak-zakhystyty-sebe-vid-kolektoriv-ta-mfo/'),
            ('Як колектори дізнаються номери телефонів та як захистити себе', '/yak-kolektory-diznayutsya-nomery-telefoniv/')],
    portrait='https://argument-consulting.com.ua/wp-content/uploads/2025/12/Tetiana-Boichuk5-741x1024.webp',
    lead='Пояснюю питання реструктуризації кредитів, аналізу договорів і кредитних карток простою мовою: що каже закон і що варто зробити в першу чергу.',
    nav=[('Освіта', 'about'), ('Досвід', 'experience'), ('Приклади', 'results'), ('Відгуки', 'reviews'), ('Блог', 'blog'), ('Контакти', 'contacts')],
    btn_style='solid', btn_radius='100px', photo_radius='20px', card_radius='14px', shadow='rgba(52,63,30,.14)', placeholders=12, articles=[],
    fonts=dict(head="Marcellus,serif", head_weight='400', body="Inter,sans-serif",
               **{'import': 'https://fonts.googleapis.com/css2?family=Marcellus&family=Inter:wght@400;600;700&display=swap'}),
    colors=dict(hero_left='#4A4540', hero_right='#343F1E', hero_text='#FDFAF1', sec_bg='#E3E9D8', sec_title='#343F1E', sec_text='#343F1E',
                card_bg='#FDFAF1', card_title='#343F1E', card_text='#4B5535', card_meta='#5C8607', tag_bg='#5C8607', tag_fg='#FDFAF1',
                cover_a='#70A309', cover_b='#343F1E', btn_bg='#5C8607', btn_fg='#FDFAF1', btn_hover='#343F1E', accent='#70A309',
                header_bg='#343F1E', header_text='#FDFAF1', footer_bg='#343F1E', footer_text='rgba(253,250,241,.85)', footer_title='#FDFAF1', footer_link='#B8D96B',
                footer_hover='#FFFFFF'),
)
