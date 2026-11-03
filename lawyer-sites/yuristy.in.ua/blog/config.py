import os
H = os.path.dirname(os.path.abspath(__file__))
cfg = dict(
    dir=H, site='yuristy.in.ua', live_id=127, hub_id=25521, preview_id=25522,
    logo='Хмельницький М. В.', full_name='Хмельницький Максим Валерійович', role='Провідний юрист<br>з кредитних спорів',
    tg='https://t.me/max_yrist', phone='+38 (050) 820 21 76', tel='+380508202176', hours='Пн–Пт<br>9:00 — 18:00',
    socials=[('Instagram', 'https://www.instagram.com/max_yrist/'), ('Facebook', 'https://www.facebook.com/profile.php?id=100087415990477'),
             ('LinkedIn', 'https://www.linkedin.com/in/%D0%BC%D0%B0%D0%BA%D1%81%D0%B8%D0%BC-%D1%85%D0%BC%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D1%8C%D0%BA%D0%B8%D0%B9-403754370/')],
    useful=[('Як закрити борг в Таліон Плюс за тіло кредиту: юридичний алгоритм', '/yak-zakryty-borh-v-talion-plyus-za-tilo-kredytu/'),
            ('Crypsee антиколлектор: как защититься от угроз, долгов и мошенников', '/crypsee-antikollektor-zashchita-ot-dolgov/')],
    portrait='https://yuristy.in.ua/wp-content/uploads/2025/07/khmelnytskyi-maksym-valeriiovych-yuryst-po-kredytam.jpg',
    lead='Пояснюю питання кредитних спорів, судових наказів і скасування рішень простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.',
    nav=[('Освіта', 'about'), ('Досвід', 'experience'), ('Результати', 'results'), ('Відгуки', 'reviews'), ('Блог', 'blog'), ('Контакти', 'contacts')],
    btn_style='solid', btn_radius='4px', photo_radius='50%', card_radius='12px', shadow='rgba(36,42,54,.14)', placeholders=12, articles=[],
    fonts=dict(head="Poppins,sans-serif", head_weight='700', body="'Open Sans',sans-serif",
               **{'import': 'https://fonts.googleapis.com/css2?family=Poppins:wght@700&family=Open+Sans:wght@400;600;700&display=swap'}),
    colors=dict(hero_left='#3E4E8A', hero_right='#3E4E8A', hero_text='#FFFFFF', sec_bg='#D9DDEE', sec_title='#000F23', sec_text='#67757F',
                card_bg='#FFFFFF', card_title='#000F23', card_text='#67757F', card_meta='#1A5CE0', tag_bg='#1A5CE0', tag_fg='#FFFFFF',
                cover_a='#3E4E8A', cover_b='#242A36', btn_bg='#1A5CE0', btn_fg='#FFFFFF', btn_hover='#000F23', accent='#1A5CE0',
                cta_bg='#1A5CE0', cta_fg='#FFFFFF',
                header_bg='#242A36', header_text='#FFFFFF', footer_bg='#242A36', footer_text='rgba(255,255,255,.85)', footer_title='#FFFFFF', footer_link='#8FB1FF',
                footer_hover='#FFFFFF'),
)
