def http_error(staus):
    match staus:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(500))


def check_permission(staus):
    match staus:
        case 200:
            return "OK - 请求成功"
        case 302 | 301:
            return "Redirect - 重定向"
        case 401 | 403 | 404:
            return "Not allowed - 无权限或未找到"
        case 500 | 502 | 503:
            return "Server Error - 服务器错误"
        case _:
            return "Unknow staus - 未知状态码"

for code in[200,301,403,500,418]:
    print(f"状态码{code}:{check_permission(code)}")
