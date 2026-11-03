import os
H = os.path.dirname(os.path.abspath(__file__))
cfg = dict(
    dir=H, site='pravovid.com.ua', live_id=989, hub_id=1261, preview_id=1262,
    logo='Вишневський С. О.', full_name='Вишневський Сергій Олександрович', role='Старший юрист<br>з виконавчого провадження',
    tg='https://t.me/yrist_visnewskyi', phone='+38 (099) 540 30 24', tel='+380995403024', hours='Пн–Пт<br>9:00 — 18:00',
    socials=[('Instagram', 'https://www.instagram.com/yrist_visnewskyi/'), ('Facebook', 'https://www.facebook.com/profile.php?id=100087419410685'),
             ('LinkedIn', 'https://www.linkedin.com/in/%D1%81%D0%B5%D1%80%D0%B3%D1%96%D0%B9-%D0%B2%D0%B8%D1%88%D0%BD%D0%B5%D0%B2%D1%81%D1%8C%D0%BA%D0%B8%D0%B9-24b414371/')],
    useful=[('Чи можна відкрити ФОП, якщо є кредит: правові нюанси', '/chy-mozhna-vidkryty-fop-yakshcho-ie-kredyt-pravovi-niuansy/'),
            ('Кредит Капітал антиколектор: як захиститись боржнику', '/kredyt-kapital-antykolektor-yak-zakhystytys-borzhnyku/')],
    portrait='https://pravovid.com.ua/wp-content/uploads/2025/07/vyshnevskyi-serhii-oleksandrovych-yuryst-po-kredytam.jpg',
    lead='Пояснюю питання виконавчого провадження, арештів рахунків і майна та реєстру боржників простою мовою: що каже закон і що варто зробити в першу чергу.',
    nav=[('Освіта', 'about'), ('Досвід', 'experience'), ('Результати', 'results'), ('Відгуки', 'reviews'), ('Блог', 'blog'), ('Контакти', 'contacts')],
    btn_style='solid', btn_radius='100px', photo_radius='20px', card_radius='14px', shadow='rgba(82,37,248,.16)', placeholders=12, articles=[],
    fonts=dict(head="'Nunito Sans',sans-serif", head_weight='800', body="Roboto,sans-serif",
               **{'import': 'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@700;800&family=Roboto:wght@400;500;700&display=swap'}),
    colors=dict(hero_left='#AB46F8', hero_right='#5225F8', hero_text='#FFFFFF', sec_bg='#F5F1F8', sec_title='#111111', sec_text='#333333',
                card_bg='#FFFFFF', card_title='#111111', card_text='#555555', card_meta='#7A2FE0', tag_bg='#F86754', tag_fg='#FFFFFF',
                cover_a='#AB46F8', cover_b='#5225F8', btn_bg='#F86754', btn_fg='#FFFFFF', btn_hover='#5225F8', accent='#F86754',
                header_bg='#3B1A8C', header_text='#FFFFFF', footer_bg='#6A2FF5', footer_text='rgba(255,255,255,.9)', footer_title='#FFFFFF', footer_link='#FFFFFF',
                footer_hover='#FFD3CC'),
)
