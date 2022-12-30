FROM python:3.8
USER root
RUN mkdir /app
COPY . /app/
WORKDIR /app/
RUN pip3 install -r requirement.txt
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True
RUN airflow db init
RUN airflow users create -e bhevendra2@gmail.com -f Bhevendra -l Gurjar -p admin -r Admin -u admin
RUN chmod 777 start.sh
RUN apt update -y && apt instll awscli -y
ENTRYPOINT ["/bin/sh"]
CMD ["start.sh"]
