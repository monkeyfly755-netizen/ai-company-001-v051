from http.server import BaseHTTPRequestHandler,HTTPServer
from pathlib import Path
import json
from .workflow import start_workflow,state
from .db import get_activities

class Handler(BaseHTTPRequestHandler):
    def send(self,data,ctype='text/html'):
        b=data.encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type',ctype+';charset=utf-8')
        self.send_header('Content-Length',str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        if self.path=='/api/dashboard':
            self.send(json.dumps({
                'agents':state,
                'activities':get_activities()
            },ensure_ascii=False),'application/json')
        else:
            self.send((Path(__file__).parent/'web'/'index.html').read_text(encoding='utf-8'))

    def do_POST(self):
        if self.path=='/api/start':
            length=int(self.headers.get('Content-Length',0))
            body=self.rfile.read(length).decode('utf-8')
            goal=json.loads(body).get('goal','测试任务')
            start_workflow(goal)
            self.send(json.dumps({'status':'started'}),'application/json')

def serve():
    HTTPServer(('0.0.0.0',10000),Handler).serve_forever()
