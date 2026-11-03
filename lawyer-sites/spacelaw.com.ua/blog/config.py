import os
H = os.path.dirname(os.path.abspath(__file__))
cfg = dict(
    dir=H, site='spacelaw.com.ua', live_id=49, hub_id=1504, preview_id=1505,
    logo='Олійник Є. Л.', full_name='Олійник Євгенія Леонідівна', role='Юристка з кредитних спорів,<br>банківського права та неплатоспроможності',
    tg='https://t.me/yrist_olynyk', phone='+380 99 497 17 38', tel='+380994971738', hours='Пн–Пт<br>9:00 — 18:00',
    socials=[('Telegram', 'https://t.me/yrist_olynyk')],
    useful=[],
    portrait='https://spacelaw.com.ua/wp-content/uploads/2026/03/oliinyk-yevheniia-leonidivna-1.jpg',
    lead='Пояснюю питання кредитних спорів, банківського права та процедур неплатоспроможності простою мовою: що каже закон і що варто зробити в першу чергу.',
    nav=[('Про себе', 'about'), ('Досвід', 'experience'), ('Відгуки', 'reviews'), ('Блог', 'blog'), ('Контакти', 'contacts')],
    btn_style='solid', btn_radius='6px', photo_radius='24px', card_radius='14px', shadow='rgba(101,40,247,.14)', placeholders=12, articles=[],
    fonts=dict(head="Inter,sans-serif", head_weight='600', body="Inter,sans-serif",
               **{'import': 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap'}),
    colors=dict(hero_left='#F2F0FE', hero_right='#E8E3FD', hero_text='#0F172A', sec_bg='#F2F0FE', sec_title='#0F172A', sec_text='#454F5E',
                card_bg='#FFFFFF', card_title='#0F172A', card_text='#454F5E', card_meta='#6528F7', tag_bg='#6528F7', tag_fg='#FFFFFF',
                cover_a='#6528F7', cover_b='#0F172A', btn_bg='#6528F7', btn_fg='#FFFFFF', btn_hover='#0F172A', accent='#6528F7',
                cta_bg='#6528F7', cta_fg='#FFFFFF',
                header_bg='#0F172A', header_text='#FFFFFF', footer_bg='#0F172A', footer_text='rgba(255,255,255,.85)', footer_title='#FFFFFF', footer_link='#C4B2FF',
                footer_hover='#FFFFFF'),
)
