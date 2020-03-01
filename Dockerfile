FROM 114.116.245.220:5000/ubuntu:latest
MAINTAINER pandas wangjuchn@outlook.com
ADD . /usr/src
VOLUME /usr/src
WORKDIR /usr/src
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x run.sh
CMD /bin/bash /usr/src/run.sh





