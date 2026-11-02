import os
H = os.path.dirname(os.path.abspath(__file__))
cfg = dict(
    dir=H, site='jurist-online.info', live_id=1271, hub_id=2675, preview_id=2676,
    logo='Мельник М. М.', full_name='Мельник Марія Миколаївна', role='Юрист з питань<br>захисту прав споживачів',
    tg='https://t.me/maria_yrist', phone='+38 (099) 232 21 83', tel='+380992322183', hours='Пн–Пт<br>9:00 — 18:00',
    socials=[('Facebook', 'https://www.facebook.com/profile.php?id=100087573902068'), ('Instagram', 'https://www.instagram.com/maria_yrist/')],
    useful=[],
    portrait='https://jurist-online.info/wp-content/uploads/2025/07/melnyk-mariia-mykolaivna-yuryst-po-kredytam.jpg',
    lead='Пояснюю питання захисту прав споживачів кредитних послуг, дій МФО та шахрайських кредитів простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.',
    nav=[('Про мене', 'about'), ('Досвід', 'experience'), ('Результати', 'results'), ('Відгуки', 'reviews'), ('Блог', 'blog'), ('Контакти', 'contacts')],
    btn_style='solid', btn_radius='8px', photo_radius='28px', card_radius='16px', shadow='rgba(102,51,0,.14)', placeholders=12, articles=[],
    fonts=dict(head="Jost,sans-serif", head_weight='600', body="'DM Sans',sans-serif",
               **{'import': 'https://fonts.googleapis.com/css2?family=Jost:wght@500;600&family=DM+Sans:wght@400;700&display=swap'}),
    colors=dict(hero_left='#FCE8CF', hero_right='#FFF6EA', hero_text='#2E1700', sec_bg='#FBF5F1', sec_title='#2E1700', sec_text='#663300',
                card_bg='#FFFFFF', card_title='#2E1700', card_text='#6B5848', card_meta='#B56A00', tag_bg='#FFA500', tag_fg='#2E1700',
                cover_a='#8A4A10', cover_b='#4A2600', btn_bg='#663300', btn_fg='#FFFFFF', btn_hover='#2E1700', accent='#FFA500',
                cta_bg='#FFA500', cta_fg='#2E1700',
                header_bg='#3B1D00', header_text='#FFFFFF', footer_bg='#E7DFD4', footer_text='#66523F', footer_title='#2E1700', footer_link='#663300',
                footer_hover='#2E1700', footer_line='rgba(102,51,0,.25)'),
)
