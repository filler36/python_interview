import socket


def parse_http(http):
    request, *headers, _, body = http.split('\r\n')
    method, path, protocol = request.split(' ')
    headers = dict(line.split(':', maxsplit=1) for line in headers)
    return method, path, protocol, headers, body


def view(request):
    return f'Hello Dear {request[-1]}!'


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
    server_socket.bind(('localhost', 8000))
    server_socket.listen(1)
    while True:
        conn, addr = server_socket.accept()
        http_request = conn.recv(1024).decode('utf-8')
        print(http_request)
        request = parse_http(http_request)
        response = view(request)
        http_response = process_response(response)
        conn.sendall(http_response.encode('utf-8'))
        conn.close()
