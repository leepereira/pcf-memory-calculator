FROM python:3.8
RUN pip install pandas

WORKDIR /app

COPY 01-pandas.py /app
COPY entrypoint_wrapper.sh /app
RUN ["chmod", "+x", "entrypoint_wrapper.sh"]

ENTRYPOINT [ "./entrypoint_wrapper.sh" ]




