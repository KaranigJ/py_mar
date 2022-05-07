from CONFIG import bot
from CONFIG import link
from CONFIG import chat
from telebot import types
import csv_func as csv

сurators = []
csv.read('members.csv', сurators)

allus = []
csv.read('alluser.csv', allus)

crmen = '👨‍🏫Меню куратора‍'

menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
cmenu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
inf = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
curmenu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
dz_markap = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
quests = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

infmenu = types.KeyboardButton('Информация')
rate = types.KeyboardButton('Рейтинг')
curator = types.KeyboardButton(crmen)
curator_сh = types.KeyboardButton('Куратор')
quest_b = types.KeyboardButton('Задания')

mymem = types.KeyboardButton('Мои участники')
curinfo = types.KeyboardButton('Информация📚')

table = types.KeyboardButton('Расписание')
course = types.KeyboardButton('Инструкции к выполнению курса')
dz = types.KeyboardButton('Инструкции к выполнению ДЗ')
info = types.KeyboardButton('Информационный канал')

dz1 = types.KeyboardButton('Домашнее задание номер 1')
#    dz2 = types.KeyboardButton('Домашнее задание номер 2')
#    dz3 = types.KeyboardButton('Домашнее задание номер 3')
#    dz4 = types.KeyboardButton('Домашнее задание номер 4')

q1 = types.KeyboardButton('Задание номер 1')
q2 = types.KeyboardButton('Задание номер 2')
q3 = types.KeyboardButton('Задание номер 3')
q4 = types.KeyboardButton('Задание номер 4')

back = types.KeyboardButton('Назад')

curmenu.add(mymem, curinfo, back)
inf.add(table, course, dz, info, back)
menu.add(quest_b, rate, curator_сh, infmenu)
cmenu.add(quest_b, rate, curator_сh, curator, infmenu)
dz_markap.add(dz1, back)
quests.add(q1, q2, q3, q4, back)

@bot.message_handler(commands=['send'])
def send(message):
    text = 'Уважаемый куратор! Статистика ответов по 1 заданию и баллы обновлены.' \
           ' Вы можете найти всю информацию в "меню куратора" по кнопкам "Мои участники" меню.'
    for i in range(len(сurators)):
        print(сurators[i][0])
        bot.send_message(сurators[i][1], text)

def guser(message):
    user = [message.text]
    csv.rewrite('users.csv', user)
    bot.send_message(message.chat.id, 'Данные получены', reply_markup=menu)

@bot.message_handler(commands=['start'])
def start(message):
    member = [f'{message.from_user.first_name} {message.from_user.last_name}', f'{message.from_user.id}', f'{message.from_user.username}']

    if member not in сurators:
        сurators.append(member)
        csv.write('members.csv', сurators)

    msg = bot.send_message(message.chat.id, 'Напишите ваше имя')
    bot.register_next_step_handler(msg, guser)

