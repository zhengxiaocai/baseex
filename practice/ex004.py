"""
今日份的题目：
编写一个函数：给一个字符串，判断是否是ipv4的IP。IP由四个数字组成，且值介于0和之间255，则应视为有效。
有效输入：
'1.2.3.4'        
'123.45.67.89'
无效输入：
'1.2.3'
'1.2.3.4.5'
'123.456.78.90'
'123.045.067.089'
"""


def is_valid_ip(s):
    return s.count('.') == 3 and all(i.isdigit() and 0 <= int(i) <= 255 and i == str(int(i)) for i in s.split('.'))


if __name__ == '__main__':
    print(is_valid_ip('12.255.56.1') is True)
    print(is_valid_ip('') is False)
    print(is_valid_ip('abc.def.ghi.jkl') is False)
    print(is_valid_ip('123.456.789.0') is False)
    print(is_valid_ip('12.34.56') is False)
    print(is_valid_ip('12.34.56 .1') is False)
    print(is_valid_ip('12.34.56.-1') is False)
    print(is_valid_ip('123.045.067.089') is False)
    print(is_valid_ip('127.1.1.0') is True)
    print(is_valid_ip('0.0.0.0') is True)
    print(is_valid_ip('0.34.82.53') is True)
    print(is_valid_ip('192.168.1.300') is False)

    """
    总结：
        1.'45 '的合法性，可以用 s.isdigit() 来判断，因为它有一个空格。
            通过这个判断完，还可以防止字母混入接下来的判断，出异常。
        2.'045'的合法性，可以用 str(int(s)) == s 来判断
        3.all()
        4.custom_str.isdigit() 判断字符串是否有纯数字组成
        5.and 是短路的
    """
