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
        "Используй:\n"
        "/rand 1 10 3\n\n"
        "Можно и так:\n"
        "/rand 1 10 (по умолчанию 1 число)"
    )


# Команда /rand
@bot.message_handler(commands=['rand'])
def rand(message):
    parts = message.text.split()

    # ❗ если не команда /rand — игнор
    if not message.text.startswith("/rand"):
        return

    try:
        if len(parts) < 3:
            bot.send_message(message.chat.id, "❗ Пример: /rand 1 10 3")
            return

        a = int(parts[1])
        b = int(parts[2])

        # если не указали количество → ставим 1
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

        result = ", ".join(map(str, numbers))

        bot.send_message(
            message.chat.id,
            f"🎲 Результат:\n{result}"
        )

    except ValueError:
        # ❗ только если реально ошибка ввода
        bot.send_message(message.chat.id, "❌ Пример: /rand 1 10 3")


print("Бот запущен...")
bot.infinity_polling()
