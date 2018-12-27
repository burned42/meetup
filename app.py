from http.server import BaseHTTPRequestHandler
import meetup.api
import debugserver

def get_meetup_url():
    client = meetup.api.Client()
    group_info = client.GetGroup({'urlname': 'dev_night'})
    next_event = client.GetEvent(group_info.next_event)
    return next_event.event_url


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        reponse = f"""
        <html>
            <head>
                <meta http-equiv="refresh" content="0; url={get_meetup_url()}" />
            </head>
        </html>
        """
        self.wfile.write(str(reponse).encode())

        return

if __name__ == '__main__':
    debugserver.serve(handler)