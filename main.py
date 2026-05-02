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
        "Я генерирую случайные числа БЕЗ повторов 🎲\n\n"
        "Используй команду:\n"
        "/rand 1 10 3\n\n"
        "Где:\n"
        "1 — от\n"
        "10 — до\n"
        "3 — сколько чисел"
    )


# Команда /rand
@bot.message_handler(commands=['rand'])
def rand(message):
    try:
        parts = message.text.split()

        # Проверка аргументов
        if len(parts) < 4:
            bot.send_message(
                message.chat.id,
                "❗ Пример: /rand 1 10 3"
            )
            return

        a = int(parts[1])
        b = int(parts[2])
        count = int(parts[3])

        # Если перепутали границы
        if a > b:
            a, b = b, a

        # Размер диапазона
        range_size = b - a + 1

        # Проверка: нельзя больше чисел, чем есть в диапазоне
        if count > range_size:
            bot.send_message(
                message.chat.id,
                f"❌ Ошибка!\n"
                f"В диапазоне всего {range_size} уникальных чисел"
            )
            return

        # Ограничение (чтобы не спамили)
        if count > 100:
            bot.send_message(
                message.chat.id,
                "❌ Слишком много чисел (макс 100)"
            )
            return

        # Генерация БЕЗ повторов
        numbers = random.sample(range(a, b + 1), count)

        # Красивый вывод
        result = ", ".join(map(str, numbers))

        bot.send_message(
            message.chat.id,
            f"🎲 Победители:\n{result}"
        )

    except:
        bot.send_message(
            message.chat.id,
            "❌ Ошибка!\nПример: /rand 1 10 3"
        )


# Запуск бота
print("Бот запущен...")
bot.polling()
