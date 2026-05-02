import telebot
import random
import time

TOKEN = "8495880705:AAE5rEWQPGxdZmT-IhCSH5qOn5gTOMC7SN8"

bot = telebot.TeleBot(TOKEN)


# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! 👋\n\n"
        "Я генерирую случайные числа БЕЗ повторов 🎲\n\n"
        "Используй команду:\n"
        "/rand 1 10 3\n\n"
        "Можно также:\n"
        "/rand 1 50 (одно число)"
    )


# Команда /rand
@bot.message_handler(commands=['rand'])
def rand(message):
    try:
        parts = message.text.split()

        # минимум 2 числа
        if len(parts) < 3:
            bot.send_message(message.chat.id, "❗ Пример: /rand 1 10 [3]")
            return

        a = int(parts[1])
        b = int(parts[2])

        # если не указали количество → 1
        count = int(parts[3]) if len(parts) >= 4 else 1

        # если перепутали
        if a > b:
            a, b = b, a

        range_size = b - a + 1

        if count > range_size:
            bot.send_message(
                message.chat.id,
                f"❌ В диапазоне всего {range_size} чисел"
            )
            return

        if count > 100:
            bot.send_message(message.chat.id, "❌ Макс 100 чисел")
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
                f"🎲 Победители:\n{result}"
            )

    except Exception as e:
        print("Ошибка:", e)
        bot.send_message(
            message.chat.id,
            "❌ Ошибка!\nПример: /rand 1 10 3"
        )


# (опционально) ответ на любые сообщения
@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.send_message(
        message.chat.id,
        "Я понимаю команды 😅\nИспользуй /rand 1 10 3"
    )


# 🔥 защита от падений (ВАЖНО для Railway)
print("Бот запущен...")

while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as e:
        print("Ошибка polling:", e)
        time.sleep(5)
