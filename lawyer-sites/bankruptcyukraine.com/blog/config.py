import os
H = os.path.dirname(os.path.abspath(__file__))
cfg = dict(
    dir=H, site='bankruptcyukraine.com', live_id=700, hub_id=1397, preview_id=1398,
    logo='Бондар О. О.', full_name='Бондар Олег Олексійович', role='Адвокат зі скасування судових наказів<br>та колекторських дій',
    tg='https://t.me/Oleg_adwokat', phone='+38 (099) 251 50 87', tel='+380992515087', hours='Пн–Пт<br>9:00 — 18:00',
    socials=[('Instagram', 'https://www.instagram.com/oleg_adwokat/'), ('Facebook', 'https://www.facebook.com/profile.php?id=100087526713738')],
    useful=[('Турбо Гроші: кредити, борги, колектори та правовий захист', '/turbo-hroshi-kredyty-borhy-kolektory/'),
            ('Приватні кредитори в Україні: юридичний супровід та права боржників', '/pryvatni-kredytory-v-ukraini/')],
    portrait='https://bankruptcyukraine.com/wp-content/uploads/2025/07/bondar-oleh-oleksiiovych-yuryst-po-kredytam.jpg',
    lead='Пояснюю питання скасування судових наказів, дій колекторів і захисту боржників простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.',
    nav=[('Освіта', 'about'), ('Досвід', 'experience'), ('Результати', 'results'), ('Відгуки', 'reviews'), ('Блог', 'blog'), ('Контакти', 'contacts')],
    btn_style='solid', photo_radius='8px', card_radius='6px', placeholders=12, articles=[],
    fonts=dict(head="Montserrat,sans-serif", head_weight='800', body="'Roboto Condensed',sans-serif",
               **{'import': 'https://fonts.googleapis.com/css2?family=Montserrat:wght@800&family=Roboto+Condensed:wght@400;700&display=swap'}),
    colors=dict(hero_left='#02176D', hero_right='#E4F7FC', hero_text='#FFFFFF', sec_bg='#E4F7FC', sec_title='#222222', sec_text='#4B4F58',
                card_bg='#FFFFFF', card_title='#222222', card_text='#4B4F58', card_meta='#02176D', tag_bg='#FFE16A', tag_fg='#02176D',
                cover_a='#02176D', cover_b='#0B2A9F', btn_bg='#FFE16A', btn_fg='#02176D', btn_hover='#FFFFFF', accent='#FFE16A',
                header_bg='#02176D', header_text='#FFFFFF', footer_bg='#02176D', footer_text='rgba(255,255,255,.85)', footer_title='#FFFFFF', footer_link='#FFE16A'),
)
