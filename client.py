import socket
import ssl

# 解析url，返回返回(protocol, host, port, path)
def parsed_url(url):
    protocol = 'http'
    port = 80
    path = ''
    host = url

    if '://' in url:
        protocol, host = url.split('://')
        if protocol == 'https':
            port = 443
    
    if '/' in host:
        host, path = host.split('/', 1)

    if ':' in host:
        host, port = host.split(':')
        port = int(port)

    path = '/' + path
    
    return protocol, host, port, path


def socket_by_protocol(protocol):
    if protocol == 'https':
        s = ssl.wrap_socket(socket.socket())
    else:
        s = socket.socket()
    return s


def response_by_socket(s):
    res = b''
    buffer_size = 1024
    while True:
        r = s.recv(buffer_size)
        if len(r) == 0:
            break
        res += r
    return res


# 解析response，返回(status_code, headers, body)
def parse_response(r):
    header, body = r.split('\r\n\r\n', 1)
    h = header.split('\r\n')
    status_code = int(h[0].split()[1])

    headers = {}
    for line in h[1:]:
        k, v = line.split(': ')
        headers[k] = v
    return status_code, headers, body


# 把向服务器发送 HTTP 请求
# 得到status_code（int）, headers（dict）, body
def get(url, query=None):
    protocol, host, port, path = parsed_url(url)

    s = socket_by_protocol(protocol)
    
    s.connect((host, port))

    ip, port = s.getsockname()

    http_request = 'GET/ HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n'.format(host)

    encoding = 'utf-8'
    request = http_request.encode(encoding)

    s.send(request)

    response = response_by_socket(s)

    r = response.decode(encoding)

    status_code, headers, body = parse_response(r)

    if status_code in [301, 302]:
        url = headers['location']
        return get(url)

    return status_code, headers, body


def main():
    url = 'https://www.bing.com/'
    status_code, headers, body = get(url)
    print(status_code, headers, body)


if __name__ == '__main__':
    main()
