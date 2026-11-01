import datetime
import pathlib
import re

EXCUSES = [
    "Это не баг, это недокументированная фича.",
    "У меня на Fedora это работало.",
    "Оно само сломалось, я вообще не трогал.",
    "Это нейросеть виновата. Любая. Какая-нибудь.",
    "Я не прокрастинирую, я жду, пока исправят зависимость.",
    "Тесты прошли. Просто не те, которые нужны.",
    "Код ревьюил я сам, я не заметил ошибок. Подозрительно.",
    "Кэш. Всегда виноват кэш.",
    "Было 3 ночи, мне тогда казалось, что это гениально.",
    "Я не опоздал с дедлайном, я его расширил.",
    "Это не костыль, это бионический протез для кода.",
    "git blame указывает на меня из прошлого, а он всегда был идиотом.",
    "Чумба, это временное решение. Ему уже три месяца.",
    "Сначала кофе, потом принципы SOLID.",
]

today = datetime.date.today()
excuse = EXCUSES[today.toordinal() % len(EXCUSES)]

readme = pathlib.Path("README.md")
text = readme.read_text(encoding="utf-8")
block = f"<!--EXCUSE:START-->\n> 💬 **Оправдание дня ({today:%d.%m.%Y}):** {excuse}\n<!--EXCUSE:END-->"
new, n = re.subn(r"<!--EXCUSE:START-->.*?<!--EXCUSE:END-->", block, text, flags=re.S)
if n:
    readme.write_text(new, encoding="utf-8")
