import os
H = os.path.dirname(os.path.abspath(__file__))
cfg = dict(
    dir=H, site='advokat-kharkov.org.ua', live_id=24, hub_id=1205, preview_id=1206,
    logo='Дорошенко Є. С.', full_name='Дорошенко Євгеній Сергійович', role='Юрист з судового захисту<br>та апеляцій',
    tg='https://t.me/yrist_evgen', phone='+38 (050) 510 06 61', tel='+380505100661', hours='Пн–Пт<br>9:00 — 18:00',
    socials=[('Instagram', 'https://www.instagram.com/yrist_evgen/'),
             ('Facebook', 'https://www.facebook.com/people/%D0%84%D0%B2%D0%B3%D0%B5%D0%BD%D1%96%D0%B9-%D0%94%D0%BE%D1%80%D0%BE%D1%88%D0%B5%D0%BD%D0%BA%D0%BE/pfbid02WQadoHpiT3zGWebZCWBVgekqSg66RZKr5cmc4jhW4WpMUeNSJhMGd1ZpdTTMjXF5l/')],
    useful=[('Як захиститися від вимог Алекс Кредит: поради юриста', '/yak-zakhystytysia-vid-vymoh-aleks-kredyt-porady-yurysta/'),
            ('Боргова яма: як вибратися законно, поради юриста', '/borhova-yama-yak-vybratysia-zakonno-porady-yurysta/')],
    portrait='https://advokat-kharkov.org.ua/wp-content/uploads/2025/07/doroshenko-yevhenii-serhiiovych-yuryst-po-kredytam.png',
    lead='Пояснюю питання судового захисту позичальників, апеляцій і касацій простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.',
    nav=[('Освіта', 'about'), ('Досвід', 'experience'), ('Результати', 'results'), ('Відгуки', 'reviews'), ('Блог', 'blog'), ('Контакти', 'contacts')],
    btn_style='solid', btn_radius='50px', photo_radius='20px', card_radius='14px', shadow='rgba(29,96,150,.16)', placeholders=12, articles=[],
    fonts=dict(head="Roboto,sans-serif", head_weight='500', body="Montserrat,sans-serif",
               **{'import': 'https://fonts.googleapis.com/css2?family=Roboto:wght@300;500;700&family=Montserrat:wght@400;600;700&display=swap'}),
    colors=dict(hero_left='#CBE6EF', hero_right='#E3F1F7', hero_text='#0E2F4A', sec_bg='#E9F4FB', sec_title='#1D6096', sec_text='#5A6470',
                card_bg='#FFFFFF', card_title='#0E2F4A', card_text='#5A6470', card_meta='#1D6096', tag_bg='#FFB716', tag_fg='#0E2F4A',
                cover_a='#1D6096', cover_b='#0E2F4A', btn_bg='#1D6096', btn_fg='#FFFFFF', btn_hover='#0E2F4A', accent='#FFB716',
                header_bg='#0E2F4A', header_text='#FFFFFF', footer_bg='#18181B', footer_text='rgba(255,255,255,.85)', footer_title='#FFB716', footer_link='#FFFFFF',
                footer_hover='#FFB716'),
)
