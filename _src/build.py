# -*- coding: utf-8 -*-
"""Собирает index.html (русский) и en/index.html (английский) из одного источника.
Запуск из корня репозитория: python3 _src/build.py"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape

# Палитра компаний. Оттенки приблизительные: чтобы поменять, исправь HEX здесь и запусти build.py
PCOL = {'parole':'#C8473D','joyka':'#3FA75A','rg':'#B5532F','w12':'#5B6575','oyf':'#7B5CD6'}
BRAND = [
 dict(c='#F26A1B', ct='#B8480C', tint='#FFF2E9', line='#F8CDB0'),   # Axenix: оранжевый
 dict(c='#0B72B9', ct='#0B5E9A', tint='#E9F3FB', line='#B8D9F0'),   # СИБУР: синий
 dict(c='#2AA5E3', ct='#0B79B0', tint='#EAF7FE', line='#BDE3F7'),   # Технологии Доверия: голубой
]

IMG = {
 'joyka': [('joyka-home',589,1280),('joyka-timer',589,1280),('joyka-settings',589,1280),('joyka-stats',589,1280)],
 'rg':    [('rg-lobby',645,1170),('rg-market',630,1030)],
 'w12':   [('w12-dashboard',1280,713),('w12-landing',1280,535),('w12-wheel',1280,509)],
 'oyf':   [('oyf-timer',528,854),('oyf-city',1280,844)],
}
def cover(kind, alt):
    def im(n, cls): return '<img class="%s" src="/img/%s.webp" alt="" loading="lazy">' % (cls, n)
    if kind == 'parole': inner = '<div class="fc fc2"><small>RU</small><b>дом</b></div><div class="fc"><small>IT</small><b>la casa</b><span>дом</span></div>'
    elif kind == 'joyka': inner = im('joyka-home','cp') + im('joyka-timer','cp')
    elif kind == 'rg': inner = im('rg-lobby','cp') + im('rg-market','cp')
    elif kind == 'w12': inner = im('w12-dashboard','cw')
    else: inner = im('oyf-timer','cx') + im('oyf-city','cw2')
    return '<div class="cover c-%s" role="img" aria-label="%s">%s</div>' % (kind, E(alt), inner)

def gallery(kind, alts):
    if not IMG.get(kind): return ''
    out = []
    for (name, w, h), a in zip(IMG[kind], alts):
        cls = 'g-m' if h > w else 'g-d'
        out.append('<figure class="%s"><img src="/img/%s.webp" alt="%s" width="%d" height="%d" loading="lazy"></figure>' % (cls, name, E(a), w, h))
    return '<div class="gal">%s</div>' % ''.join(out)

# =================================================================== RU
RU = dict(
 lang='ru', name='Андрей Перепечай',
 title='Андрей Перепечай — Product Owner & Project Manager',
 desc='Product Owner. Корпоративные ИТ-проекты, пять собственных продуктов: задача, роль, результат.',
 alt_url='/en/', alt_label='EN', cur_label='RU',
 nav=[('#projects','Продукты'),('#experience','Проекты'),('#skills','Навыки'),('#contact','Контакты')],
 role='Product Owner & Project Manager',
 lead='Project Manager в банковском и корпоративном IT: проекты с бюджетом более 250 млн руб., 3 команды разработки (около 30 человек). Закрыл 5 квартальных поставок подряд в срок и в согласованном объёме. Вёл два ИИ-продукта: корпоративную базу знаний с нейросетевым поиском на 20 000 пользователей и ML-сервис прогнозирования для казначейства. Использую нейросети в работе: сократил подготовку отчётности в 4 раза, сам запускаю продукты без команды.',
 b_exp='Проекты', b_proj='Продукты', b_tg='Написать в Telegram',
 facts=[('≈260 млн руб.','бюджет платформы банковских взаиморасчётов. 3 команды, около 30 человек. Axenix.'),
        ('≈20 000','пользователей корпоративной базы знаний с нейросетевым поиском. СИБУР.'),
        ('5 продуктов','собственные продукты от идеи до запуска. Один в App Store, одна онлайн-игра с 50+ игроками.')],
 exp_h='Опыт работы',
 x_lbl=dict(project='Проект', scale='Масштаб', resp='Ответственность', res='Результаты'),
 exp=[
  dict(co='Axenix', pos='Project Manager', per='08.2025 — настоящее время',
       project='Платформа автоматизации взаиморасчётов крупного банка.',
       scale='Бюджет около 260 млн руб. Три взаимосвязанные системы, три функциональных модуля, около 300 внутренних пользователей. 3 команды разработки, около 30 человек, 3 тимлида.',
       resp='Бюджет, ресурсы и загрузка команд, зависимости между системами, эскалации заказчика.',
       res=['Три модуля импортозамещения запущены и масштабируются.','Отклонений от плана по бюджету нет.','Подготовил новый проект на 77 млн руб.: оценки команд, бюджет, финансовая модель, сроки с заказчиком.','5 квартальных поставок подряд в срок и в согласованном объёме.']),
  dict(co='Технологии Доверия', pos='Бизнес-аналитик, руководитель проекта AI Co-Pilot', per='11.2024 — 08.2025',
       project='Сервис прогнозирования движения денежных средств для казначейства на машинном обучении.',
       scale='Кросс-функциональная команда: backend, frontend, DevOps, аналитика, машинное обучение.',
       resp='План, бэклог и дорожная карта, требования, демонстрации, исследования рынка.',
       res=['Вместе с командой машинного обучения повысил точность прогноза с 70% до 85% на исторических данных.','Подготовил блок демонстраций для пилота в нефтехимической компании.','Исследование для облачного хранилища банка: 10 фокус-групп, 70+ гипотез, 10 инициатив. Клиент заказал повторный проект.']),
  dict(co='СИБУР', pos='Проектный офис (PMO)', per='06.2024 — 11.2024',
       project='Корпоративная база знаний с поиском на основе больших языковых моделей и RAG, внутри контура компании.',
       scale='Около 20 000 пользователей, подключена вся компания. Бюджет около 350 млн руб.',
       resp='Бюджет и сроки, контрольные точки, бэклог из 100+ гипотез (Jira, приоритизация RICE), планирование спринтов, груминг, обзоры спринтов, подрядчики, обучение пользователей.',
       res=['Контрольные точки пройдены с отклонением по бюджету менее 15%.','Процесс подготовки к контрольным точкам в Confluence: экономия около 7 человеко-дней на каждой квартальной точке.','Рост ежедневных активных пользователей (DAU) на 15% за счёт обучения и коммуникаций.']),
 ],
 proj_h='Собственные продукты', proj_sub='Пять продуктов, которые я придумал, описал и вывел в рабочую версию.',
 p_lbl=dict(role='Роль',stage='Стадия',res='Результат',more='Подробнее'),
 d_lbl=dict(about='О продукте',problem='Проблема пользователя',role='Моя роль',done='Что сделано',result='Результат',metrics='Метрики и аналитика',fact='Фактически',main='Главная метрика',aux='Вспомогательные',events='События для сбора',close='Закрыть'),
 projects=[
  dict(id='joyka', name='Joyka', desc='Мобильное приложение коротких медитаций для людей под стрессом.',
   role='Product Owner. Команда: разработчик и дизайнер.', stage='Готовое приложение в App Store', res_short='≈200 установок, рейтинг 5,0',
   alts=['Joyka: главный экран','Joyka: экран медитации','Joyka: настройки звука и голоса','Joyka: личная статистика'],
   about='8 сценариев по 4–5 минут: сон, напряжение, аппетит, решение и другие. Метроном, звуки природы, музыка 432 Гц, 3 голоса.',
   problem='Человеку под стрессом нужна короткая практика под конкретную ситуацию. Длинные общие курсы для этого не подходят.',
   role_d='Product Owner. Исследование рынка и аудитории, анкетирование, требования. Разработчик и дизайнер реализовали продукт.',
   done=['Исследовал рынок и аудиторию, провёл анкетирование.','Выделил пользовательские ситуации и описал 8 сценариев.','Описал требования к настройкам звука, голосов и громкости каждого слоя.','Добавил механики возврата: ежедневное напоминание, серия дней, статистика.'],
   result=['Готовое приложение для iOS, выпущено в App Store.','≈200 установок, рейтинг 5,0.'],
   fact=['≈200 установок, рейтинг 5,0 в App Store.'],
   main='Завершённые сессии на активного пользователя в неделю (Sessions per Active User).',
   aux=['Доля активации (Activation Rate): первая сессия в день установки.','Удержание на 7-й день (D7 Retention).'],
   events=['Установка','Начало и завершение сессии','Смена голоса','Включение напоминания']),
  dict(id='rg', name='Растущий город', desc='Онлайн-экономическая настольная игра: быстрая партия с ботами и лобби по ссылке.',
   role='Product Owner. Реализация с Claude и Cursor.', stage='Запущена. Хостинг не продлён', res_short='50+ игроков',
   alts=['Растущий город: лобби','Растущий город: рынок и ход игрока'],
   about='Игроки покупают карты построек и получают доход по броску кубика. Партия стартует за один клик, свободные места занимают 6 ботов-персонажей.',
   problem='Для настольной игры нужна компания. Собрать людей в один момент трудно.',
   role_d='Product Owner: правила, игровая экономика, бэклог и приоритеты, релизы, аналитика. Claude и Cursor использовал как инструменты реализации.',
   done=['Проработал правила и баланс игровой экономики: две итерации баланса карт.','Вёл бэклог и приоритеты, выпустил рабочую версию за 3 недели.','Быстрая игра с ботами, многопользовательский режим, лобби по ссылке с PIN-кодом.','Три языка интерфейса, мобильная адаптация.','Настроил аналитику партий: воронка, DAU, удержание D1 и D7, длительность сессий.'],
   result=['50+ игроков.','Первые 3 недели: 21 игрок, 42 партии, средняя сессия 18 минут.','Сайт подтверждён в Google Search Console и Яндекс.Вебмастере.','Хостинг не продлён, публичной ссылки сейчас нет.'],
   fact=['50+ игроков, из них за первые 3 недели: 21 игрок, 42 партии, средняя сессия 18 минут.'],
   main='Завершённые партии на игрока (Completed Games).',
   aux=['Зарегистрированные пользователи.','Удержание на 7-й день (D7 Retention).','Ежедневные активные пользователи (DAU).'],
   events=['Регистрация','Вход в лобби','Старт партии','Завершение партии','Выход до конца партии']),
  dict(id='w12', name='Week12', desc='Сервис планирования целей по методологии «12 недель в году».',
   role='Product Owner.', stage='Проект закрыт', res_short='Рабочий путь от регистрации до завершения сезона',
   alts=['Week12: дашборд цикла','Week12: главная страница','Week12: колесо жизни'],
   about='Иерархия целей: вектор, цели года, цели сезона, задачи. Дашборд цикла, колесо жизни по 8 сферам, еженедельные ретроспективы.',
   problem='Большая цель теряется, если она не связана с действиями недели.',
   role_d='Product Owner. Перенёс консалтинговую методологию достижения целей в цифровой продукт.',
   done=['Проработал пользовательский путь и иерархию целей.','Дашборд цикла, система планирования и ретроспектив.','Онбординг с самооценкой, письма-напоминания, админ-панель.','Требования 152-ФЗ: согласие на cookie, политика обработки данных.'],
   result=['Рабочий сценарий от регистрации до завершения сезона.','Проект закрыт. Подтверждённых показателей активной аудитории нет.'],
   fact=['Подтверждённых данных об активной аудитории нет.'],
   main='Доля выполненных задач недели (Task Completion Rate).',
   aux=['Доля активации (Activation Rate): первая цель в день регистрации.','Удержание на 4-й неделе (W4 Retention).','Еженедельные активные пользователи (WAU), при наличии аудитории.'],
   events=['Создание цели','Отметка задачи','Заполнение ретроспективы','Завершение сезона']),
  dict(id='oyf', name='Own Your Future', desc='Приложение для Windows: время на долгие цели превращается в этажи города.',
   role='Product Owner. Реализация с Claude.', stage='Рабочая версия', res_short='Рабочая версия с игровой экономикой монет',
   alts=['Own Your Future: таймер сессии','Own Your Future: город и активная сессия'],
   about='Фокус-сессия добавляет этаж, высота пропорциональна времени. Три направления: работа, развитие, развлечения. На монеты строятся здания для отдыха.',
   problem='Таймеры считают часы, но не показывают накопленный результат по долгой цели.',
   role_d='Product Owner. Продуктовый бриф, механики, приоритеты версий, требования к интерфейсу.',
   done=['Сформулировал продуктовую концепцию и механику фокус-сессий.','Проработал игровую экономику: монеты за этажи, здания для отдыха.','Описал виртуальный город: здание не закрывается, цель остаётся маркером.','Расставил приоритеты функций, довёл до рабочей версии.'],
   result=['Рабочая версия для Windows: таймер, город, настройки.','Используется для личных целей. Пользовательских данных нет.'],
   fact=['Пользовательских данных нет: приложение для личного использования.'],
   main='Завершённые фокус-сессии на активного пользователя в неделю (Completed Focus Sessions).',
   aux=['Активированные пользователи: завершена первая сессия.','Еженедельные активные пользователи (WAU).','Удержание на 7-й день (D7 Retention).'],
   events=['Старт и завершение сессии','Построенный этаж','Трата монет','Открытие экрана города']),
  dict(id='parole', name='Parole', desc='Веб-приложение для изучения итальянских слов: карточки, ввод перевода, проверка написания.',
   role='Product Owner.', stage='Работает. Устанавливается на экран «Домой»', res_short='Работает без интернета, без аккаунта разработчика Apple',
   alts=['Parole: карточка со словом'],
   about='Список слов вставляется из таблицы или от ChatGPT, приложение показывает слова по одному. Три режима: итальянский в русский, русский в итальянский, в обе стороны. Слово считается выученным после нескольких верных ответов подряд.',
   problem='Нужен простой способ учить итальянские слова из собственных списков без платного аккаунта разработчика Apple.',
   role_d='Product Owner: сценарий занятия, формат загрузки слов, правила «выученного» слова, публикация без App Store.',
   done=['Загрузка слов: вставка списка, файл csv, ячейки из Google Таблиц и Excel. Язык определяется сам.','Занятие: три режима, возврат ошибок в том же занятии, подсказка по буквам, кнопка «Засчитать как верное».','Готовые запросы для ChatGPT, которые отдают слова в нужном формате.','Публикация как сайт с установкой на экран «Домой» и работой без интернета.'],
   result=['Работающее приложение: установка на экран «Домой», работа без интернета.','Сделано для личного использования. Данных об аудитории нет.'],
   fact=['Данных об аудитории нет: приложение для личного использования.'],
   main='Выученные слова на активного пользователя в неделю (Learned Words).',
   aux=['Доля завершённых занятий (Session Completion Rate).','Удержание на 7-й день (D7 Retention).','Доля ответов с подсказкой.'],
   events=['Добавление списка слов','Старт занятия','Верный и неверный ответ','Слово выучено']),
 ],
 sk_h='Навыки',
 skills=[('Управление проектами',['Бюджет и финансовая модель','Сроки и ресурсы','Риски и зависимости','Работа с заказчиком','Scrum: планирование, груминг, обзоры спринтов']),
         ('Продуктовая работа',['Исследование пользователей и рынка','Гипотезы и приоритизация (RICE)','Бэклог и требования','Минимально жизнеспособный продукт (MVP)','Продуктовая аналитика']),
         ('Нейросети и инструменты',['Поиск на больших языковых моделях (RAG)','Прогнозирование на машинном обучении','Claude, Cursor','Jira, Confluence'])],
 c_h='Контакты', phone='Телефон',
)

# =================================================================== EN
EN = dict(
 lang='en', name='Andrey Perepechay',
 title='Andrey Perepechay — Product Owner & Project Manager',
 desc='Product Owner. Enterprise IT projects and five products of my own: problem, role, result.',
 alt_url='/', alt_label='RU', cur_label='EN',
 nav=[('#projects','Products'),('#experience','Projects'),('#skills','Skills'),('#contact','Contact')],
 role='Product Owner & Project Manager',
 lead='Project Manager in banking and corporate IT: projects with a budget above 250 million RUB, 3 development teams (about 30 people). Closed 5 quarterly deliveries in a row on time and in the agreed scope. Led two products with AI: a corporate knowledge base with AI search (LLM, RAG) for 20,000 users and an ML forecasting service for treasury. I use AI at work: cut report preparation time by 4 times, and I launch products on my own without a team.',
 b_exp='Projects', b_proj='Products', b_tg='Message on Telegram',
 facts=[('≈260 M RUB','budget of a bank settlements platform. 3 teams, about 30 people. Axenix.'),
        ('≈20,000','users of a corporate knowledge base with AI search. SIBUR.'),
        ('5 products','my own products from idea to launch. One in the App Store, one online game with 50+ players.')],
 exp_h='Experience',
 x_lbl=dict(project='Project', scale='Scale', resp='Responsibility', res='Results'),
 exp=[
  dict(co='Axenix', pos='Project Manager', per='08.2025 — present',
       project='Settlements automation platform for a large bank.',
       scale='Budget about 260 M RUB. Three connected systems, three functional modules, about 300 internal users. 3 development teams, about 30 people, 3 team leads.',
       resp='Budget, resources and team load, dependencies between systems, customer escalations.',
       res=['Three import-substitution modules launched and scaling.','No budget deviations from plan.','Prepared a new 77 M RUB project: team estimates, budget, financial model, timeline agreed with the customer.','5 quarterly deliveries in a row on time and in the agreed scope.']),
  dict(co='Technologies of Trust', pos='Business Analyst, Project Lead of AI Co-Pilot', per='11.2024 — 08.2025',
       project='Machine-learning cash flow forecasting service for corporate treasury.',
       scale='Cross-functional team: backend, frontend, DevOps, analytics, machine learning.',
       resp='Plan, backlog and roadmap, requirements, demos, market research.',
       res=['With the machine learning team raised forecast accuracy from 70% to 85% on historical data.','Prepared the demo block for a pilot at a petrochemical company.','Research for a bank cloud storage: 10 focus groups, 70+ hypotheses, 10 initiatives. The client ordered a follow-up project.']),
  dict(co='SIBUR', pos='Project Management Office (PMO)', per='06.2024 — 11.2024',
       project='Corporate knowledge base with search on large language models and RAG, inside the company perimeter.',
       scale='About 20,000 users, the whole company connected. Budget about 350 M RUB.',
       resp='Budget and timeline, checkpoints, a backlog of 100+ hypotheses (Jira, RICE prioritization), sprint planning, grooming, sprint reviews, contractors, user training.',
       res=['Checkpoints passed with budget deviation under 15%.','Checkpoint preparation process in Confluence: about 7 person-days saved at each quarterly checkpoint.','Daily active users (DAU) up 15% through training and communication.']),
 ],
 proj_h='Products of my own', proj_sub='Five products I defined, specified and brought to a working version.',
 p_lbl=dict(role='Role',stage='Stage',res='Result',more='Details'),
 d_lbl=dict(about='About the product',problem='User problem',role='My role',done='What I did',result='Result',metrics='Metrics and analytics',fact='Actual',main='Primary metric',aux='Supporting metrics',events='Events to collect',close='Close'),
 projects=[
  dict(id='joyka', name='Joyka', desc='Mobile app with short meditations for people under stress.',
   role='Product Owner. Team: developer and designer.', stage='Finished app in the App Store', res_short='≈200 installs, 5.0 rating',
   alts=['Joyka: home screen','Joyka: meditation screen','Joyka: sound and voice settings','Joyka: personal statistics'],
   about='8 scenarios of 4–5 minutes: sleep, tension, appetite, decisions and others. Metronome, nature sounds, 432 Hz music, 3 voices.',
   problem='A person under stress needs a short practice for a specific situation. Long generic courses do not fit.',
   role_d='Product Owner. Market and audience research, questionnaire survey, requirements. The developer and the designer built the product.',
   done=['Researched the market and the audience, ran a questionnaire survey.','Identified user situations and specified 8 scenarios.','Specified sound, voice and per-layer volume settings.','Added retention mechanics: daily reminder, day streak, statistics.'],
   result=['Finished iOS app, released in the App Store.','≈200 installs, 5.0 rating.'],
   fact=['≈200 installs, 5.0 rating in the App Store.'],
   main='Completed sessions per active user per week (Sessions per Active User).',
   aux=['Activation Rate: first session on install day.','Day-7 Retention (D7 Retention).'],
   events=['Install','Session start and finish','Voice change','Reminder enabled']),
  dict(id='rg', name='Growing City', desc='Online economic board game: quick match with bots and a lobby by link.',
   role='Product Owner. Built with Claude and Cursor.', stage='Launched. Hosting not renewed', res_short='50+ players',
   alts=['Growing City: lobby','Growing City: market and player turn'],
   about='Players buy building cards and earn income on dice rolls. A match starts in one click, free seats are filled by 6 bot characters.',
   problem='A board game needs company. Gathering people at one moment is hard.',
   role_d='Product Owner: rules, game economy, backlog and priorities, releases, analytics. Claude and Cursor were implementation tools.',
   done=['Designed the rules and the game economy balance: two iterations of card balance.','Ran the backlog and priorities, shipped a working version in 3 weeks.','Quick game with bots, multiplayer mode, lobby by link with a PIN code.','Three interface languages, mobile adaptation.','Set up match analytics: funnel, DAU, D1 and D7 retention, session length.'],
   result=['50+ players.','First 3 weeks: 21 players, 42 matches, average session 18 minutes.','Site verified in Google Search Console and Yandex Webmaster.','Hosting is not renewed, there is no public link now.'],
   fact=['50+ players; in the first 3 weeks: 21 players, 42 matches, average session 18 minutes.'],
   main='Completed matches per player (Completed Games).',
   aux=['Registered users.','Day-7 Retention (D7 Retention).','Daily Active Users (DAU).'],
   events=['Sign-up','Lobby join','Match start','Match finish','Exit before the end']),
  dict(id='w12', name='Week12', desc='Goal planning service based on the “12 Week Year” method.',
   role='Product Owner.', stage='Project closed', res_short='Working path from sign-up to a finished season',
   alts=['Week12: cycle dashboard','Week12: landing page','Week12: life wheel'],
   about='Goal hierarchy: vector, yearly goals, season goals, tasks. Cycle dashboard, life wheel with 8 areas, weekly retrospectives.',
   problem='A big goal gets lost when it is not linked to the actions of the week.',
   role_d='Product Owner. Turned a consulting goal-achievement method into a digital product.',
   done=['Designed the user path and the goal hierarchy.','Cycle dashboard, planning and retrospective system.','Onboarding with self-assessment, email reminders, admin panel.','Russian personal data law (152-FZ): cookie consent, data processing policy.'],
   result=['Working scenario from sign-up to a finished season.','Project closed. There are no confirmed active audience figures.'],
   fact=['No confirmed data on an active audience.'],
   main='Share of completed weekly tasks (Task Completion Rate).',
   aux=['Activation Rate: first goal on sign-up day.','Week-4 Retention (W4 Retention).','Weekly Active Users (WAU), once there is an audience.'],
   events=['Goal created','Task checked','Retrospective filled','Season finished']),
  dict(id='oyf', name='Own Your Future', desc='Windows app: time spent on long goals turns into floors of a city.',
   role='Product Owner. Built with Claude.', stage='Working version', res_short='Working version with a coin economy',
   alts=['Own Your Future: session timer','Own Your Future: city and active session'],
   about='A focus session adds a floor, height is proportional to time. Three directions: work, development, entertainment. Coins buy leisure buildings.',
   problem='Timers count hours but do not show the accumulated result of a long goal.',
   role_d='Product Owner. Product brief, mechanics, release priorities, interface requirements.',
   done=['Defined the product concept and the focus session mechanics.','Designed the game economy: coins for floors, leisure buildings.','Described the virtual city: a building never closes, the goal stays a marker.','Prioritized features and brought the product to a working version.'],
   result=['Working Windows version: timer, city, settings.','Used for personal goals. No user data.'],
   fact=['No user data: the app is for personal use.'],
   main='Completed focus sessions per active user per week (Completed Focus Sessions).',
   aux=['Activated users: first session completed.','Weekly Active Users (WAU).','Day-7 Retention (D7 Retention).'],
   events=['Session start and finish','Floor built','Coins spent','City screen opened']),
  dict(id='parole', name='Parole', desc='Web app for learning Italian words: flashcards, typed translation, spelling check.',
   role='Product Owner.', stage='Working. Installs to the Home screen', res_short='Works offline, no Apple developer account needed',
   alts=['Parole: word card'],
   about='A word list is pasted from a spreadsheet or from ChatGPT, and the app shows words one by one. Three modes: Italian to Russian, Russian to Italian, both ways. A word counts as learned after several correct answers in a row.',
   problem='A simple way to learn Italian words from your own lists without a paid Apple developer account.',
   role_d='Product Owner: lesson flow, word import format, rules for a “learned” word, publishing without the App Store.',
   done=['Word import: pasted list, csv file, cells from Google Sheets and Excel. The language is detected automatically.','Lesson: three modes, mistakes return in the same lesson, letter-by-letter hint, “Count as correct” button.','Ready-made ChatGPT prompts that return words in the right format.','Published as a site that installs to the Home screen and works offline.'],
   result=['Working app: installs to the Home screen, works offline.','Built for personal use. No audience data.'],
   fact=['No audience data: the app is for personal use.'],
   main='Learned words per active user per week (Learned Words).',
   aux=['Session Completion Rate.','D7 Retention.','Share of answers given with a hint.'],
   events=['Word list added','Session started','Correct and wrong answer','Word learned']),
 ],
 sk_h='Skills',
 skills=[('Project management',['Budget and financial model','Timeline and resources','Risks and dependencies','Customer communication','Scrum: planning, grooming, sprint reviews']),
         ('Product work',['User and market research','Hypotheses and prioritization (RICE)','Backlog and requirements','Minimum viable product (MVP)','Product analytics']),
         ('AI and tools',['Search on large language models (RAG)','Forecasting with machine learning','Claude, Cursor','Jira, Confluence'])],
 c_h='Contact', phone='Phone',
)

CSS = r'''
:root{--bg:#fff;--ink:#14161a;--mute:#5f6670;--line:#e4e7ec;--soft:#f6f7f9;--ok:#0f7b4f;--okbg:#e9f6ef;--okline:#bfe5cf}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:70px}
body{font-family:Inter,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:inherit}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
header.top{position:sticky;top:0;background:rgba(255,255,255,.93);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);z-index:5}
header.top .wrap{display:flex;justify-content:space-between;align-items:center;height:54px}
header.top b{font-weight:600}
nav{display:flex;align-items:center;gap:18px}
nav a{text-decoration:none;color:var(--mute);font-size:14px}
nav a:hover{color:var(--ink)}
.lang{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;font-size:13px}
.lang span,.lang a{padding:4px 11px;display:block}
.lang span{background:var(--ink);color:#fff}
.lang a{color:var(--mute)}
.hero{padding:44px 0 8px}
.hero .role{font-size:14px;color:var(--ok);font-weight:600;letter-spacing:.02em}
.hero h1{font-size:clamp(28px,4.2vw,40px);line-height:1.12;letter-spacing:-.02em;font-weight:700;margin-top:6px}
.hero p.lead{margin-top:12px;font-size:17px;color:var(--mute);max-width:660px}
.cta{margin-top:24px;display:flex;gap:10px;flex-wrap:wrap}
.btn{display:inline-block;padding:9px 18px;border-radius:999px;font-size:14.5px;font-weight:500;text-decoration:none;border:1px solid var(--ink);background:#fff;color:var(--ink);cursor:pointer;font-family:inherit}
.btn.dark{background:var(--ink);color:#fff}
.tabs{display:inline-flex;gap:4px;margin-top:34px;padding:4px;border:1px solid var(--line);border-radius:999px;background:var(--soft)}
.tabs button{border:0;background:transparent;padding:9px 22px;border-radius:999px;font:inherit;font-size:15px;font-weight:600;color:var(--mute);cursor:pointer}
.tabs{position:relative}
.tabs .ind{position:absolute;top:4px;bottom:4px;left:0;width:0;border-radius:999px;background:var(--ink);transition:transform .45s cubic-bezier(.22,1,.36,1),width .45s cubic-bezier(.22,1,.36,1);z-index:0}
.tabs button{position:relative;z-index:1;transition:color .3s}
.tabs button.on{color:#fff}
.panel{transition:opacity .2s ease,transform .2s ease}
.panel.leave{opacity:0;transform:translateY(-8px)}
.panel.enter{animation:panelIn .55s cubic-bezier(.22,1,.36,1)}
@keyframes panelIn{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
@keyframes up{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.hero>*{animation:up .8s cubic-bezier(.22,1,.36,1) both}
.hero>.role{animation-delay:.05s}.hero>h1{animation-delay:.12s}.hero>.lead{animation-delay:.2s}.hero>.cta{animation-delay:.3s}.hero>.facts{animation-delay:.4s}
.js .rv{opacity:0;transform:translateY(22px);transition:opacity .8s cubic-bezier(.22,1,.36,1),transform .8s cubic-bezier(.22,1,.36,1)}
.js .rv.in{opacity:1;transform:none}
.grid .card:nth-child(2n).rv{transition-delay:.1s}
.card{transition:transform .35s cubic-bezier(.22,1,.36,1),box-shadow .35s ease}
.card.rv.in:hover{transform:translateY(-5px);box-shadow:0 16px 36px rgba(20,22,26,.12)}
.cover img{transition:transform .6s cubic-bezier(.22,1,.36,1)}
.card:hover .cover img{transform:translateY(-6px) scale(1.04)}
.fc{transition:transform .5s cubic-bezier(.22,1,.36,1)}
.card:hover .fc{transform:translateY(-6px) rotate(2deg)}.card:hover .fc2{transform:translateY(-4px) rotate(-7deg)}
.btn{transition:transform .2s ease,background .2s ease,color .2s ease,box-shadow .2s ease}
.btn:hover{transform:translateY(-2px)}
.btn.dark:hover{background:#2c3038}
.btn.tg svg{transition:transform .35s cubic-bezier(.22,1,.36,1)}
.btn.tg:hover svg{transform:translate(2px,-2px) rotate(-8deg)}
.fact{transition:transform .3s ease,box-shadow .3s ease}.fact:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(20,22,26,.08)}
.contacts a{transition:background .25s}
.nl{transition:color .2s}
dialog[open]{animation:pop .35s cubic-bezier(.22,1,.36,1)}
dialog[open]::backdrop{animation:fade .35s ease}
@keyframes pop{from{opacity:0;transform:translateY(24px) scale(.97)}to{opacity:1;transform:none}}
@keyframes fade{from{opacity:0}to{opacity:1}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}.js .rv{opacity:1;transform:none}}
.panel[hidden]{display:none}
.btn.tg{background:#229ED9;border-color:#229ED9;color:#fff;display:inline-flex;align-items:center;gap:8px;margin-left:auto;font-weight:600;box-shadow:0 4px 14px rgba(34,158,217,.35)}
.btn.tg:hover{background:#1b8cc2}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:10px;margin-top:26px}
.fact{border:1px solid var(--line);border-radius:14px;padding:14px 16px;background:var(--soft)}
.fact b{display:block;font-size:24px;letter-spacing:-.02em;line-height:1.1}
.fact span{display:block;margin-top:5px;font-size:13.5px;color:var(--mute)}
h2.sec{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);font-weight:600;margin:44px 0 6px}
p.sub{font-size:14.5px;color:var(--mute);margin-bottom:14px}
.own{background:#f2f1fb;border:1px solid #dcd9f3;border-radius:26px;padding:24px 22px 22px;margin-top:44px}
.own-h{display:flex;align-items:center;gap:10px}
.own-h h2{font-size:22px;letter-spacing:-.01em}
.own-h .cnt{font-size:13px;font-weight:600;color:#fff;background:#6b5bd6;border-radius:999px;padding:1px 10px}
.own p.sub{margin-top:4px}
.own .card{box-shadow:0 1px 0 rgba(20,22,26,.04),0 8px 24px rgba(80,70,160,.08)}
.xp{border:1px solid var(--line);border-left:5px solid var(--c);border-radius:18px;padding:20px 22px;margin-top:12px}
.xp-h{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;align-items:baseline}
.xp-h b{font-size:18px;display:flex;align-items:center;gap:9px}.xp-h .dot{width:12px;height:12px;border-radius:50%;background:var(--c);display:inline-block}.xp-h span{font-size:13px;color:var(--ct);background:var(--tint);border:1px solid var(--line2);border-radius:999px;padding:2px 11px}
.xp-p{font-size:14.5px;color:var(--mute);margin-top:2px}
.xrow{display:grid;grid-template-columns:130px 1fr;gap:4px 20px;padding:10px 0;border-top:1px solid var(--line);margin-top:10px;font-size:14.5px}
.xrow+.xrow{margin-top:0}
.xrow dt{font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);font-weight:600;padding-top:2px}
.xrow.res{background:var(--tint);border:1px solid var(--line2);border-radius:12px;padding:12px 14px;margin-top:8px}
.xrow.res dt{color:var(--ct)}
.xrow.res li::marker{color:var(--c)}
.xrow ul{padding-left:18px}.xrow li{margin-bottom:3px}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:6px}
.card{border:1px solid var(--line);border-radius:18px;overflow:hidden;background:#fff;display:flex;flex-direction:column}
.cover{height:170px;overflow:hidden;display:flex;justify-content:center;align-items:flex-start;gap:14px;padding-top:18px}
.c-parole{background:#f7e3df}.fc{background:#fff;border-radius:14px;width:150px;height:118px;box-shadow:0 8px 22px rgba(20,22,26,.14);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;margin-top:10px}.fc2{margin-top:30px;opacity:.85;transform:rotate(-4deg)}.fc small{font-size:11px;letter-spacing:.1em;color:#C8473D;font-weight:700}.fc b{font-size:22px}.fc span{font-size:14px;color:var(--mute)}
.c-joyka{background:#e3f4e1}.c-rg{background:#efe6d2}.c-w12{background:#eceef2}.c-oyf{background:#2b2740}
.cover img{display:block;height:auto}
.cover .cp{width:112px;border-radius:16px 16px 0 0;box-shadow:0 0 0 4px #14161a}
.cover .cw{width:340px;border-radius:10px 10px 0 0;box-shadow:0 8px 24px rgba(20,22,26,.18)}
.cover .cw2{width:300px;border-radius:10px 10px 0 0}
.cover .cx{width:100px;border-radius:14px 14px 0 0}
.card .cb{padding:16px 18px 18px;display:flex;flex-direction:column;gap:10px;flex:1}
.card h3{font-size:20px;letter-spacing:-.01em}
.card .d{font-size:14.5px;color:var(--mute)}
.card dl{display:grid;grid-template-columns:70px 1fr;gap:4px 10px;font-size:13.5px}
.card dt{color:var(--mute)}
.card dd.r{color:var(--ok);font-weight:600}
.card .btn{margin-top:auto;align-self:flex-start}
.sk{display:grid;grid-template-columns:repeat(3,1fr);border:1px solid var(--line);border-radius:20px;background:#fff;overflow:hidden}
.sk div{padding:18px 20px;border-left:1px solid var(--line)}
.sk div:first-child{border-left:0}
.sk b{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--mute);display:block;margin-bottom:8px}
.sk span{display:inline-block;font-size:13.5px;padding:3px 10px;border-radius:8px;background:var(--soft);border:1px solid var(--line);margin:0 5px 6px 0}
.contacts{display:grid;grid-template-columns:repeat(3,1fr);margin-top:10px;border:1px solid var(--line);border-radius:20px;background:var(--soft);overflow:hidden}
.contacts a{display:block;padding:18px 20px;border-left:1px solid var(--line);text-decoration:none;font-weight:500;font-size:14.5px}
.contacts a:first-child{border-left:0}
.contacts a:hover{background:#eceef2}
.contacts small{display:block;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);font-weight:600;margin-bottom:4px}
footer{margin:44px 0 32px;color:var(--mute);font-size:13px}
dialog{border:none;border-radius:20px;padding:0;max-width:860px;width:calc(100% - 24px);max-height:92vh;margin:auto;color:var(--ink)}
dialog::backdrop{background:rgba(20,22,26,.55)}
.dh{border-top:0;position:sticky;top:0;background:#fff;border-bottom:1px solid var(--line);padding:14px 20px;display:flex;justify-content:space-between;align-items:center;z-index:2}
.dh h3{font-size:20px}
.dh button{font:inherit;font-size:14px;border:1px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.db{padding:6px 22px 22px}
.gal{display:flex;gap:12px;overflow-x:auto;padding:14px 0;align-items:flex-start}
.gal figure{flex:0 0 auto;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#fff}
.gal .g-m{width:180px}.gal .g-d{width:380px}
.gal img{display:block;width:100%;height:auto}
.drow{display:grid;grid-template-columns:150px 1fr;gap:6px 20px;padding:14px 0;border-top:1px solid var(--line);font-size:15px}
.drow dt{font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);font-weight:600;padding-top:2px}
.drow ol,.drow ul{padding-left:19px}.drow li{margin-bottom:4px}
.drow.res{background:var(--okbg);border:1px solid var(--okline);border-radius:14px;padding:14px 16px;margin:4px 0}
.drow.res dt{color:var(--ok)}
.m3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.m3 div{border:1px solid var(--line);border-radius:12px;padding:10px 12px;font-size:14px;background:var(--soft)}
.m3 small{display:block;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-bottom:4px;font-weight:600}
.m3 ul{padding-left:16px}
@media(max-width:760px){.grid{grid-template-columns:1fr}.sk,.contacts{grid-template-columns:1fr}.sk div,.contacts a{border-left:0;border-top:1px solid var(--line)}.sk div:first-child,.contacts a:first-child{border-top:0}.xrow,.drow{grid-template-columns:1fr}.m3{grid-template-columns:1fr}nav a.nl{display:none}.db{padding:4px 16px 18px}.gal .g-m{width:130px}.gal .g-d{width:260px}}
'''

def li(items): return ''.join('<li>%s</li>' % E(x) for x in items)

def page(L):
    detect = ("<script>try{var s=localStorage.getItem('lang'),n=((navigator.languages&&navigator.languages[0])||navigator.language||'ru').toLowerCase();"
              "if(s==='en'||(!s&&n.indexOf('en')===0)){location.replace('/en/')}}catch(e){}</script>") if L['lang']=='ru' else \
             "<script>try{if(localStorage.getItem('lang')==='ru'){location.replace('/')}}catch(e){}</script>"
    setlang = "try{localStorage.setItem('lang','%s')}catch(e){}" % ('en' if L['alt_label']=='EN' else 'ru')
    o = ['<!doctype html>\n<html lang="%s">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n%s\n<title>%s</title>\n<meta name="description" content="%s">' % (L['lang'], detect, E(L['title']), E(L['desc']))]
    o.append('<link rel="alternate" hreflang="ru" href="/"><link rel="alternate" hreflang="en" href="/en/">')
    o.append('<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:type" content="website">' % (E(L['title']), E(L['desc'])))
    o.append('<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap&subset=cyrillic" rel="stylesheet">')
    o.append('<style>%s</style>\n</head>\n<body>\n<script>document.documentElement.classList.add("js")</script>' % CSS)
    nav = ''.join('<a class="nl" href="%s">%s</a>' % (h, E(t)) for h, t in L['nav'])
    o.append('<header class="top"><div class="wrap"><b>%s</b><nav>%s<div class="lang"><span>%s</span><a href="%s" onclick="%s">%s</a></div></nav></div></header>' % (E(L['name']), nav, L['cur_label'], L['alt_url'], setlang, L['alt_label']))
    o.append('<main class="wrap"><section class="hero"><div class="role">%s</div><h1>%s</h1><p class="lead">%s</p><div class="cta"><a class="btn dark" href="#projects">%s</a><a class="btn" href="#experience">%s</a><a class="btn tg" href="https://t.me/andrew_727"><svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><path fill="currentColor" d="M21.9 4.3 18.6 19.6c-.2 1.1-.9 1.3-1.8.8l-5-3.7-2.4 2.3c-.3.3-.5.5-1 .5l.4-5.1 9.3-8.4c.4-.4-.1-.6-.6-.2L6.1 13 1.2 11.5c-1.1-.3-1.1-1 .2-1.5L20.5 2.6c.9-.3 1.7.2 1.4 1.7z"/></svg>%s</a></div><div class="facts">' % (E(L['role']), E(L['name']), E(L['lead']), E(L['b_proj']), E(L['b_exp']), E(L['b_tg'])))
    for i, (b, t) in enumerate(L['facts']):
        st = ' style="border-top:3px solid %s"' % BRAND[i]['c'] if i < 2 else ''
        o.append('<div class="fact"%s><b>%s</b><span>%s</span></div>' % (st, E(b), E(t)))
    o.append('</div></section>')
    o.append('<h2 class="sec" id="contact" style="margin-top:36px">%s</h2><div class="contacts"><a href="https://t.me/andrew_727"><small>Telegram</small>@andrew_727</a><a href="mailto:perepechayandrew@gmail.com"><small>Email</small>perepechayandrew@gmail.com</a><a href="tel:+79163448547"><small>%s</small>+7 (916) 344-85-47</a></div>' % (E(L['c_h']), E(L['phone'])))
    # опыт
    _keep = o; o = []
    o.append('<h2 class="sec" id="experience">%s</h2>' % E(L['exp_h']))
    xl = L['x_lbl']
    for i, x in enumerate(L['exp']):
        B = BRAND[(0,2,1)[i]]
        o.append('<article class="xp" style="--c:%s;--ct:%s;--tint:%s;--line2:%s"><div class="xp-h"><b><i class="dot"></i>%s</b><span>%s</span></div><div class="xp-p">%s</div><dl>' % (B['c'], B['ct'], B['tint'], B['line'], E(x['co']), E(x['per']), E(x['pos'])))
        o.append('<div class="xrow"><dt>%s</dt><dd>%s</dd></div>' % (E(xl['project']), E(x['project'])))
        o.append('<div class="xrow"><dt>%s</dt><dd>%s</dd></div>' % (E(xl['scale']), E(x['scale'])))
        o.append('<div class="xrow"><dt>%s</dt><dd>%s</dd></div>' % (E(xl['resp']), E(x['resp'])))
        o.append('<div class="xrow res"><dt>%s</dt><dd><ul>%s</ul></dd></div></dl></article>' % (E(xl['res']), li(x['res'])))
    # проекты
    exp_html = ''.join(o); o = []
    o.append('<section class="own" id="projects"><div class="own-h"><h2>%s</h2><span class="cnt">%d</span></div><p class="sub">%s</p><div class="grid">' % (E(L['proj_h']), len(L['projects']), E(L['proj_sub'])))
    pl = L['p_lbl']
    for p in L['projects']:
        o.append('<article class="card" style="border-top:4px solid %s">%s<div class="cb"><h3>%s</h3><p class="d">%s</p><dl><dt>%s</dt><dd>%s</dd><dt>%s</dt><dd>%s</dd><dt>%s</dt><dd class="r">%s</dd></dl><button class="btn" type="button" data-open="%s">%s</button></div></article>' % (
            PCOL[p['id']], cover(p['id'], p['alts'][0]), E(p['name']), E(p['desc']), E(pl['role']), E(p['role']), E(pl['stage']), E(p['stage']), E(pl['res']), E(p['res_short']), p['id'], E(pl['more'])))
    o.append('</div></section>')
    # навыки
    prod_html = ''.join(o); o = _keep
    o.append('<div class="tabs" role="tablist"><i class="ind"></i><button type="button" role="tab" class="on" data-tab="prod">%s</button><button type="button" role="tab" data-tab="exp">%s</button></div>' % (E(L['b_proj']), E(L['b_exp'])))
    o.append('<div class="panel" id="p-prod">' + prod_html + '</div><div class="panel" id="p-exp" hidden>' + exp_html + '</div>')
    o.append('<h2 class="sec" id="skills">%s</h2><div class="sk">' % E(L['sk_h']))
    for t, items in L['skills']:
        o.append('<div><b>%s</b>%s</div>' % (E(t), ''.join('<span>%s</span>' % E(i) for i in items)))
    o.append('</div>')
    o.append('<footer>© 2026 %s</footer></main>' % E(L['name']))
    # диалоги
    dl = L['d_lbl']
    for p in L['projects']:
        o.append('<dialog id="d-%s" aria-labelledby="t-%s"><div class="dh"><h3 id="t-%s">%s</h3><button type="button" data-close>%s</button></div><div class="db">' % (p['id'], p['id'], p['id'], E(p['name']), E(dl['close'])))
        o.append(gallery(p['id'], p['alts']))
        o.append('<dl>')
        o.append('<div class="drow"><dt>%s</dt><dd>%s</dd></div>' % (E(dl['about']), E(p['about'])))
        o.append('<div class="drow"><dt>%s</dt><dd>%s</dd></div>' % (E(dl['problem']), E(p['problem'])))
        o.append('<div class="drow"><dt>%s</dt><dd>%s</dd></div>' % (E(dl['role']), E(p['role_d'])))
        o.append('<div class="drow"><dt>%s</dt><dd><ol>%s</ol></dd></div>' % (E(dl['done']), li(p['done'])))
        o.append('<div class="drow res"><dt>%s</dt><dd><ul>%s</ul></dd></div>' % (E(dl['result']), li(p['result'])))
        o.append('<div class="drow"><dt>%s</dt><dd><div class="m3"><div><small>%s</small>%s</div><div><small>%s</small>%s<ul>%s</ul></div><div><small>%s</small><ul>%s</ul></div></div></dd></div>' % (
            E(dl['metrics']), E(dl['fact']), E(p['fact'][0]), E(dl['main']), E(p['main']), li(p['aux']), E(dl['events']), li(p['events'])))
        o.append('</dl></div></dialog>')
    o.append("""<script>
