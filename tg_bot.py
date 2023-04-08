#5998229215:AAECm7CmxPX_vuxugvrHnUn6fePHPWx0rdQ

import telebot
from telebot import types
bot = telebot.TeleBot('5998229215:AAECm7CmxPX_vuxugvrHnUn6fePHPWx0rdQ')

@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Привет, я бот-помощник")
    bot.send_message(message.from_user.id, "Я могу делать простые вычисления")
    bot.send_message(message.from_user.id, " +   -   *   /   **  sqrt")
    num_one = bot.send_message(message.chat.id, 'Введи 1 число')
    bot.register_next_step_handler(num_one, num1_fun)

def num1_fun(message):
    global num1
    num1 = message.text
    num1 = num1.replace(',', '.')
    num_two = bot.send_message(message.chat.id, 'Введи 2 число')
    bot.register_next_step_handler(num_two, num2_fun)

def num2_fun(message):
    global num2
    num2 = message.text
    num2 = num2.replace(',', '.')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('+')
    btn2 = types.KeyboardButton('-')
    btn3 = types.KeyboardButton('*')
    btn4 = types.KeyboardButton('/')
    btn5 = types.KeyboardButton('**')
    btn6 = types.KeyboardButton('sqrt')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    operu = bot.send_message(message.from_user.id, "Выбери операцию", reply_markup=markup)
    bot.register_next_step_handler(operu, operi)

def operi(message):
    try:
        global oper
        oper = message.text
        if oper == "+":
            result = float(num1) + float(num2)
            bot.send_message(message.chat.id, 'Ответ: ')
            bot.send_message(message.chat.id, result)
        elif oper == "-":
            result = float(num1) - float(num2)
            bot.send_message(message.chat.id, 'Ответ: ')
            bot.send_message(message.chat.id, result)
        elif oper == "*":
            result = float(num1) * float(num2)
            bot.send_message(message.chat.id, 'Ответ: ')
            bot.send_message(message.chat.id, result)
        elif oper == "/":
            result = float(num1) / float(num2)
            bot.send_message(message.chat.id, 'Ответ: ')
            bot.send_message(message.chat.id, result)
        elif oper == "**":
            result = float(num1) ** float(num2)
            bot.send_message(message.chat.id, 'Ответ: ')
            bot.send_message(message.chat.id, result)
        elif oper == "sqrt":
            result = float(num1) ** 0.5
            bot.send_message(message.chat.id, 'Ответ: ')
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, "Нет такой операции 🤷‍♀️, нажми /start")
    except ValueError:
        bot.send_message(message.chat.id, "Нет такого числа 🤷‍♀️, нажми /start")


    bot.send_message(message.from_user.id, "Спасибо, Антон, за науку 👍")

bot.polling(none_stop=True)