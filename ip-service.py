from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import json
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        ip = json.loads(subprocess.run('ip -j a'.split(),capture_output=True).stdout.decode())[1]['addr_info'][0]['local']

        html = f"""
        <html>
            <head><title>Backend Python</title></head>
            <body>
                <h1>Backend Python</h1>
                <p>Hostname : {hostname}</p>
                <p>IP : {ip}</p>
            </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Server running on port 8080")
    server.serve_forever()
