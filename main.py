import CONFIG
from CONFIG import bot
from CONFIG import link
from CONFIG import  chat
from telebot import types
import csv_func as csv

markup_check = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
yes_button = types.KeyboardButton('Да')
no_button = types.KeyboardButton('Нет')
markup_check.add(yes_button, no_button)

@bot.message_handler(commands=['start'])
def start(message):
    member = [f'{message.from_user.first_name} {message.from_user.last_name}', f'{message.from_user.id}']
    mes = f'Добро пожаловать на курс, {member[0]}!\nУ вас уже есть приложение Getcourse.ru?'

    bot.send_message(message.chat.id, mes, reply_markup=markup_check)

#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#    back = types.KeyboardButton('↩К началу')

#    markup.add( back)
#    bot.send_message(message.chat.id, mes, parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    if message.text == 'Да':
        step = 0
        next = types.KeyboardButton(f'{step+1})Авторизация Далее➡')
        markup.add(next)
        bot.send_message(message.chat.id, 'Первый шаг к авторизации. Если вы перепутали кнопку, дойдите до конца регистрации не выполняя пунктов,'
                                          ' а затем выберите кнопку "На старт!"', reply_markup=markup)
    elif message.text == 'Нет':
        step = 0
        next = types.KeyboardButton(f'{step + 1})Регистрация Далее➡')
        markup.add(next)
        bot.send_message(message.chat.id, 'Первый шаг. Если вы перепутали кнопку, дойдите до конца регистрации не выполняя пунктов,'
                                          ' а затем выберите кнопку "На старт!"')
        markup_get = types.InlineKeyboardMarkup()
        markup_get.add(types.InlineKeyboardButton('Перейти к регистрации', url=link))
        bot.send_message(message.chat.id, 'Перейдите по ссылке для начала ругистрации.', reply_markup=markup_get)
        bot.send_message(message.chat.id, 'Нажмите далее чтобы получить следующий шаг', reply_markup=markup)

    def next_but_a(markup, count):
        step = count
        next = types.KeyboardButton(f'{step + 1})Авторизация Далее➡')
        markup.add(next)
        if count == 1:
            bot.send_message(message.chat.id, 'Нажмите кнопку "Авторизоваться и найти"', reply_markup=markup)
            file = open('Photo/12.png', 'rb')
            bot.send_photo(message.chat.id, file)
        elif count == 2:
            bot.send_message(message.chat.id, 'Нажмите кнопку "Войти по почте"', reply_markup=markup)
            file = open('Photo/13.png', 'rb')
            bot.send_photo(message.chat.id, file)
        elif count == 3:
            bot.send_message(message.chat.id, 'Введите вашу электронную почту и нажмите "получить ссылку для входа"', reply_markup=markup)
            file = open('Photo/14.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/3.gif', 'rb')
            bot.send_video(message.chat.id, vid)
        elif count == 4:
            bot.send_message(message.chat.id, 'Перейдите в почту и найдите там письмо от Chatium.\n'
                                              'Если его нет в основных письмах проверьте папку спам.\n'
                                              'Если его нет и там, проверьте правильность почты и попробуйте ещё раз.\n'
                                              'В письме есть ссылка, нажав на которую вы увидите код, который необходимо запомнить.',
                             reply_markup=markup)
            file = open('Photo/3.png', 'rb')
            file1 = open('Photo/4.png', 'rb')
            file2 = open('Photo/5.png', 'rb')

            bot.send_photo(message.chat.id, file)
            bot.send_photo(message.chat.id, file1)
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/4.gif', 'rb')
            bot.send_video(message.chat.id, vid)
        elif count == 5:
            bot.send_message(message.chat.id, 'Возвращаемся в Getcourse и вводим полученый код в специальное поле',
                             reply_markup=markup)
            file = open('Photo/6.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/5.gif', 'rb')
            bot.send_video(message.chat.id, vid)
        elif count == 6:
            bot.send_message(message.chat.id, 'Открываем меню избранного')
            file = open('Photo/8.png', 'rb')
            file1 = open('Photo/9.png', 'rb')
            file2 = open('Photo/10.png', 'rb')
            bot.send_photo(message.chat.id, file)
            bot.send_message(message.chat.id,
                             'Находим кнопку настройка избранного и ставим галочку напротив practicumtk',
                             reply_markup=markup)
            bot.send_photo(message.chat.id, file1)
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/7.gif', 'rb')
            bot.send_video(message.chat.id, vid)
        elif count == 7:
            bot.send_message(message.chat.id,
                             'Возвращаемся назад в избранное при помощи стрелки назад на телефоне и находим там курс',
                             reply_markup=markup)
            file2 = open('Photo/11.png', 'rb')
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/8.gif', 'rb')
            bot.send_video(message.chat.id, vid)

    def next_but_r(markup, count):
        step = count
        next = types.KeyboardButton(f'{step + 1})Регистрация Далее➡')
        markup.add(next)
        if count == 1:
            bot.send_message(message.chat.id, 'Найдите кнопку скачать приложение', reply_markup=markup)
            file = open('Photo/1.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/1.gif', 'rb')
            bot.send_video(message.chat.id, vid)
        elif count == 2:
            bot.send_message(message.chat.id, 'Установите приложение', reply_markup=markup)
            vid = open('Vid/2.gif', 'rb')
            bot.send_video(message.chat.id, vid)
        elif count == 3:
            bot.send_message(message.chat.id, 'Введите вашу электронную почту и нажмите "получить ссылку для входа"', reply_markup=markup)
            file = open('Photo/2.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/3.gif', 'rb')
            bot.send_video(message.chat.id, vid)
        elif count == 4:
            bot.send_message(message.chat.id, 'Перейдите в почту и найдите там письмо от Chatium.\n'
                                              'Если его нет в основных письмах проверьте папку спам.\n'
                                              'Если его нет и там, проверьте правильность почты и попробуйте ещё раз.\n'
                                              'В письме есть ссылка, нажав на которую вы увидите код, который необходимо запомнить.', reply_markup=markup)
            file = open('Photo/3.png', 'rb')
            file1 = open('Photo/4.png', 'rb')
            file2 = open('Photo/5.png', 'rb')

            bot.send_photo(message.chat.id, file)
            bot.send_photo(message.chat.id, file1)
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/4.gif', 'rb')
            bot.send_video(message.chat.id, vid)
        elif count == 5:
            bot.send_message(message.chat.id, 'Возвращаемся в Getcourse и вводим полученый код в специальное поле', reply_markup=markup)
            file = open('Photo/6.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/5.gif', 'rb')
            bot.send_video(message.chat.id, vid)
        elif count == 6:
            bot.send_message(message.chat.id, 'Нажимаем кнопку зарегистрироваться с помощью email', reply_markup=markup)
            file = open('Photo/7.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/6.gif', 'rb')
            bot.send_video(message.chat.id, vid)
        elif count == 7:
            bot.send_message(message.chat.id, 'Открываем меню избранного')
            file = open('Photo/8.png', 'rb')
            file1 = open('Photo/9.png', 'rb')
            file2 = open('Photo/10.png', 'rb')
            bot.send_photo(message.chat.id, file)
            bot.send_message(message.chat.id, 'Находим кнопку настройка избранного и ставим галочку напротив practicumtk', reply_markup=markup)
            bot.send_photo(message.chat.id, file1)
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/7.gif', 'rb')
            bot.send_video(message.chat.id, vid)
        elif count == 8:
            bot.send_message(message.chat.id, 'Возвращаемся назад в избранное при помощи стрелки назад на телефоне и находим там курс', reply_markup=markup)
            file2 = open('Photo/11.png', 'rb')
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/8.gif', 'rb')
            bot.send_video(message.chat.id, vid)

    if message.text == '1)Авторизация Далее➡':
        next_but_a(markup, 1)
    elif message.text == '2)Авторизация Далее➡':
        next_but_a(markup, 2)
    elif message.text == '3)Авторизация Далее➡':
        next_but_a(markup, 3)
    elif message.text == '4)Авторизация Далее➡':
        next_but_a(markup, 4)
    elif message.text == '5)Авторизация Далее➡':
        next_but_a(markup, 5)
    elif message.text == '6)Авторизация Далее➡':
        next_but_a(markup, 6)
    elif message.text == '7)Авторизация Далее➡':
        next_but_a(markup, 7)
        bot.send_message(message.chat.id, 'Поздравляю с авторизацией на курсе!', reply_markup=menu)


    if message.text == '1)Регистрация Далее➡':
        next_but_r(markup, 1)
    elif message.text == '2)Регистрация Далее➡':
        next_but_r(markup, 2)
    elif message.text == '3)Регистрация Далее➡':
        next_but_r(markup, 3)
    elif message.text == '4)Регистрация Далее➡':
        next_but_r(markup, 4)
    elif message.text == '5)Регистрация Далее➡':
        next_but_r(markup, 5)
    elif message.text == '6)Регистрация Далее➡':
        next_but_r(markup, 6)
    elif message.text == '7)Регистрация Далее➡':
        next_but_r(markup, 7)
    elif message.text == '8)Регистрация Далее➡':
        next_but_r(markup, 8)
        bot.send_message(message.chat.id, 'Поздравляю с регистрацией на курсе!\n\nЯ ваш помощник! Вы всегда можешь обратиться ко мне за помощью😉', reply_markup=menu)

    back = types.KeyboardButton('Назад')
    if message.text == 'Назад':
        bot.send_message(message.chat.id,'Основное меню', reply_markup=menu)


    if message.text == 'Инструкции к выполнению курса':
        print('course')
        bot.send_message(message.chat.id,'Уроки будут выходить по понедельникам и четвергам в <b>10:00 МСК</b>\n\n'
                                        'Срок выполнения домашнего задания — <b>до</b> момента выхода <b>следующего</b> урока\n\n'
                                        'За <b>своевременное</b> выполнение домашних заданий вам будут начисляться баллы,'
                                        'по итогам которых вы можете выиграть <b>ценные призы</b>\n\n'
                                        'Также баллы будут начисляться за <b>приглашение в марафон</b> своих знакомых\n\n'
                                        'В комментариях пишем сообщения,<b> относящиеся к марафону</b>, никакого <s>негатива</s> и <s>сторонних ссылок</s>',
                                        parse_mode='html')
    elif message.text == 'Инструкции к выполнению ДЗ':
        dz_markap = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        dz1 = types.KeyboardButton('Домашнее задание номер 1')
    #    dz2 = types.KeyboardButton('Домашнее задание номер 2')
    #    dz3 = types.KeyboardButton('Домашнее задание номер 3')
    #    dz4 = types.KeyboardButton('Домашнее задание номер 4')
        dz_markap.add(dz1, back)
        bot.send_message(message.chat.id, 'Выберете интструкцию к какому заданию хотите получить', reply_markup=dz_markap)
    elif message.text == 'Информационный канал':
        ch_markup = types.InlineKeyboardMarkup()
        ch_markup.add(types.InlineKeyboardButton('Информационный канал', url=chat))
        bot.send_message(message.chat.id, 'Марафон "Кризис. Зона роста."', reply_markup=ch_markup)
    elif message.text == 'Расписание':

        bot.send_message(message.chat.id, '<b>25 апреля:</b> Кризис и главный фактор риска\n<b>28 апреля:</b> Кризис и финансы\n'
                                          '<b>02 мая:</b> Кризис. Трамплин к мечте\n<b>04 мая:</b> Кризис. Прорыв\n<b>05 мая:</b> Кризис. За линией страха',
                         parse_mode='html')
    if message.text == 'На старт!':
        bot.send_message(message.chat.id, 'У вас уже есть приложение Getcourse.ru?', reply_markup=markup_check)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
course = types.KeyboardButton('Инструкции к выполнению курса')
dz = types.KeyboardButton('Инструкции к выполнению ДЗ')
info = types.KeyboardButton('Информационный канал')
table = types.KeyboardButton('Расписание')
again = types.KeyboardButton('На старт!')
menu.add(course, dz, info, table, again)



   # elif message.text == '↩К началу':
    #    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    #    start = types.KeyboardButton('/start')
    #    markup.add(start)
    #    bot.send_message(message.chat.id, 'Давайте начнем?', reply_markup=markup)


print('start')
bot.polling(none_stop=True)
