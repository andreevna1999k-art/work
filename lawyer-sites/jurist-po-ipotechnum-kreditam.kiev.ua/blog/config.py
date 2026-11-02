import os
H = os.path.dirname(os.path.abspath(__file__))
cfg = dict(
    dir=H, site='jurist-po-ipotechnum-kreditam.kiev.ua', live_id=590, hub_id=960, preview_id=961,
    logo='Пономаренко В. М.', full_name='Пономаренко Володимир Михайлович', role='Юрист з майнових спорів<br>та арештів',
    tg='https://t.me/Gvm_yrist_la', phone='+38 (050) 691 29 27', tel='+380506912927', hours='Пн–Пт<br>9:00 — 18:00',
    socials=[('Instagram', 'https://www.instagram.com/gvm_yrist_la/'), ('Facebook', 'https://www.facebook.com/profile.php?id=100087217846791')],
    useful=[('ЄАПБ подали в суд: алгоритм дій боржника та судова практика', '/eapb-podaly-v-sud-alhorytm-dii-borzhnyka-ta-sudova-praktyka/'),
            ('Де колектори беруть номера телефонів родичів і чи законно це', '/de-kolektory-berut-nomera-telefoniv-rodichiv-i-chy-zakonn%d0%be-tse/')],
    portrait='https://jurist-po-ipotechnum-kreditam.kiev.ua/wp-content/uploads/2025/07/ponomarenko-volodymyr-mykhailovych-yuryst-po-kredytam.jpg',
    lead='Пояснюю питання іпотеки, арештів майна та майнових спорів простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.',
    nav=[('Освіта', 'about'), ('Досвід', 'experience'), ('Результати', 'results'), ('Відгуки', 'reviews'), ('Блог', 'blog'), ('Контакти', 'contacts')],
    btn_style='solid', btn_radius='0', photo_radius='24px', card_radius='12px', shadow='rgba(0,12,48,.12)', placeholders=6, articles=[],
    fonts=dict(head="'Playfair Display',serif", head_weight='400', body="Poppins,sans-serif",
               **{'import': 'https://fonts.googleapis.com/css2?family=Playfair+Display&family=Poppins:wght@400;500;600&display=swap'}),
    colors=dict(hero_left='#BFE3F2', hero_right='#E8F5FB', hero_text='#000C30', sec_bg='#F2F2F2', sec_title='#000C30', sec_text='#000C30',
                card_bg='#FFFFFF', card_title='#000C30', card_text='#4A5470', card_meta='#0A8BB5', tag_bg='#0EB2E7', tag_fg='#FFFFFF',
                cover_a='#0A6F90', cover_b='#000C30', btn_bg='#000C30', btn_fg='#FFFFFF', btn_hover='#0EB2E7', accent='#0EB2E7',
                cta_bg='#0EB2E7', cta_fg='#FFFFFF',
                header_bg='#000C30', header_text='#FFFFFF', footer_bg='#000C30', footer_text='rgba(255,255,255,.85)', footer_title='#FFFFFF', footer_link='#7FD6F5',
                footer_hover='#FFFFFF'),
)
