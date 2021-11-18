from Crypto.Cipher import AES
import base64


BLOCK_SIZE = 16  # Bytes
def pad(s): return s + (BLOCK_SIZE - len(s) %
                        BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


def unpad(s): return s[:-ord(s[len(s) - 1:])]


def aesEncrypt(key, data):
    '''
    AES的ECB模式加密方法
    :param key: 密钥
    :param data:被加密字符串（明文）
    :return:密文
    '''
    key = key.encode('utf8')
    # 字符串补位
    data = pad(data)
    cipher = AES.new(key, AES.MODE_ECB)
    # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    result = cipher.encrypt(data.encode())
    encodestrs = base64.b64encode(result)
    enctext = encodestrs.decode('utf8')
    return enctext


def aesDecrypt(key, data):
    '''

    :param key: 密钥
    :param data: 加密后的数据（密文）
    :return:明文
    '''
    key = key.encode('utf8')
    data = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_ECB)

    # 去补位
    text_decrypted = unpad(cipher.decrypt(data))
    text_decrypted = text_decrypted.decode('utf8')
    return text_decrypted


def getKey(n):
    dic = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(dic)
    key = ''

    while True:
        key = dic[n % length] + key
        n //= length

        if n == 0:
            return key


if __name__ == '__main__':

    # data = aesEncrypt("f1aGf1aGf1aGf1aG", r"flag{S0C0d1nGAeSpUzZlE}")
    # print(data)

    ecdata = 'wlvAf86kRSKdiCQ4Vbqe/KdTZVBD19o6TXhThxA30ak='

    cnt = 0
    for i in range(1000000000000000000000):
        key = getKey(i)
        if len(key) != 4:
            continue

        cnt += 1
        data = None
        try:
            data = aesDecrypt(key*4, ecdata)
        except Exception:
            data = ""

        print(key, data, cnt/14776336*100)
        if 'flag' in data:
            break
