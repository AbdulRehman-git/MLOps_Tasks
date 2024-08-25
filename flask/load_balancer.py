# from flask import Flask, request, Response
# import requests

# app = Flask(__name__)


# BACKENDS = [
#     'http://localhost:5000',
#     'http://localhost:5001'
# ]

# current_backend = 0

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])

# def proxy(path):
#     global current_backend

#     # Get the URL of the backend server to which the request will be forwarded
#     backend = BACKENDS[current_backend]

#     # Update round-robin index
#     current_backend = (current_backend + 1) % len(BACKENDS)

#     # Forward the request to the backend server
#     url = f"{backend}/{path}"
#     resp = requests.request(
#         method=request.method,
#         url=url,
#         headers=dict(request.headers),
#         data=request.get_data(),
#         cookies=request.cookies,
#         allow_redirects=False
#     )

#     # Return the response from the backend server to the client
#     return Response(
#         resp.content,
#         status=resp.status_code,
#         headers=dict(resp.headers)
#     )

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=8080)





from flask import Flask, request
import requests

app = Flask(__name__)

servers = ["http://backend-server1:5000", "http://backend-server2:5001"]
counter = 0

@app.route("/")
def load_balancer():
    global counter
    server = servers[counter % len(servers)]
    counter += 1
    try:
        response = requests.get(server)
        return response.content
    except requests.exceptions.RequestException as e:
        return f"Error connecting to backend: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