@bot.message_handler(content_types=['text'])
def get_text(message):
    def check(text):
        mem = [f'{message.from_user.first_name} {message.from_user.last_name}', f'{message.from_user.id}', f'{message.from_user.username}']
        if mem in сurators:
            bot.send_message(message.chat.id,
                            text,
                             reply_markup=cmenu)
        else:
            bot.send_message(message.chat.id,
                             text,
                             reply_markup=menu)

    if message.chat.id == 443257481:
        txt = message.text
        for i in range(len(allus)):
            bot.send_message(allus[i][1], txt)


    if message.text == 'Назад':
        check('Основное меню')

    if message.text == 'Задания':
        bot.send_message(message.chat.id, 'Задания:', reply_markup=quests)

    if message.text == 'Задание номер 1':
        bot.send_message(message.chat.id, '1')
    elif message.text == 'Задание номер 2':
        bot.send_message(message.chat.id, '2')
    elif message.text == 'Задание номер 3':
        bot.send_message(message.chat.id, '3')
    elif message.text == 'Задание номер 4':
        bot.send_message(message.chat.id, '4')

    if message.text == 'Информация':
        bot.send_message(message.chat.id, 'Информационные меню', reply_markup=inf)

    if message.text == 'Инструкции к выполнению курса':
        print('course')
        bot.send_message(message.chat.id,'У вас будет на выбор несколько заданий, каждое из которых принесёт вам определённое количество баллов(2, 4, 8 баллов).\n\n'
                                        'Для получения бОльшего количества баллов, рекомендуется выполнять все задаия.\n\n'
                                        'Если задание выполнено не полностью или некорректно, то количество баллов уменьшается пропорционально количеству неточностей.\n\n'
                                        'Ответ отправляется ТОЛЬКО 1 РАЗ. Повторные ответы учитываться не будут.\n\n'
                                        'Количество набранных баллов будет суммироваться и участвововать в рейтинге всех участников марафона.\n\n'
                                        'Кураторы не участвуют в начислении баллов.\n\n'
                                        'Крайний срок выполнения задания — до выхода следующего урока(дата следующего урока указана в боте марафона и на платформе Getcourse)\n\n'
                                        'Есть возможность дополнительного получения баллов, о которой вы можете узнать у кураторов.\n\n',
                                        parse_mode='html')

    elif message.text == 'Инструкции к выполнению ДЗ':
        bot.send_message(message.chat.id, 'Выберете интструкцию к какому заданию хотите получить', reply_markup=dz_markap)

    elif message.text == 'Информационный канал':
        ch_markup = types.InlineKeyboardMarkup()
        ch_markup.add(types.InlineKeyboardButton('Информационный канал', url=chat))
        bot.send_message(message.chat.id, 'Марафон "Кризис. Зона роста."', reply_markup=ch_markup)

    elif message.text == 'Расписание':
        bot.send_message(message.chat.id, '<b>25 апреля:</b> Кризис и главный фактор риска\n<b>28 апреля:</b> Кризис и финансы\n'
                                          '<b>02 мая:</b> Кризис. Трамплин к мечте\n<b>04 мая:</b> Кризис. Прорыв\n<b>05 мая:</b> Кризис. За линией страха',
                         parse_mode='html')

    if message.text == 'Куратор':
        all_cur = types.InlineKeyboardMarkup(row_width=1)
        gi = types.InlineKeyboardButton('Гребнева Ирина', url='https://t.me/+_Prgd1rS2Uc3MTQy')
        mm = types.InlineKeyboardButton('Троц Марина', url='https://t.me/+uxYWaMlr5RoxOTBi')
        tk = types.InlineKeyboardButton('Кислая Татьяна', url=link)
        el = types.InlineKeyboardButton('Вайнилович Елена', url='https://t.me/+JTyr8ADNZ_E0ZDEy')
        nt = types.InlineKeyboardButton('Трусь Наталья', url='https://t.me/+F29DwEh9J0Q5MGUy')
        sv = types.InlineKeyboardButton('Евтушик Святослав', url='https://t.me/sonarostaes')
        kl = types.InlineKeyboardButton('Котусова Людмила', url='https://t.me/LiudmilaKotusova')
        dk = types.InlineKeyboardButton('Кислый Денис', url=link)
        ma = types.InlineKeyboardButton('Левкович Матвей', url=link)
        ki = types.InlineKeyboardButton('Кузьминский Игорь', url=link)
        all_cur.add(ma, sv, mm, dk, ki)
        bot.send_message(message.chat.id, 'Выберите вашего куратора', reply_markup=all_cur)

    all = []
    csv.read('Curator/All.csv', all)

    if message.text == 'Рейтинг':
        bot.send_message(message.chat.id, 'Место: Участник : Баллы')
        for i in range(len(all)):
            text = f'{i+1}: {all[i][0]} : {float(all[i][1])}'
            bot.send_message(message.chat.id, text)

    if message.text == crmen:
        bot.send_message(message.chat.id, 'Меню кураторов', reply_markup=curmenu)

    greb = []
    csv.read('Curator/Гребнева.csv', greb)
    troc = []
    csv.read('Curator/Троц.csv', troc)
    evtu= []
    csv.read('Curator/Евтушик.csv', evtu)
    trus = []
    csv.read('Curator/Трусь.csv', trus)
    vain = []
    csv.read('Curator/Вайнилович.csv', vain)
    kots = []
    csv.read('Curator/Котусова.csv', kots)

    if message.text == 'Мои участники':
        if message.chat.id == 742739821: #Гребнева
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1P_wW6kwpj5QXOPYWAmc2NyuOjj7SnQ-4u42fM6KJ8bI/edit?usp=sharing')
            for i in range(len(greb)):
                text = f'{greb[i][0]} : {float(greb[i][1])}'
                bot.send_message(message.chat.id, text)
    if message.text == 'Мои участники':
        if message.chat.id == 531433683: #Котусова
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1P_wW6kwpj5QXOPYWAmc2NyuOjj7SnQ-4u42fM6KJ8bI/edit?usp=sharing')
            for i in range(len(kots)):
                text = f'{kots[i][0]} : {float(kots[i][1])}'
                bot.send_message(message.chat.id, text)
        elif message.chat.id == 1383469137:#Троц
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1_vUmD-MiKx2Kpubvies9-qym6mdRp2sZqZURe_QLjkg/edit?usp=sharing')
            for i in range(len(troc)):
                text = f'{troc[i][0]} : {float(troc[i][1])}'
                bot.send_message(message.chat.id, text)
        elif message.chat.id == 1121927226:#Евтушик
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1z8F433XA4pqMscGHmP9h_sWgbkAIYgNX03SLGO_AQU8/edit?usp=sharing')
            for i in range(len(evtu)):
                text = f'{evtu[i][0]} : {float(evtu[i][1])}'
                bot.send_message(message.chat.id, text)
        elif message.chat.id == 650172724:#Трусь
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1WIZdBedtZvAkXD1xSnbVjgFM2q2cII0oQYKHQO5iips/edit?usp=sharing')
            for i in range(len(trus)):
                text = f'{trus[i][0]} : {float(trus[i][1])}'
                bot.send_message(message.chat.id, text)
        elif message.chat.id == 315332801:#Вайнилович
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1577Jea9eSXLxc7Zs7FTm4loSs63uleGf7iacRNmNgWI/edit?usp=sharing')
            for i in range(len(vain)):
                text = f'{vain[i][0]} : {float(vain[i][1])}'
                bot.send_message(message.chat.id, text)
        elif message.chat.id == 405934214:#Я
           bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1577Jea9eSXLxc7Zs7FTm4loSs63uleGf7iacRNmNgWI/edit?usp=sharing')
           for i in range(len(greb)):
               text = f'{greb[i][0]} : {float(greb[i][1])}'
               bot.send_message(message.chat.id, text)

    elif message.text == 'Информация📚':
        bot.send_message(message.chat.id, 'Дополнительное начисление баллов за приобретённую продукцию:\n'
                                            '1. пакет Начальный – 20 баллов\n'
                                            '2. пакет Стандарт – 40 баллов\n'
                                            '3. пакет Вип – 60 баллов\n'
                                            '4. пакет Инвестор – 100 баллов\n'
                                            '5. пакет Инвестор 2 – 150 баллов\n'
                                            '6. пакет Инвестор 3 – 300 баллов\n'
                                            '7. пакет Инвестор Премиум – 500 баллов\n'
                                            '8. Бизнес-вход Молодёжный – 120 баллов\n'
                                            '9. Бизнес-вход Базовый – 160 баллов\n'
                                            '10. Бизнес-вход Быстрый старт – 360 баллов\n'
                                            '11. Годовая бизнес активность – 20 баллов\n')

    if message.text == 'Домашнее задание номер 1':
        v = open('Vid/1.mp4', 'rb')
        bot.send_message(message.chat.id, 'Подождите пока придёт файл.')
        bot.send_video(message.chat.id, v)

print('start')
bot.polling(none_stop=True)
print('stop')