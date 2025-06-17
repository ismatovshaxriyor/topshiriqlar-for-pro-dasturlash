from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }
]

class SimpleHTTPRequstHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle GET requests
        if self.path == "/data":
            self.send_response(200)

            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        elif self.path.startswith("/data/"):
            try:
                item_id = int(self.path.split("/")[-1])
                for items in data:
                    if items["id"] == item_id:
                        self.send_response(200)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode())
                        break
                else:
                    self.send_error(404)
            except ValueError:
                self.send_error(400)
        else:
            self.send_error(404)

    def do_POST(self):
        # Handle POST requests
        if self.path == "/data":
            content_length = int(self.headers["Content-Length"])
            print("Content Length:", content_length)
            post_data = self.rfile.read(content_length)
            new_item = json.loads(post_data.decode())
            new_item["id"] = len(data) + 1
            data.append(new_item)
            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.send_header("Location", "/data/{}".format(new_item["id"]))
            self.end_headers()
            self.wfile.write(json.dumps(new_item).encode())
        else:
            self.send_error(404)

    def do_PUT(self):
        if self.path.startswith("/data/"):
            item_id = int(self.path.split("/")[-1])
            for i, items in enumerate(data):
                if items["id"] == item_id:
                    content_length = int(self.headers["Content-Length"])
                    put_data = self.rfile.read(content_length)
                    update_item = json.loads(put_data)
                    update_item["id"] = item_id
                    data[i] = update_item
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(update_item).encode())
                    break
            else:
                self.send_error(404)
        else:
            self.send_error(404)

    def do_DELETE (self):
        # Handle DELETE requests
        if self.path.startswith("/data/"):
            item_id = int(self.path.split("/")[-1])
            for i, item in enumerate(data):
                if item["id"] == item_id:
                    del data[i]
                    self.send_response(204)
                    self.end_headers()
                    break
            else:
                self.send_error(404)
        else:
            self.send_error(404)

if __name__ == "__main__":
    httpd = HTTPServer(("localhost", 8080), SimpleHTTPRequstHandler)
    print("Server started...")
    httpd.serve_forever()