# Настройки облачного окружения (для восстановления)

Записано 27.10.2026 со скриншотов окна «Изменить облачную среду». Паролей и значений секретов здесь нет, их показать нельзя.

## Доступ к сети
- Был «Ограниченный» со списком из 33 разрешённых доменов (в основном юридические сайты Румынии и Польши, api.openai.com и пакетные менеджеры).
- Выбран «Полный» (при сохранении 33 домена удаляются).
- Чтобы вернуть защиту: Edit → «Доступ к сети» → «Ограниченный».

## Сетевые секреты (правила WordPress, доступ только к /wp-json/)
advokat-kharkov.org.ua, advokato.in.ua, argument-consulting.com.ua, bankruptcyukraine.com,
jurist-online.info, jurist-po-ipotechnum-kreditam.kiev.ua, lawmsb.com.ua, legaladdress.com.ua,
pravovid.com.ua, profconsulting.com.ua, rada-advokat.uz.ua, spacelaw.com.ua,
uchet.com.ua, ukrjurist.com.ua, urists.com.ua, yuristy.in.ua
(все с путём /wp-json/)

## Скрипт настройки
Пустой (подсказка по умолчанию «#!/bin/bash npm install»).
