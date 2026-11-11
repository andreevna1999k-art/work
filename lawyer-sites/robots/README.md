# robots.txt для сайтів юристів
Готові файли `<домен>.txt` (вміст для вставки). На сайтах `robots.txt` -- фізичний файл, через REST API його змінити не можна.
- Сайти з `Disallow: /` (потрібна заміна, інакше блог і статті не скануються): advokato.in.ua, bankruptcyukraine.com, jurist-online.info, jurist-po-ipotechnum-kreditam.kiev.ua, lawmsb.com.ua, pravovid.com.ua, yuristy.in.ua.
- Усім сайтам потрібен рядок `Sitemap:` (його зараз немає ні на одному).
- Yoast SEO (11 сайтів): адмінка -> SEO -> Інструменти -> Редактор файлів -> robots.txt -> вставити вміст -> зберегти.
- Сайти без Yoast (legaladdress, ukrjurist, uchet, urists, spacelaw): додати рядок Sitemap у robots.txt через файловий менеджер хостингу або SEO-плагін сайту.
- Сайти з блоком Content-Signal / ШІ-ботів (rada-advokat, advokat-kharkov, profconsulting, argument-consulting, spacelaw): цей блок додає Cloudflare, його не чіпати, він дописується до вмісту файлу.
- Після збереження перевірити `https://<домен>/robots.txt` і додати сайтмап у Google Search Console.
