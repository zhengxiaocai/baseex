from collections import defaultdict


class RouterMine:
    """小编解法，主键是path，多层嵌套"""

    def __init__(self):
        self.__route = defaultdict(dict)

    def bind(self, p, m, f):
        self.__route[p][m] = f

    def runRequest(self, p, m):
        r_p = self.__route.get(p)
        if r_p:
            r_m = r_p.get(m)
            if r_m:
                return r_m()
        return 'Error 404: Not Found'


class Router:
    """ 大佬解法，元组 (path, method) 做主键"""

    def __init__(self):
        self._routes = {}

    def bind(self, url, method, action):
        self._routes[(url, method)] = action

    def runRequest(self, url, method):
        return self._routes.get((url, method), lambda: "Error 404: Not Found")()


if __name__ == '__main__':
    router = Router()
    router.bind('/hello', 'GET', lambda: 'hello world')
    router.bind('/login', 'GET', lambda: 'Please log-in.')

    print(router.runRequest('/hello', 'GET') == 'hello world')
    print(router.runRequest('/login', 'GET') == 'Please log-in.')

    router = Router()
    router.bind('/vote', 'POST', lambda: 'Voted.')
    router.bind('/comment', 'POST', lambda: 'Comment sent.')

    print(router.runRequest('/vote', 'POST') == 'Voted.')
    print(router.runRequest('/comment', 'POST') == 'Comment sent.')

    router = Router()
    router.bind('/login', 'GET', lambda: 'Please log-in.')
    router.bind('/login', 'POST', lambda: 'Logging-in.')

    print(router.runRequest('/login', 'GET') == 'Please log-in.')
    print(router.runRequest('/login', 'POST') == 'Logging-in.')

    router = Router()
    print(router.runRequest('/this-url-does-not-exist', 'GET') == 'Error 404: Not Found')

    router = Router()
    router.bind('/page', 'GET', lambda: 'First binding.')
    router.bind('/page', 'GET', lambda: 'Modified binding.')

    print(router.runRequest('/page', 'GET') == 'Modified binding.')