(function(){
var ds={};[].forEach.call(document.querySelectorAll('dialog'),function(d){ds[d.id]=d});
function open(id){var d=ds['d-'+id];if(d&&!d.open){d.showModal();try{history.replaceState(null,'','#'+id)}catch(e){}}}
[].forEach.call(document.querySelectorAll('[data-open]'),function(b){b.addEventListener('click',function(){open(b.dataset.open)})});
[].forEach.call(document.querySelectorAll('dialog'),function(d){
 d.addEventListener('click',function(e){if(e.target===d||e.target.hasAttribute('data-close'))d.close()});
 d.addEventListener('close',function(){try{history.replaceState(null,'',location.pathname)}catch(e){}});
});
var tb=document.querySelectorAll('[data-tab]');
var ind=document.querySelector('.tabs .ind'),cur='prod',tk=0;
function mv(){var b=document.querySelector('.tabs .on');if(b&&ind){ind.style.width=b.offsetWidth+'px';ind.style.transform='translateX('+(b.offsetLeft-4)+'px)'}}
function tab(n){if(n===cur)return;var from=document.getElementById('p-'+cur),to=document.getElementById('p-'+n),t=++tk;cur=n;
 [].forEach.call(tb,function(b){b.classList.toggle('on',b.dataset.tab===n)});mv();
 from.classList.add('leave');
 setTimeout(function(){if(t!==tk)return;from.hidden=true;from.classList.remove('leave');to.hidden=false;to.classList.remove('enter');void to.offsetWidth;to.classList.add('enter')},200)}
mv();window.addEventListener('load',mv);window.addEventListener('resize',mv);if(document.fonts&&document.fonts.ready)document.fonts.ready.then(mv);
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.08,rootMargin:'0px 0px -40px 0px'});
 [].forEach.call(document.querySelectorAll('.contacts,.tabs,.xp,.card,.sk,.own-h,h2.sec'),function(el){el.classList.add('rv');io.observe(el)})}
[].forEach.call(tb,function(b){b.addEventListener('click',function(){tab(b.dataset.tab)})});
function fromHash(){var h=location.hash.replace('#','');if(!h)return;
 if(ds['d-'+h]){tab('prod');open(h);return}
 if(h==='experience'){tab('exp')}else if(h==='projects'){tab('prod')}
 var el=document.getElementById(h);if(el)el.scrollIntoView()}
fromHash();window.addEventListener('hashchange',fromHash);
})();
</script><script defer src="/_vercel/insights/script.js"></script></body></html>""")
    return '\n'.join(o)

open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(page(RU))
os.makedirs(os.path.join(ROOT, 'en'), exist_ok=True)
open(os.path.join(ROOT, 'en', 'index.html'), 'w', encoding='utf-8').write(page(EN))
print('ok')
