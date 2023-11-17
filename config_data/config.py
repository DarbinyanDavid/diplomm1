import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("low", "Поиск фильма/мультфильма с низким рейтингом"),
    ("High", "Поиск фильма/мультфильма с высоким рейтингом"),
    ("History", "Истоия поиска")
)


url_1 = "https://imdb-top-100-movies.p.rapidapi.com/top32"
url_2 = "https://imdb-top-100-movies.p.rapidapi.com/"



headers = {
	"X-RapidAPI-Key": "df3ab69933msh2583fa28e2ad7b2p167456jsne76b137bd394",
	"X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}