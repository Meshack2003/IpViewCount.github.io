import os
from flask import Flask, request, render_template

app = Flask(__name__)

# Set to store unique IP addresses
visitor_ips = set()


@app.route('/')
def index():
    # Get the IP address of the visitor
    visitor_ip = request.remote_addr

    # Check if the IP address is new
    if visitor_ip not in visitor_ips:
        visitor_ips.add(visitor_ip)

    # Counter is the size of the set
    visitor_count = len(visitor_ips)

    return render_template('index.html', visitor_count=visitor_count)


if __name__ == '__main__':
   # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))  # Default port is 5000 if PORT env var is not found
    app.run(host='0.0.0.0', port=port)
