# -*- coding: utf-8 -*-
"""Собирает index.html (русский) и en/index.html (английский) из одного источника.
Запуск из корня репозитория: python3 _src/build.py"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape

def gallery(kind):
    if kind == 'joyka':
        return '''<div class="stage joyka">
<div class="phone t1"><img src="/img/joyka-home.webp" alt="{a1}" width="589" height="1280"></div>
<div class="phone t2"><img src="/img/joyka-timer.webp" alt="{a2}" width="589" height="1280"></div>
<div class="phone t1"><img src="/img/joyka-settings.webp" alt="{a3}" width="589" height="1280"></div>
<div class="phone t2"><img src="/img/joyka-stats.webp" alt="{a4}" width="589" height="1280"></div></div>'''
    if kind == 'rg':
        return '''<div class="stage rg">
<div class="phone t1"><img src="/img/rg-lobby.webp" alt="{a1}" width="645" height="1170"></div>
<div class="phone t2"><img src="/img/rg-market.webp" alt="{a2}" width="630" height="1030"></div></div>'''
    if kind == 'w12':
        return '''<div class="stage w12">
<div class="desk"><div class="bar"><i></i><i></i><i></i></div><img src="/img/w12-dashboard.webp" alt="{a1}" width="1280" height="713"></div>
<div class="desk-row">
<div class="desk"><div class="bar"><i></i><i></i><i></i></div><img src="/img/w12-landing.webp" alt="{a2}" width="1280" height="535"></div>
<div class="desk"><div class="bar"><i></i><i></i><i></i></div><img src="/img/w12-wheel.webp" alt="{a3}" width="1280" height="509"></div></div></div>'''
    return '''<div class="stage oyf">
<div class="widget"><img src="/img/oyf-timer.webp" alt="{a1}" width="528" height="854"></div>
<div class="desk"><div class="bar"><i></i><i></i><i></i></div><img src="/img/oyf-city.webp" alt="{a2}" width="1280" height="844"></div></div>'''

# ---------------------------------------------------------------- RU
RU = dict(
  lang='ru', title='Андрей Перепечай — Product Owner, Project Manager',
  desc='Портфолио: четыре продукта с задачей, ролью, результатом и метриками. Product Owner и Project Manager.',
  alt_url='/en/', alt_label='EN', cur_label='RU',
  nav=[('#cases','Кейсы'),('#about','Опыт'),('#contact','Контакты')],
  h1='Product Owner и Project Manager',
  lead='Три года в корпоративных ИТ-проектах. Четыре собственных продукта: от исследования до рабочей версии.',
  cta1='Смотреть кейсы', cta2='Написать в Telegram',
  facts=[('3 команды','около 10 человек в каждой. Платформа банковских расчётов, Axenix: бюджет, нагрузка команд, эскалации заказчика.'),
         ('20 000','пользователей корпоративной базы знаний с нейросетевым поиском. СИБУР.'),
         ('4 продукта','от идеи до рабочей версии. Ниже: задача, роль, результат, метрики.'),
         ('50+','человек играли в онлайн-игру «Растущий город».')],
  cases_h='Кейсы', expand='Развернуть все', collapse='Свернуть все',
  l_problem='Задача', l_role='Роль', l_done='Что сделано', l_result='Результат',
  l_tools='Инструменты', l_metrics='Метрики', l_lesson='Вывод',
  m_head=('Метрика','Как считается','Цель'),
  m_note='Цели — ориентиры, которые я задал бы продукту. Это не измеренные результаты.',
  m_main='главная метрика',
  peek_task='Задача', peek_res='Результат',
  about_h='Опыт', contact_h='Контакты',
  about=[('Axenix, Project Manager','Платформа банковских расчётов. Три команды по 10 человек. Бюджет, загрузка команд, эскалации заказчика.'),
         ('Технологии Доверия','Запуск пробной версии продукта на нейросетях для казначейства. Исследование рынка цифровых финансовых активов: регулирование и кейсы.'),
         ('СИБУР','Корпоративная база знаний с поиском на нейросети. Подключена вся компания, около 20 000 пользователей.'),
         ('Образование','Юридическое: правовое обеспечение национальной безопасности.')],
  cases=[
   dict(kind='joyka', n='01', name='Joyka', one='Мобильное приложение коротких медитаций для людей под стрессом.',
     tags=['Product Owner','iOS','Разработчик и дизайнер в команде'],
     peek_task='снизить стресс за 4–5 минут.', peek_res='8 сценариев, 3 голоса, статистика серий. Приложение для iOS.',
     alts=['Joyka: главный экран со списком медитаций','Joyka: экран медитации «Удержи аппетит»','Joyka: настройки звуков и голоса','Joyka: личная статистика'],
     problem='Людям под стрессом нужна быстрая практика. Длинные общие курсы не подходят для ситуации «сейчас».',
     role='Product Owner. Исследование рынка, анализ аудитории, анкетирование. Требования для разработчика и дизайнера. Код и дизайн делали они.',
     done=['Исследовал рынок и аудиторию, провёл анкетирование.','Выделил 8 ситуаций по 4–5 минут: сон, напряжение, аппетит, решение и другие.','Описал настройки: метроном, звуки природы, музыка 432 Гц, 3 голоса, отдельная громкость каждого слоя.','Добавил возврат пользователя: ежедневное напоминание, серия дней, статистика по каждой медитации.'],
     tiles=[('8','сценариев'),('3','голоса'),('3','слоя звука'),('4–5 мин','одна сессия')],
     result_pts=['Готовое приложение для iOS с личной статистикой и серией.'],
     tools=['Анкетирование','Анализ рынка','Анализ аудитории'],
     metrics=[('Частота',True,'Завершённые сессии на активного пользователя в неделю','3'),('Активация',False,'Новые пользователи, завершившие первую сессию в день установки','60%'),('Завершаемость',False,'Завершённые сессии / начатые','70%'),('Возврат на 7-й день',False,'Пользователи, вернувшиеся на 7-й день','20%')],
     lesson='Заложил бы события аналитики в первую версию: без них непонятно, какие сценарии возвращают людей.'),
   dict(kind='rg', n='02', name='Растущий город', one='Онлайн-игра в браузере: партия за один клик, боты, лобби по ссылке.',
     tags=['Product Owner','Project Manager','Веб','Полный цикл'],
     peek_task='играть без ожидания компании.', peek_res='50+ игроков, 3 языка, аналитика партий, проиндексирован в Google и Яндексе.',
     alts=['Растущий город: лобби','Растущий город: рынок и ход игрока'],
     problem='Для настольной игры нужна компания. Собрать людей в один момент трудно.',
     role='Product Owner и Project Manager в одном лице: идея, правила, баланс, приоритеты, релизы, аналитика. Код писал с Claude и Cursor.',
     done=['«Быстрая игра»: партия стартует сразу, свободные места занимают 6 ботов-персонажей.','Лобби по ссылке с PIN-кодом, 3 режима длины партии.','Баланс карт: две итерации. Туториал, чат с реакциями, исключение игроков.','Интерфейс на русском, английском и испанском.','Исправил блокировку соединения, потерю связи игрока и мобильную вёрстку.'],
     tiles=[('50+','игроков'),('2','поисковика: сайт подтверждён'),('1','админ-панель с аналитикой партий')],
     result_pts=['Собственная аналитика партий.','Запуск на своём домене с SSL.','Хостинг не продлён, публичной ссылки сейчас нет.'],
     tools=['Claude','Cursor','React','Node.js','Socket.io','SQLite','nginx','Git'],
     metrics=[('Партии на игрока',True,'Завершённые партии на игрока в неделю','3'),('Первая партия',False,'Игроки, дошедшие до конца первой партии','80%'),('Возврат на следующий день',False,'Игроки, вернувшиеся на второй день','25%'),('Время до старта',False,'От нажатия до первого хода','10 сек')],
     lesson='Запустил бы закрытый тест на 10–15 игроках и опрос после первой партии до расширения контента.'),
   dict(kind='w12', n='03', name='Week12', one='Сервис планирования целей по методологии «12 недель».',
     tags=['Product Owner','Project Manager','Веб','Первый продукт'],
     peek_task='связать цель на год с задачами недели.', peek_res='4 уровня целей, колесо жизни по 8 сферам, ретроспективы. Проект закрыт.',
     alts=['Week12: дашборд цикла','Week12: главная страница','Week12: колесо жизни'],
     problem='Большая цель теряется без связи с действиями недели.',
     role='Product Owner и Project Manager. Перенёс консалтинговую методологию достижения целей в сервис.',
     done=['Иерархия целей: вектор, цели года, цели сезона, задачи.','Дашборд: прогресс цикла, фокус недели, карта 12 недель.','Колесо жизни по 8 сферам, еженедельные ретроспективы, награда за завершённый сезон.','Онбординг с самооценкой, письма-напоминания, админ-панель.','Требования 152-ФЗ: согласие на cookie, политика обработки данных.'],
     tiles=[('4','уровня целей'),('12','недель в цикле'),('8','сфер жизни'),('1','полный путь пользователя')],
     result_pts=['Рабочий путь от регистрации до завершения сезона.','Защита: ограничение попыток входа в админку, права на уровне строк в базе.','Проект закрыт. Был проверкой методологии на практике.'],
     tools=['Cursor','Next.js','TypeScript','Supabase','Vercel','Tailwind'],
     metrics=[('Выполнение недели',True,'Выполненные задачи недели / запланированные','70%'),('Активация',False,'Создана первая цель в день регистрации','70%'),('Возврат на 2-й неделе',False,'Пользователи, вернувшиеся на 2-й неделе','40%'),('Завершённые сезоны',False,'Сезоны, дошедшие до недели 12','15%')],
     lesson='Начал бы с проверки спроса: страница с описанием и 10 интервью до разработки полной иерархии целей.'),
   dict(kind='oyf', n='04', name='Own Your Future', one='Приложение для Windows: время на цели превращается в этажи города.',
     tags=['Product Owner','Project Manager','Windows','Игровая механика'],
     peek_task='показать накопленный прогресс по долгим целям.', peek_res='Рабочая версия: таймер, город, монеты, серия дней.',
     alts=['Own Your Future: таймер сессии','Own Your Future: город и активная сессия'],
     problem='Таймеры считают часы, но не показывают накопленный результат по долгой цели.',
     role='Product Owner и Project Manager. Продуктовый бриф, механика, приоритеты версий, требования к интерфейсу. Разработка с Claude.',
     done=['Механика: одна сессия добавляет этаж, высота пропорциональна времени.','3 направления: «Работа», «Развитие», «Развлечения», плюс свои.','Монеты за этажи, здания для отдыха на монеты.','Здание не закрывается: цель только маркер, навык можно растить дальше.','Окно-виджет без системной рамки, фиксированного размера.'],
     tiles=[('3','направления'),('3','раздела: таймер, город, настройки'),('1','экономика монет')],
     result_pts=['Рабочая версия для Windows: таймер, город, настройки.'],
     tools=['Claude','GitHub'],
     metrics=[('Часы в неделю',True,'Часы целевой работы на активного пользователя в неделю','7'),('Дни с сессией',False,'Дни в неделю с хотя бы одной завершённой сессией','5 из 7'),('План',False,'Сессии, завершённые по плану','80%'),('Возврат на 7-й день',False,'Пользователи, вернувшиеся на 7-й день','30%')],
     lesson='Проверил бы механику монет и зданий на 5–10 людях до экрана города: она задаёт экономику продукта.'),
  ],
)

# ---------------------------------------------------------------- EN
EN = dict(
  lang='en', title='Andrey Perepechay — Product Owner, Project Manager',
  desc='Portfolio: four products with problem, role, result and metrics. Product Owner and Project Manager.',
  alt_url='/', alt_label='RU', cur_label='EN',
  nav=[('#cases','Case studies'),('#about','Experience'),('#contact','Contact')],
  h1='Product Owner and Project Manager',
  lead='Three years in enterprise IT projects. Four products of my own, from research to a working release.',
  cta1='View case studies', cta2='Message on Telegram',
  facts=[('3 teams','about 10 people each. Bank settlements platform, Axenix: budget, team load, customer escalations.'),
         ('20,000','users of a corporate knowledge base with AI search. SIBUR.'),
         ('4 products','from idea to a working release. Below: problem, role, result, metrics.'),
         ('50+','people played the online game “Growing City”.')],
  cases_h='Case studies', expand='Expand all', collapse='Collapse all',
  l_problem='Problem', l_role='Role', l_done='What I did', l_result='Result',
  l_tools='Tools', l_metrics='Metrics', l_lesson='Takeaway',
  m_head=('Metric','Definition','Target'),
  m_note='Targets are benchmarks I would set for the product. They are not measured results.',
  m_main='primary metric',
  peek_task='Problem', peek_res='Result',
  about_h='Experience', contact_h='Contact',
  about=[('Axenix, Project Manager','Bank settlements platform. Three teams of 10 people. Budget, team load, customer escalations.'),
         ('Technologies of Trust','Launched a pilot AI product for corporate treasury. Researched the digital financial assets market: regulation and cases.'),
         ('SIBUR','Corporate knowledge base with AI search. Whole company connected, about 20,000 users.'),
         ('Education','Law degree: legal support of national security.')],
  cases=[
   dict(kind='joyka', n='01', name='Joyka', one='Mobile app with short guided meditations for people under stress.',
     tags=['Product Owner','iOS','Developer and designer on the team'],
     peek_task='reduce stress in 4–5 minutes.', peek_res='8 scenarios, 3 voices, streak statistics. iOS app.',
     alts=['Joyka: home screen with meditations','Joyka: meditation screen','Joyka: sound and voice settings','Joyka: personal statistics'],
     problem='People under stress need a fast practice. Long generic courses do not fit the “right now” situation.',
     role='Product Owner. Market research, audience analysis, questionnaire survey. Requirements for the developer and the designer. They wrote the code and drew the design.',
     done=['Researched the market and the audience, ran a questionnaire survey.','Defined 8 situations of 4–5 minutes: sleep, tension, appetite, decisions and others.','Specified the sound setup: metronome, nature sounds, 432 Hz music, 3 voices, separate volume per layer.','Added retention: daily reminder, day streak, statistics per meditation.'],
     tiles=[('8','scenarios'),('3','voices'),('3','sound layers'),('4–5 min','per session')],
     result_pts=['Finished iOS app with personal statistics and streaks.'],
     tools=['Questionnaire survey','Market research','Audience analysis'],
     metrics=[('Frequency',True,'Completed sessions per active user per week','3'),('Activation',False,'New users who finish a first session on install day','60%'),('Completion rate',False,'Completed sessions / started sessions','70%'),('Day-7 retention',False,'Users who return on day 7','20%')],
     lesson='I would build analytics events into the first release. Without them it is unclear which scenarios bring people back.'),
   dict(kind='rg', n='02', name='Growing City', one='Browser game: one-click match, bots, lobby by link.',
     tags=['Product Owner','Project Manager','Web','Full cycle'],
     peek_task='play without waiting for friends.', peek_res='50+ players, 3 languages, match analytics, indexed by Google and Yandex.',
     alts=['Growing City: lobby','Growing City: market and player turn'],
     problem='A board game needs company. Gathering people at one moment is hard.',
     role='Product Owner and Project Manager in one person: idea, rules, balance, priorities, releases, analytics. Code written with Claude and Cursor.',
     done=['“Quick game”: a match starts at once, free seats are filled by 6 bot characters.','Lobby by link with a PIN code, 3 match-length modes.','Card balance: two iterations. Tutorial, chat with reactions, player kick.','Interface in Russian, English and Spanish.','Fixed connection blocking, player disconnects and the mobile layout.'],
     tiles=[('50+','players'),('2','search engines: site verified'),('1','admin panel with match analytics')],
     result_pts=['Own match analytics.','Launched on its own domain with SSL.','Hosting is not renewed, there is no public link now.'],
     tools=['Claude','Cursor','React','Node.js','Socket.io','SQLite','nginx','Git'],
     metrics=[('Matches per player',True,'Completed matches per player per week','3'),('First match',False,'Players who reach the end of a first match','80%'),('Next-day return',False,'Players who return on day 2','25%'),('Time to start',False,'From click to first turn','10 sec')],
     lesson='I would run a closed test with 10–15 players and a survey after the first match before adding content.'),
   dict(kind='w12', n='03', name='Week12', one='Goal planning service based on the “12 Week Year” method.',
     tags=['Product Owner','Project Manager','Web','First product'],
     peek_task='connect a yearly goal with weekly tasks.', peek_res='4 goal levels, life wheel with 8 areas, retrospectives. Project closed.',
     alts=['Week12: cycle dashboard','Week12: landing page','Week12: life wheel'],
     problem='A big goal gets lost without a link to the actions of the week.',
     role='Product Owner and Project Manager. Moved a consulting goal-achievement method into a service.',
     done=['Goal hierarchy: vector, yearly goals, season goals, tasks.','Dashboard: cycle progress, weekly focus, 12-week map.','Life wheel with 8 areas, weekly retrospectives, reward for a finished season.','Onboarding with self-assessment, email reminders, admin panel.','Russian personal data law (152-FZ): cookie consent, data processing policy.'],
     tiles=[('4','goal levels'),('12','weeks per cycle'),('8','life areas'),('1','full user path')],
     result_pts=['Working path from sign-up to a finished season.','Protection: login attempt limit for the admin panel, row-level access in the database.','Project closed. It tested the method in practice.'],
     tools=['Cursor','Next.js','TypeScript','Supabase','Vercel','Tailwind'],
     metrics=[('Week completion',True,'Completed weekly tasks / planned tasks','70%'),('Activation',False,'First goal created on sign-up day','70%'),('Week-2 return',False,'Users who return in week 2','40%'),('Finished seasons',False,'Seasons that reach week 12','15%')],
     lesson='I would start by testing demand: a description page and 10 interviews before building the full goal hierarchy.'),
   dict(kind='oyf', n='04', name='Own Your Future', one='Windows app: time spent on goals turns into floors of a city.',
     tags=['Product Owner','Project Manager','Windows','Game mechanics'],
     peek_task='show accumulated progress on long goals.', peek_res='Working version: timer, city, coins, day streak.',
     alts=['Own Your Future: session timer','Own Your Future: city and active session'],
     problem='Timers count hours but do not show the accumulated result of a long goal.',
     role='Product Owner and Project Manager. Product brief, mechanics, release priorities, interface requirements. Built with Claude.',
     done=['Mechanics: one session adds a floor, floor height is proportional to time.','3 directions: Work, Development, Entertainment, plus custom ones.','Coins for floors, leisure buildings bought with coins.','A building never closes: the goal is only a marker, a skill can keep growing.','Frameless widget window of fixed size.'],
     tiles=[('3','directions'),('3','sections: timer, city, settings'),('1','coin economy')],
     result_pts=['Working Windows version: timer, city, settings.'],
     tools=['Claude','GitHub'],
     metrics=[('Hours per week',True,'Hours of goal work per active user per week','7'),('Session days',False,'Days per week with at least one completed session','5 of 7'),('Plan',False,'Sessions finished as planned','80%'),('Day-7 retention',False,'Users who return on day 7','30%')],
     lesson='I would test the coin and building mechanics with 5–10 people before building the city screen: it sets the product economy.'),
  ],
)

CSS = r'''
:root{--bg:#fff;--ink:#14161a;--mute:#5f6670;--line:#e4e7ec;--soft:#f6f7f9;--ok:#0f7b4f;--okbg:#e8f6ee;--okline:#bfe5cf}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:Inter,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:inherit}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
header.top{position:sticky;top:0;background:rgba(255,255,255,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);z-index:5}
header.top .wrap{display:flex;justify-content:space-between;align-items:center;height:56px}
header.top b{font-weight:600}
nav{display:flex;align-items:center;gap:20px}
nav a{text-decoration:none;color:var(--mute);font-size:14px}
nav a:hover{color:var(--ink)}
.lang{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;font-size:13px}
.lang span,.lang a{padding:4px 11px;display:block}
.lang span{background:var(--ink);color:#fff}
.lang a{color:var(--mute)}
.hero{padding:64px 0 24px}
.hero h1{font-size:clamp(32px,5.4vw,54px);line-height:1.08;letter-spacing:-.03em;font-weight:700;max-width:820px}
.hero p.lead{margin-top:16px;font-size:clamp(17px,2vw,20px);color:var(--mute);max-width:680px}
.cta{margin-top:24px;display:flex;gap:10px;flex-wrap:wrap}
.btn{display:inline-block;padding:11px 20px;border-radius:999px;font-size:15px;font-weight:500;text-decoration:none;border:1px solid var(--ink)}
.btn.dark{background:var(--ink);color:#fff}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:12px;margin:36px 0 0}
.fact{border:1px solid var(--line);border-radius:16px;padding:16px 18px;background:var(--soft)}
.fact b{display:block;font-size:30px;letter-spacing:-.02em;line-height:1.1}
.fact span{display:block;margin-top:6px;font-size:14px;color:var(--mute)}
.sechead{display:flex;justify-content:space-between;align-items:center;margin:56px 0 16px}
h2.sec{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);font-weight:600}
.toggleall{font:inherit;font-size:13px;border:1px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer;color:var(--ink)}
.case{border:1px solid var(--line);border-radius:24px;margin-bottom:20px;background:#fff;overflow:hidden}
.case summary{list-style:none;cursor:pointer;padding:24px 28px;position:relative}
.case summary::-webkit-details-marker{display:none}
.case .num{font-size:13px;color:var(--mute)}
.case h3{font-size:clamp(24px,3.4vw,32px);letter-spacing:-.02em;margin:2px 0 4px;padding-right:40px}
.case .one{color:var(--mute);font-size:16px;max-width:720px}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.tag{font-size:13px;padding:4px 11px;border-radius:999px;background:var(--soft);border:1px solid var(--line)}
.tag.role{background:var(--ink);color:#fff;border-color:var(--ink)}
.peek{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:18px}
.peek div{font-size:14.5px;padding:12px 14px;border-radius:12px;background:var(--soft);border:1px solid var(--line)}
.peek div.r{background:var(--okbg);border-color:var(--okline)}
.peek small{display:block;font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-bottom:2px}
.peek .r small{color:var(--ok)}
.case[open] .peek{display:none}
.chev{position:absolute;right:26px;top:28px;width:28px;height:28px;border:1px solid var(--line);border-radius:50%;display:flex;align-items:center;justify-content:center}
.chev:after{content:"";width:7px;height:7px;border-right:2px solid var(--ink);border-bottom:2px solid var(--ink);transform:rotate(45deg) translate(-1px,-1px);transition:transform .2s}
.case[open] .chev:after{transform:rotate(225deg) translate(-1px,-1px)}
.more{padding:0 28px 28px}
.stage{border-radius:20px;padding:30px 18px;display:flex;gap:18px;justify-content:center;align-items:flex-start;overflow-x:auto;margin-bottom:8px}
.stage.joyka{background:linear-gradient(135deg,#d9f5d4,#c9e9f2)}
.stage.rg{background:linear-gradient(135deg,#efe3c8,#e3c9a8)}
.stage.w12{background:linear-gradient(135deg,#eceef2,#dfe3ea);flex-direction:column;align-items:center}
.stage.oyf{background:linear-gradient(135deg,#2a2440,#4a2f3d);align-items:center}
.phone{flex:0 0 auto;width:190px;border-radius:26px;overflow:hidden;background:#fff;box-shadow:0 18px 40px rgba(20,22,26,.22),0 0 0 6px #14161a}
.phone img,.widget img,.desk img{display:block;width:100%;height:auto}
.phone.t1{margin-top:20px}
.widget{flex:0 0 auto;width:240px;filter:drop-shadow(0 18px 34px rgba(0,0,0,.45))}
.desk{width:100%;max-width:760px;border-radius:12px;overflow:hidden;background:#fff;box-shadow:0 18px 40px rgba(20,22,26,.18)}
.stage.oyf .desk{flex:1 1 auto;max-width:540px;min-width:300px}
.desk .bar{height:26px;background:#f1f2f4;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:6px;padding:0 12px}
.desk .bar i{width:9px;height:9px;border-radius:50%;background:#c9ccd2;display:block}
.desk-row{display:flex;gap:18px;flex-wrap:wrap;justify-content:center;width:100%}
.desk-row .desk{max-width:370px;flex:1 1 300px}
dl.rows{margin-top:10px}
.row{display:grid;grid-template-columns:150px 1fr;gap:12px 28px;padding:20px 0;border-top:1px solid var(--line)}
.row dt{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);font-weight:600;padding-top:3px}
.row dd{font-size:15.5px}
.row ol{padding-left:20px}
.row li{margin-bottom:6px}
.row.res{background:var(--okbg);border:1px solid var(--okline);border-radius:16px;padding:20px;margin:6px 0;border-top:1px solid var(--okline)}
.row.res dt{color:var(--ok)}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin-bottom:12px}
.tile{background:#fff;border:1px solid var(--okline);border-radius:12px;padding:10px 12px}
.tile b{display:block;font-size:26px;line-height:1.1;color:var(--ok);letter-spacing:-.02em}
.tile span{font-size:13px;color:var(--mute)}
.res ul{padding-left:18px}
.res li{margin-bottom:4px}
.tools{display:flex;flex-wrap:wrap;gap:7px}
.tools span{font-size:13px;padding:4px 11px;border-radius:8px;background:#fff;border:1px solid var(--line)}
table{width:100%;border-collapse:collapse;font-size:14.5px}
th{text-align:left;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--mute);font-weight:600;padding:0 10px 8px 0;border-bottom:1px solid var(--line)}
td{padding:9px 10px 9px 0;border-bottom:1px solid var(--line);vertical-align:top}
td.t{white-space:nowrap;font-weight:600}
.star{display:inline-block;font-size:11px;padding:1px 7px;border-radius:999px;background:var(--ink);color:#fff;margin-left:6px;font-weight:500;vertical-align:1px}
.note{font-size:13px;color:var(--mute);margin-top:8px}
.exp{border-top:1px solid var(--line)}
.exp div{display:grid;grid-template-columns:200px 1fr;gap:8px 28px;padding:16px 0;border-bottom:1px solid var(--line)}
.exp b{font-weight:600}
.exp span{color:#2b2f36}
.contacts{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}
.contacts a{display:block;padding:16px 18px;border:1px solid var(--line);border-radius:14px;text-decoration:none;font-weight:500;background:var(--soft)}
footer{margin:56px 0 40px;color:var(--mute);font-size:13px}
@media(max-width:760px){.case summary{padding:20px}.more{padding:0 20px 22px}.peek{grid-template-columns:1fr}.row{grid-template-columns:1fr;gap:6px;padding:16px 0}.exp div{grid-template-columns:1fr;gap:2px}.phone{width:140px}.stage{padding:24px 14px;gap:14px;justify-content:flex-start}.stage.w12{align-items:stretch}.stage.rg{justify-content:center}.widget{width:190px}nav a.nl{display:none}.chev{right:18px;top:22px}}
'''

def page(L):
    # переключатель языка и автоопределение
    detect = ''
    if L['lang'] == 'ru':
        detect = ("<script>try{var s=localStorage.getItem('lang'),n=((navigator.languages&&navigator.languages[0])||navigator.language||'ru').toLowerCase();"
                  "if(s==='en'||(!s&&n.indexOf('en')===0)){location.replace('/en/')}}catch(e){}</script>")
    else:
        detect = ("<script>try{if(localStorage.getItem('lang')==='ru'){location.replace('/')}}catch(e){}</script>")
    setlang = "try{localStorage.setItem('lang','%s')}catch(e){}" % ('en' if L['alt_label']=='EN' else 'ru')
    o = []
    o.append('<!doctype html>\n<html lang="%s">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n%s\n<title>%s</title>\n<meta name="description" content="%s">' % (L['lang'], detect, E(L['title']), E(L['desc'])))
    o.append('<link rel="alternate" hreflang="ru" href="/"><link rel="alternate" hreflang="en" href="/en/">')
    o.append('<meta property="og:title" content="%s"><meta property="og:description" content="%s">' % (E(L['title']), E(L['desc'])))
    o.append('<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap&subset=cyrillic" rel="stylesheet">')
    o.append('<style>%s</style>\n</head>\n<body>' % CSS)
    nav = ''.join('<a class="nl" href="%s">%s</a>' % (h, E(t)) for h, t in L['nav'])
    o.append('<header class="top"><div class="wrap"><b>%s</b><nav>%s<div class="lang"><span>%s</span><a href="%s" onclick="%s">%s</a></div></nav></div></header>' % (
        'Андрей Перепечай' if L['lang']=='ru' else 'Andrey Perepechay', nav, L['cur_label'], L['alt_url'], setlang, L['alt_label']))
    o.append('<main class="wrap"><section class="hero"><h1>%s</h1><p class="lead">%s</p><div class="cta"><a class="btn dark" href="#cases">%s</a><a class="btn" href="https://t.me/andrew_727">%s</a></div><div class="facts">' % (E(L['h1']), E(L['lead']), E(L['cta1']), E(L['cta2'])))
    for b, t in L['facts']:
        o.append('<div class="fact"><b>%s</b><span>%s</span></div>' % (E(b), E(t)))
    o.append('</div></section>')
    o.append('<div class="sechead"><h2 class="sec" id="cases">%s</h2><button class="toggleall" type="button" id="tg" data-e="%s" data-c="%s">%s</button></div>' % (E(L['cases_h']), E(L['expand']), E(L['collapse']), E(L['collapse'])))
    for i, c in enumerate(L['cases']):
        alts = dict(('a%d' % (k+1), E(a)) for k, a in enumerate(c['alts']))
        g = gallery(c['kind']).format(**alts)
        tags = ''.join('<span class="tag%s">%s</span>' % (' role' if k == 0 else '', E(t)) for k, t in enumerate(c['tags']))
        o.append('<details class="case"%s><summary><div class="num">%s</div><h3>%s</h3><p class="one">%s</p><div class="tags">%s</div>'
                 '<div class="peek"><div><small>%s</small>%s</div><div class="r"><small>%s</small>%s</div></div><span class="chev"></span></summary><div class="more">' % (
                 ' open' if i == 0 else '', c['n'], E(c['name']), E(c['one']), tags, E(L['peek_task']), E(c['peek_task'][0].upper()+c['peek_task'][1:]), E(L['peek_res']), E(c['peek_res'])))
        o.append(g)
        o.append('<dl class="rows">')
        o.append('<div class="row"><dt>%s</dt><dd>%s</dd></div>' % (E(L['l_problem']), E(c['problem'])))
        o.append('<div class="row"><dt>%s</dt><dd>%s</dd></div>' % (E(L['l_role']), E(c['role'])))
        o.append('<div class="row"><dt>%s</dt><dd><ol>%s</ol></dd></div>' % (E(L['l_done']), ''.join('<li>%s</li>' % E(x) for x in c['done'])))
        tiles = ''.join('<div class="tile"><b>%s</b><span>%s</span></div>' % (E(a), E(b)) for a, b in c['tiles'])
        pts = ''.join('<li>%s</li>' % E(x) for x in c['result_pts'])
        o.append('<div class="row res"><dt>%s</dt><dd><div class="tiles">%s</div><ul>%s</ul></dd></div>' % (E(L['l_result']), tiles, pts))
        o.append('<div class="row"><dt>%s</dt><dd><div class="tools">%s</div></dd></div>' % (E(L['l_tools']), ''.join('<span>%s</span>' % E(x) for x in c['tools'])))
        rows = ''
        for name, main, how, tgt in c['metrics']:
            rows += '<tr><td>%s%s</td><td>%s</td><td class="t">%s</td></tr>' % (E(name), ('<span class="star">%s</span>' % E(L['m_main'])) if main else '', E(how), E(tgt))
        o.append('<div class="row"><dt>%s</dt><dd><table><thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody></table><p class="note">%s</p></dd></div>' % (E(L['l_metrics']), E(L['m_head'][0]), E(L['m_head'][1]), E(L['m_head'][2]), rows, E(L['m_note'])))
        o.append('<div class="row"><dt>%s</dt><dd>%s</dd></div>' % (E(L['l_lesson']), E(c['lesson'])))
        o.append('</dl></div></details>')
    o.append('<div class="sechead"><h2 class="sec" id="about">%s</h2></div><div class="exp">' % E(L['about_h']))
    for a, b in L['about']:
        o.append('<div><b>%s</b><span>%s</span></div>' % (E(a), E(b)))
    o.append('</div><div class="sechead"><h2 class="sec" id="contact">%s</h2></div><div class="contacts"><a href="https://t.me/andrew_727">Telegram: @andrew_727</a><a href="mailto:perepechayandrew@gmail.com">perepechayandrew@gmail.com</a><a href="tel:+79163448547">+7 (916) 344-85-47</a></div>' % E(L['contact_h']))
    o.append('<footer>© 2026 %s</footer></main>' % ('Андрей Перепечай' if L['lang']=='ru' else 'Andrey Perepechay'))
    o.append("<script>var tg=document.getElementById('tg'),ds=[].slice.call(document.querySelectorAll('details.case'));"
             "function sync(){var all=ds.every(function(d){return d.open});tg.textContent=all?tg.dataset.c:tg.dataset.e}"
             "tg.addEventListener('click',function(){var all=ds.every(function(d){return d.open});ds.forEach(function(d){d.open=!all});sync()});"
             "ds.forEach(function(d){d.addEventListener('toggle',sync)});sync();</script></body></html>")
    return '\n'.join(o)

open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(page(RU))
os.makedirs(os.path.join(ROOT, 'en'), exist_ok=True)
open(os.path.join(ROOT, 'en', 'index.html'), 'w', encoding='utf-8').write(page(EN))
print('ok')
