#5998229215:AAECm7CmxPX_vuxugvrHnUn6fePHPWx0rdQ

import telebot
bot = telebot.TeleBot('5998229215:AAECm7CmxPX_vuxugvrHnUn6fePHPWx0rdQ')

@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Привет, я бот-помощник")
    bot.send_message(message.from_user.id, "Я могу делать простые вычисления")
    num_one = bot.send_message(message.chat.id, 'Введи 1 число')
    bot.register_next_step_handler(num_one, num1_fun)

def num1_fun(message):
    global num1
    num1 = message.text
    num_two = bot.send_message(message.chat.id, 'Введи 2 число')
    bot.register_next_step_handler(num_two, num2_fun)

def num2_fun(message):
    global num2
    num2 = message.text
    operu = bot.send_message(message.chat.id, 'Введи действие')
    bot.register_next_step_handler(operu, operi)

def operi(message):
    global oper
    oper = message.text
    if oper == "+":
        result = int(num1) + int(num2)
        bot.send_message(message.chat.id, 'Ответ: ')
        bot.send_message(message.chat.id, result)
    elif oper == "-":
        result = int(num1) - int(num2)
        bot.send_message(message.chat.id, 'Ответ: ')
        bot.send_message(message.chat.id, result)
    elif oper == "*":
        result = int(num1) * int(num2)
        bot.send_message(message.chat.id, 'Ответ: ')
        bot.send_message(message.chat.id, result)
    elif oper == "/":
        result = int(num1) / int(num2)
        bot.send_message(message.chat.id, 'Ответ: ')
        bot.send_message(message.chat.id, result)
    else:
        bot.send_message(message.chat.id, "ошибка ведите /start")

    bot.send_message(message.from_user.id, "Спасибо, Антон, за науку 👍")

bot.polling(none_stop=True)