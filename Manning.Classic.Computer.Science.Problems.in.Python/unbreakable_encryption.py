# coding=utf-8
# @Time    : 2019-03-29 16:33
# @Author  : 张嘉麒
# @File    : unbreakable_encryption.py

"""
一次性密码使用
设置随机值
用数据对随机值进行异或运算
得到两个密码

解码的时候对两个密码做异或运算
得到数据本身
"""
from secrets import token_bytes
from typing import  Tuple

def random_key(length: int) ->int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode() # 转为Bytes
    dummy: int = random_key(len(original_bytes)) # 获取随机的key
    original_key: int = int.from_bytes(original_bytes, "big") # 随机的key转二进制
    encrypted: int = original_key ^ dummy  # 进行异或运算 两次异或运算就能得到其本身
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+7) // 8, "big")
    return temp.decode()

if __name__ == "__main__":
    key1, key2 = encrypt("Hello")
    result: str = decrypt(key1, key2)