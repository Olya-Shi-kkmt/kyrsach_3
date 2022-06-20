import os #библиотека функций для работы с операционной системой

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

admin_id = [ 5086015886 ]