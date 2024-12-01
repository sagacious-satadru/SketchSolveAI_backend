from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = 'localhost'
PORT = '8900'
ENV = 'dev'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") # the way load_dotenv works is that it will look for a .env file in the root directory of the project and then load the variables from there. The process to do this is to create a .env file in the root directory of the project and then add the variables in the format of VARIABLE_NAME=VALUE