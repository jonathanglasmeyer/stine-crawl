from flask import *
import markdown
from subprocess import call
import subprocess
from datetime import datetime
import time
import os

from extract import extract
app = Flask(__name__)
wd = os.path.dirname(os.path.realpath(__file__))
dateformat = '%d.%m.%Y'
date_output_format = '%a, %d.%m'
def get_event_list(username, password):
    html_raw = subprocess.check_output(
            ['coffee', os.path.join(wd,'crawl.coffee'), username, password])
    days = extract(html_raw)
    content = "###Today: {}\n\n".format(time.strftime(date_output_format))
    for date, events in days:
        date_ = datetime.strptime(date, dateformat)
        if datetime.now() <=  date_ and events:
            date_formatted = date_.strftime(date_output_format)
            if datetime.now() == date_:
                content += '\n###{}\n\n'.format(date_formatted)
            else:
                content += '\n**{}**\n\n'.format(date_formatted)
            for event in events:
                content += '* {}\n'.format(event)
            content += '\n'

    return content.decode('utf8', 'replace')

@app.route("/")
def main():
    username = request.args.get('username')
    password = request.args.get('password')
    content = Markup(markdown.markdown(get_event_list(username, password)))
    return render_template('index.html', **locals())

@app.route("/hello")
def hello():
    return 'heshoetnllo'

if __name__ == "__main__":
    app.run()
