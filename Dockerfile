FROM dockerfile/nodejs
RUN npm install -g coffee-script
RUN npm install -g phantomjs

RUN apt-get update && apt-get install -y
RUN apt-get install -y libfreetype6 libfontconfig bzip2
ADD package.json /app/
WORKDIR /app
RUN npm install
ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt
WORKDIR /app

