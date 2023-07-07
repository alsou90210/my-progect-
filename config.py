import os 
from dotenv import load_dotenv 
load_dotenv()

TOKEN = os.environ.get('TOKEN')
if __name__ == '__main__':
    print(TOKEN)
