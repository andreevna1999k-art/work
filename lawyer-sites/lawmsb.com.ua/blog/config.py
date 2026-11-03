import os
H = os.path.dirname(os.path.abspath(__file__))
cfg = dict(
    dir=H, site='lawmsb.com.ua', live_id=3638, hub_id=3766, preview_id=3767,
    logo='Коваленко В. С.', full_name='Коваленко Володимир Сергійович', role='Юрист з переговорів з банками<br>та реструктуризації боргів',
    tg='https://t.me/Kovalenko_la_co_ua', phone='+38 (099) 251 50 87', tel='+380992515087', hours='Пн–Пт<br>9:00 — 18:00',
    socials=[('Instagram', 'https://www.instagram.com/kovalenko_la_co_ua/'), ('Facebook', 'https://www.facebook.com/profile.php?id=100092142673410')],
    useful=[('БІ ЕЛ ДЖИ МІКРОФІНАНС: огляд, умови, права боржника та захист', '/bi-el-dzhy-mikrofinans/'),
            ('Укр Кредит Фінанс суд: огляд рішень, права боржників і практика', '/ukr-kredyt-finans-sud-ohliad-rishen-prava-borzhnykiv-i-praktyka/')],
    portrait='https://lawmsb.com.ua/wp-content/uploads/2025/07/kovalenko-volodymyr-serhiiovych-kredytnyi-yuryst.jpg',
    lead='Пояснюю питання переговорів з банками, реструктуризації та позасудового врегулювання боргів простою мовою: що каже закон і що варто зробити в першу чергу.',
    nav=[('Про мене', 'about'), ('Досвід', 'experience'), ('Результати', 'results'), ('Відгуки', 'reviews'), ('Блог', 'blog'), ('Контакти', 'contacts')],
    btn_style='solid', btn_radius='5px', photo_radius='20px', card_radius='14px', shadow='rgba(15,23,42,.12)', placeholders=12, articles=[],
    fonts=dict(head="'Playfair Display',serif", head_weight='600', body="'Open Sans',sans-serif",
               **{'import': 'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Open+Sans:wght@400;600;700&display=swap'}),
    colors=dict(hero_left='#DCE2E4', hero_right='#EAEEEF', hero_text='#0F172A', sec_bg='#EDF6EE', sec_title='#0F172A', sec_text='#454F5E',
                card_bg='#FFFFFF', card_title='#0F172A', card_text='#454F5E', card_meta='#178E79', tag_bg='#1B9C85', tag_fg='#FFFFFF',
                cover_a='#1B9C85', cover_b='#0F172A', btn_bg='#1B9C85', btn_fg='#FFFFFF', btn_hover='#0F172A', accent='#1B9C85',
                header_bg='#0F172A', header_text='#FFFFFF', footer_bg='#222222', footer_text='rgba(255,255,255,.85)', footer_title='#FFFFFF', footer_link='#7FE0CB',
                footer_hover='#FFFFFF'),
)
