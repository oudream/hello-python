from flask import Flask, request, jsonify
from OpenSSL import SSL

app = Flask(__name__)


class DeviceRequest:
    def __init__(self, device_id, device_name):
        self.device_id = device_id
        self.device_name = device_name


class DeviceResponse:
    def __init__(self, success, message, data=""):
        self.success = success
        self.message = message
        self.data = data


@app.route('/device', methods=['POST'])
def handle_device_request():
    try:
        request_data = request.get_json()
        device_request = DeviceRequest(**request_data)

        response = DeviceResponse(
            success=True,
            message=f"Received device request for {device_request.device_name} ({device_request.device_id})",
            data=request_data
        )
    except (TypeError, KeyError):
        response = DeviceResponse(
            success=False,
            message="Invalid request data"
        )

    return jsonify(response.__dict__)


if __name__ == '__main__':
    # 请确保有 server.pem 和 server.key 证书文件用于 SSL
    context = SSL.Context(SSL.SSLv23_METHOD)
    context.use_privatekey_file('server.key')
    context.use_certificate_file('server.pem')

    app.run(host='0.0.0.0', port=4443, ssl_context=('server.pem', 'server.key'))
