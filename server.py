import datetime

def app(environ, start_response):
    """WSGI application"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [b"Hello, World! the time is: %s" % time.encode('utf-8')]
