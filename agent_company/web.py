from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import json
from .company import start_company_task
from .db import get_activities

class Handler(BaseHTTPRequestHandler):
    def reply(self, text, ctype='text/html'):
        data = text.encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', ctype + '; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == '/api/dashboard':
            data = {
                'mode':'SIMULATION',
                'agents': {
                    'CEO':'READY',
                    'Research':'WAITING',
                    'Developer':'WAITING',
                    'Marketing':'WAITING'
                },
                'activities':[x[0] for x in get_activities()]
            }
            self.reply(json.dumps(data, ensure_ascii=False), 'application/json')
        else:
            html = Path(__file__).parent / 'web' / 'index.html'
            self.reply(html.read_text(encoding='utf-8'))

    def do_POST(self):
        if self.path == '/api/start':
            start_company_task()
            self.reply(json.dumps({'status':'started'}), 'application/json')

def serve():
    server = HTTPServer(('0.0.0.0', 10000), Handler)
    print('AI Company 001 running')
    server.serve_forever()
