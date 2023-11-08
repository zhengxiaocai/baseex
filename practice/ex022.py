def html_special_chars(data):
    """ 初版，分步replace """
    return data.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def html_special_chars_update(data):
    """ custom_str.translate(str.maketrans()) """
    symbols = {'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}
    return data.translate(str.maketrans(symbols))


if __name__ == '__main__':
    html_special_chars = html_special_chars_update
    print(html_special_chars("<h2>Hello World</h2>") == "&lt;h2&gt;Hello World&lt;/h2&gt;")
    print(html_special_chars("Hello, how would you & I fare?") == "Hello, how would you &amp; I fare?")
    print(html_special_chars('How was "The Matrix"?  Did you like it?') ==
          'How was &quot;The Matrix&quot;?  Did you like it?')
    print(html_special_chars("<script>alert('Website Hacked!');</script>") ==
          "&lt;script&gt;alert('Website Hacked!');&lt;/script&gt;")
