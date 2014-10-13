from flask import *
import markdown
from subprocess import call
import subprocess
from extract import extract
from datetime import datetime
app = Flask(__name__)

dateformat = '%d.%m.%Y'
def get_event_list(username, password):
    html_raw = subprocess.check_output(['coffee', 'crawl.coffee', username, password])
    days = extract(html_raw)
    content = "### Events\n\n"
    for date, events in days:
        date_ = datetime.strptime(date, dateformat)
        if datetime.now() <=  date_ and events:
            if datetime.now() == date_:
                content += '\n####{}\n\n'.format(date)
            else:
                content += '\n**{}**\n\n'.format(date)
            for event in events:
                content += '* {}\n'.format(event)
            content += '\n'

    return content.decode('utf8', 'replace')

@app.route("/")
def hello():
    username = request.args.get('username')
    password = request.args.get('password')
    content = Markup(markdown.markdown(get_event_list(username, password)))
    return render_template('index.html', **locals())


if __name__ == "__main__":
    app.run()
