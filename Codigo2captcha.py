# Link de video de explicacion
# https://youtu.be/OJyFMWujXZo

# Código de Python

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(_file_))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'xxxxxxxxxxx')

solver = TwoCaptcha(api_key)

try:
    result = solver.normal("ruta_de_imagen")

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))