FROM python:latest
LABEL com.ibm.maintainer="Grant Moore <grant.moore@ibm.com>"
COPY /berts/ /home/bertulator/berts/
COPY /jens/ /home/bertulator/jens/
COPY /bertjen.py /home/bertulator/
WORKDIR /home/bertulator/
CMD ["bash", "-c","python ./bertjen.py"]