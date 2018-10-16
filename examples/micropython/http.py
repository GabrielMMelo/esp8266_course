import socket

def http_get(url):
        _, _, host, path = url.split('/', 3)
        addr = socket.getaddrinfo(host, 80)[0][-1]
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
        while True:
            data = s.recv(100)
            if data:
                print(str(data, 'utf8'), end='')
            else:
                break
                s.close()

def http_server():
    html = """<!DOCTYPE html>
    <html>
        <head> <title>ESP8266 Pins</title> </head>
        <body> <h1>ESP8266 Pins</h1>
            <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
        </body>
    </html>
    """
    addr = socket.getaddrinfo('192.168.0.101', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)

    while True:
            cl, addr = s.accept()
            print('client connected from', addr)
            cl_file = cl.makefile('rwb', 0)
            while True:
                    line = cl_file.readline()
                    if not line or line == b'\r\n':
                            break
#            rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
#            response = html % '\n'.join(rows)
            test = "teste" 
            response = html % '\n'.join(test)
            cl.send(response)
            cl.close()
