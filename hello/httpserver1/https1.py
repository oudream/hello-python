# 生成 SSL 证书：在当前目录中生成 SSL 证书：
# openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.pem -days 365 -nodes


# curl -k -X POST https://localhost:4443/device -d '{"device_id": "123", "device_name": "DeviceXYZ"}' -H 'Content-Type: application/json'


import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl


# 定义数据类
class DeviceRequest:
    def __init__(self, device_id, device_name):
        self.device_id = device_id
        self.device_name = device_name


class DeviceResponse:
    def __init__(self, success, message, data=""):
        self.success = success
        self.message = message
        self.data = data


# HTTP 服务器请求处理程序
class DeviceRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 仅在 /device 路径上处理请求
        if self.path == '/device':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                request_data = json.loads(post_data.decode('utf-8'))
                device_request = DeviceRequest(**request_data)

                response = DeviceResponse(
                    success=True,
                    message=f"Received device request for {device_request.device_name} ({device_request.device_id})",
                    data=json.dumps(request_data)
                )
            except (json.JSONDecodeError, KeyError):
                response = DeviceResponse(
                    success=False,
                    message="Invalid request data"
                )

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response.__dict__).encode('utf-8'))
        else:
            self.send_error(404, "Not Found: The requested resource was not found.")

    def do_GET(self):
        self.send_response(404)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Endpoint not found"}).encode('utf-8'))


# 启动 HTTPS 服务器
def run(server_class=HTTPServer, handler_class=DeviceRequestHandler, port=4443, cert_file='server.pem',
        key_file='server.key'):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    # 加载 SSL 证书和密钥
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        certfile=cert_file,
        keyfile=key_file,
        server_side=True
    )

    print(f'Starting HTTPS server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    # 请确保有 server.pem 和 server.key 证书文件用于 SSL
    run(cert_file='server.pem', key_file='server.key')
