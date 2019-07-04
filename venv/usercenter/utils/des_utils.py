#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyDes import des, ECB, PAD_PKCS5
import binascii

NO_SESSION_KEY = "C86EA4369B61AE5E"
OUT_PUBLIC_KEY = "A891167560B398D8"
NON_SESSION_SID = -1

'''
    本实现类采用DES/ECB/PKCS5Padding作为基础加密算法，采用两轮加密方式。 第一轮加密（也即内层加密）采用用户会话的Token作为Key
    第二轮加密（也即外层加密）采用客户端、服务器端均知晓的公共Key
    若用户并未登录，即Session为null的情况，则使用另外一个客户端、服务器均知晓的功能Key,NON_SESSION_TOKEN
'''


class DesUtil(object):
    @classmethod
    def encrypt_data(cls, plain_text=None, session_id=0, token=None):
        """
        使用DES算法进行加密（两次）并返回密文。
        若处于未登录状态，内层加密密钥使用nonSessionKey； 若处于登录状态，内层加密密钥使用Session#getToken()返回的字符串。
        :param plain_text:明文
        :param session_id:用户会话ID
        :param token:用户会话token
        :return:加密后的密文
        """
        plain_text = plain_text.encode('utf-8')
        try:
            sid = NON_SESSION_SID
            inner_cipher_key = NO_SESSION_KEY
            # 判断是否有session id
            if session_id > 0:
                sid = session_id
                inner_cipher_key = token

            # 第一次加密，使用token进行加密
            first_secret_key = des(bytes.fromhex(inner_cipher_key), ECB, b"\0\0\0\0\0\0\0\0", pad=None,
                                   padmode=PAD_PKCS5)
            first_encrypt_text = first_secret_key.encrypt(plain_text)
            # print("第一次加密结果：" + binascii.b2a_hex(first_encrypt_text).decode('utf-8'))

            # 使用第一次加密的结果，与sid组合，构造被加密文本
            plain_text = binascii.b2a_hex(first_encrypt_text).decode('utf-8') + "|" + str(sid)

            # 第二次加密,使用OUT_PUBLIC_KEY加密
            second_secret_key = des(bytes.fromhex(OUT_PUBLIC_KEY), ECB, b"\0\0\0\0\0\0\0\0", pad=None,
                                    padmode=PAD_PKCS5)
            final_data = second_secret_key.encrypt(plain_text)
            # print("第二次加密结果：" + binascii.b2a_hex(final_data).decode('utf-8'))
            return binascii.b2a_hex(final_data).decode('utf-8')
        except Exception as e:
            print(e)

    @classmethod
    def decrypt_data(cls, cipher_text=None, token=None):
        """
        使用DES算法进行解密（两次）并返回明文
        若处于未登录状态，内层加密密钥使用nonSessionKey； 若处于登录状态，内层加密密钥使用Session#getToken()返回的字符串。
        :param cipher_text:密文(String)
        :param token:解密以后的明文
        :return:
        """

        try:
            # 第一次解密，通过OUT_PUBLIC_KEY进行解密
            inner_cipher_key = des(bytes.fromhex(OUT_PUBLIC_KEY), ECB, b"\0\0\0\0\0\0\0\0", pad=None,
                                   padmode=PAD_PKCS5)

            first_decrypt_text = inner_cipher_key.decrypt(bytes.fromhex(cipher_text))

            # 对第一次解密出来数据进行拆分，以“|” 为分割符，如果长度不为2，则解密失败,
            # 分割以后，最后一部分的只为“-1",则表示为未登陆时，进行的加密，因此使用NO_SESSION_KEY解密
            cipher_text = first_decrypt_text.decode('utf-8')
            # print("第一次解密后类容：" + cipher_text)

            cipher_text_list = cipher_text.split("|")
            if len(cipher_text_list) != 2:
                raise Exception("第一次解密以后字符串有问题，解密失败：" + cipher_text)

            if cipher_text_list[-1] == "-1":
                outer_cipher_key = des(bytes.fromhex(NO_SESSION_KEY), ECB, b"\0\0\0\0\0\0\0\0", pad=None,
                                       padmode=PAD_PKCS5)
            else:
                outer_cipher_key = des(bytes.fromhex(token), ECB, b"\0\0\0\0\0\0\0\0", pad=None,
                                       padmode=PAD_PKCS5)
            second_decrypt_text = outer_cipher_key.decrypt(bytes.fromhex(cipher_text_list[0]))
            # print("第二次解密后的类容：" + second_decrypt_text.decode('utf-8'))

            return second_decrypt_text.decode('utf-8')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    str1 = "测试加解密"
    print("加密前的内容: ", str1)
    encrypt_data = DesUtil.encrypt_data(str1, 63254590, "3411BCCE3FD3B956")
    print("加密后的内容: ", encrypt_data)
    data = DesUtil.decrypt_data(encrypt_data, "3411BCCE3FD3B956")
    print("解密后的内容: ", data)
