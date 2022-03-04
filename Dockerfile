# AMD64
# FROM pandoc/core:2.17-ubuntu as pandoc-python3-base 
# M1 chip - ARM64
FROM issakuss/pandoc:2.17.1.1 as pandoc-python3-base 

WORKDIR /app

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev git wget curl nano \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# --------------------------------------------

FROM pandoc-python3-base as pandoc-app

ADD ./ /app/
RUN chmod 755 /app/convert.sh
RUN pip3 install -r requirements.txt


ENTRYPOINT [ "/app/convert.sh" ]