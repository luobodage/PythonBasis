# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/04/30
# software: PyCharm
#         =    =     =
#          =   =   =
#           =  =  =
#         ===========
#         =   萝    =
#         =   卜    =
#         =   神    =
#         =   保    =
#         =   佑    =
#         =   永    =
#         =   无    =
#         =   bug  =
#          =      =
#           =    =
#              =
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Cookie': 'wordpress_b296963d5ad5f67200a8e68fec7e557a=luobo%7C1619942742%7CB3trFQfSHgKewooeEru43YrxWmYRD2UbYLD8Nf2CqNY%7C95553dc4c8ad59392b39ae12aa2480ec8286961f10b953fca7a2d79302bb51a4; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_b296963d5ad5f67200a8e68fec7e557a=luobo%7C1619942742%7CB3trFQfSHgKewooeEru43YrxWmYRD2UbYLD8Nf2CqNY%7C0540d5628123a394e87526921b32a35039515df7e6a955db89189b5eb6a84c7f; language=en-gb; currency=USD; lhc_vid=b3aa6f91f810f4cc995c; __atuvc=2%7C16',
}
content = requests.get(url='http://zmzlove.xyz/wordpress/wp-admin/',headers=headers)
print(content.ok)
print(content.status_code)
print(content.text)