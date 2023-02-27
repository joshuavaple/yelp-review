FROM python:3.9.16-slim


COPY . /app

# set working directory as /app
WORKDIR /app

# copy the requirements.txt file to the Docker image
COPY requirements.txt requirements.txt

# use the RUN command to execute the command pip3 install. 
# This works exactly the same as if we were running pip3 install locally on our machine, 
# but this time the modules are installed into the image.
RUN pip3 install -r requirements.txt && \
    pip3 install -e .


# The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime. 
# Your container needs to listen to Streamlit’s (default) port 8501
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# v1.0
# CMD streamlit run --server.port 8080 --server.enableCORS false ./streamlit/app.py

# v1.1
# CMD streamlit run ./streamlit/app.py

# v1.2, 1.3
# ENTRYPOINT ["streamlit", "run", "./streamlit/app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# v1.4 - google cloud run
EXPOSE 8080
CMD streamlit run ./streamlit/app.py --server.port=8080