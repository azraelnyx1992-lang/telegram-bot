import telebot
import random

TOKEN = "8495880705:AAE5rEWQPGxdZmT-IhCSH5qOn5gTOMC7SN8"

bot = telebot.TeleBot(TOKEN)


# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! 👋\n\n"
        "Я генерирую случайные числа 🎲\n\n"
        "Используй:\n"
        "/roll 1 10 3\n\n"
        "Можно и так:\n"
        "/roll 1 50 (одно число)"
    )


# 🔥 Команда /roll (вместо /rand)
@bot.message_handler(commands=['roll'])
def roll(message):
    try:
        parts = message.text.split()

        if len(parts) < 3:
            bot.send_message(message.chat.id, "❗ Пример: /roll 1 10 3")
            return

        a = int(parts[1])
        b = int(parts[2])

        count = int(parts[3]) if len(parts) > 3 else 1

        if a > b:
            a, b = b, a

        range_size = b - a + 1

        if count > range_size:
            bot.send_message(
                message.chat.id,
                f"❌ В диапазоне только {range_size} чисел"
            )
            return

        if count > 100:
            bot.send_message(message.chat.id, "❌ Максимум 100 чисел")
            return

        numbers = random.sample(range(a, b + 1), count)

        if count == 1:
            bot.send_message(
                message.chat.id,
                f"🎲 Число: {numbers[0]}"
            )
        else:
            result = ", ".join(map(str, numbers))
            bot.send_message(
                message.chat.id,
                f"🎲 Результат:\n{result}"
            )

    except ValueError:
        bot.send_message(message.chat.id, "❌ Пример: /roll 1 10 3")


print("Бот запущен...")
bot.infinity_polling()
