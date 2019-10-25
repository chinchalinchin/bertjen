FROM python:3.8.0-alpine
LABEL com.ibm.maintainer="Grant Moore <grant.moore@ibm.com>"
RUN apk update && apk upgrade && apk add bash
WORKDIR /home/bertulator/
CMD ["bash", "-c","python ./bertjen.py"]
COPY /berts/ /home/bertulator/berts/
COPY /jens/ /home/bertulator/jens/
COPY /bertjen.py /home/bertulator/