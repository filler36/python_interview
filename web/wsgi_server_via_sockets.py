import socket
from io import StringIO


def parse_http(http):
    request, *headers, _, body = http.split('\r\n')
    method, path, protocol = request.split(' ')
    headers = dict(line.split(':', maxsplit=1) for line in headers)
    return method, path, protocol, headers, body


def to_environ(method, path, protocol, headers, body):
    return {
        'REQUEST_METHOD': method,
        'PATH_INFO': path,
        'SERVER_PROTOCOL': protocol,
        'wsgi.input': StringIO(body),
        **{'HTTP_' + key: value for key, value in headers.items()},
    }


def start_response(status, headers):
    conn.sendall(f'HTTP/1.1 {status}\r\n'.encode('utf-8'))
    for (key, value) in headers:
        conn.sendall(f'{key}: {value}\r\n'.encode('utf-8'))
    conn.sendall('\r\n'.encode('utf-8'))


def view(environ):
    print(environ["wsgi.input"])
    return f'Hello Dear {environ["wsgi.input"].read()}!'


def application(environ, start_response):
    response = view(environ)
    start_response('200 OK', [('Content-Length', len(response))])
    return [response]


def process_response(response):
    return (
        'HTTP/1.1 200 OK\r\n'
        f'Content-Lenth: {len(response)}\r\n'
        'Content-Type: text/html\r\n'
        '\r\n'
        f'{response}'
        '\r\n'
    )


if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(('localhost', 8001))
    server_socket.listen(1)
    while True:
        conn, addr = server_socket.accept()
        http_request = conn.recv(1024).decode('utf-8')
        print('REQUEST:\r\n', http_request, sep='', end='\n--------------------\n')
        request = parse_http(http_request)
        environ = to_environ(*request)
        print('ENVIRON:', environ, sep='', end='\n--------------------\n')
        response = application(environ, start_response)

        for data in response:
            conn.sendall(data.encode('utf-8'))
        conn.close()
