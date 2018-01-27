import socket

def log(*args, **kw):
    print('log', *args, **kw)


def route_index():
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body = '<h1>Hello World!</h1>'
    res = header + '\r\n' + body
    response = res.encode('utf-8')
    return response

def response_for_path(path):
    res = {
        '/': route_index,
    }
    response = res[path]
    return response()


def run(host='', port=3000):
    with socket.socket() as s:
        s.bind((host, port))

        while True:
            s.listen(5)
            connection, address = s.accept()
            request = connection.recv(1024)
            request = request.decode('utf-8')
            try:
                path = request.split()[1]
                response = response_for_path(path)
                connection.sendall(response)
            except Exception as e:
                log('error', e) 
            
            connection.close()


def main():
    config = dict(
        host='',
        port=3000,
    )
    run(**config)


if __name__ == '__main__':
    main()  
