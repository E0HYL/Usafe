#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import string
import random
from Crypto.Cipher import AES
import binascii


def keyGenerater(length):  # 生成指定长度的秘钥
    if length not in (16, 24, 32):
        return None
    x = string.ascii_letters+string.digits
    return ''.join([random.choice(x) for i in range(length)])


def encryptor_decryptor(key, mode):
    return AES.new(key, mode, b'0000000000000000')


# 使用指定密钥和模式对给定信息进行加密
def AESencrypt(key, mode, text):
    # 明文必须以字节串形式，且长度为16的倍数
    text_encoded = text.encode()
    text_length = len(text_encoded)
    padding_length = 16 - text_length % 16
    text_encoded = text_encoded + b'0'*padding_length

    encryptor = encryptor_decryptor(key, mode)
    return encryptor.encrypt(text_encoded)


# 使用指定密钥和模式对给定信息进行解密
def AESdecrypt(key, mode, text):
    decryptor = encryptor_decryptor(key, mode)
    tmp = decryptor.decrypt(text)
    return tmp.decode().strip('0')


if __name__ == '__main__':
    # text = 'Python3.50 is excellent.'
    # key = keyGenerater(16)
    # # 随机选择AES的模式
    # mode = random.choice((AES.MODE_CBC, AES.MODE_CFB, AES.MODE_ECB, AES.MODE_OFB))
    # if not key:
    #     print('Something is wrong.')
    # else:
    #     print('key:', key)
    #     print('mode:', mode)
    #     print('Before encryption:', text)
    #
    #     text_encrypted = AESencrypt(key, mode, text)
    #     print('After encryption:', text_encrypted)

    de_key = 'Be056eZU6JVAybUp'
    de_mes = b'\x89\xf9\xd9\x1aF\x92\xdc?E\x06\xd1\x95I\x19J\x8a>\xc53\x8d?)w!\xbe"\xa6q^^yj\xee\xc2\xd3^\x7f#\xefy\xa5\xfb/\x18\xd4(\x99\x06xP\x80\xdd3\x82"\xcft\xeb\x82r\x94\xea\xeb\xd0=\xc6+\xaa\x87i>\xb1d\xc6|\xed\xc6\xa1\xbc\x15\x8fc\x07>\xe6\xfd\xae\x07\x8c\x01m;\xde\x8e!I\xe5\xf2\x8f\x95\xdc2\r%\x99\xe1\x07+F7\x94S\x8f\x17\xaeLu\x05\xe4W\x84\n79uK\xe6\x8fP\xbe\x8c}\xe5\xe7(\x08:\x0c\xe0%\xc9\x01\xc3\x12\xb6\x82\x00\x17\xe4\xe1\xb3\xd1?\xe4\xf1/\xe3\x04N.X_zH\x92\x80\x15>\x93A\xeem)\xabY0\xdf\xff\xff}\xa5T\xca\x85{\x18^\xb7\xcc\x98\xa5L-E\xbb\xfc9[Vi!A\xa8*%+\x18\'\xef\xc8@Q\xaf\xd7a\x0f:\xe3\r\xf3\xb2\x0c!_ru\xb2\x17\x9b!k\x8b\xe7\x88\xb8 \xab\xca\xc7\x8c\xfe\xa8?G\x9b\x0b\x90\xe8\x99[\xc7\x9b\xfa\xb1D\xab}\x94Lbd\x1f\xa7\x8e\xecK!\x8b%\x03_\x18\xc2i\x81\xfa\x0f\x9d\xc3XG\'\xed9\xf0k\x01\xdeJ\xfa\xb0\x05\xe2\xec7|\x7f\xa9\x0c\xfa\xce\xf5\x8f\xfc'
    text_decrypted = AESdecrypt(de_key, AES.MODE_CFB, de_mes)
    print('--------After decryption--------\n%s' % text_decrypted)
