FROM apache/airflow:2.8.0

ENV AIRFLOW_HOME=/opt/airflow
ENV DATA_DIR = /opt/airflow/data
ENV AIRFLOW_UID=50000
ENV AIRFLOW_GID=50000
ENV GOOGLE_APPLICATION_CREDENTIALS=${AIRFLOW_HOME}/config/google_credentials_ngu_a.json

ENV PYTHONPATH = $AIRFLOW_HOME/helper:$PYTHONPATH


USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        unzip \
        wget \
        vim \
        curl \
        python3-pip \
        python3-dev



RUN sudo apt-get install apt-transport-https ca-certificates gnupg 
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list 
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - 
RUN sudo apt-get update && sudo apt-get install google-cloud-cli 


# Create airflow group

# Add airflow user to sudoers
RUN usermod -aG sudo airflow

# Change password to airflow
RUN echo "airflow:airflow" | chpasswd 

# Grant sudo permissions to the airflow user
RUN echo "airflow ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Grant permissions to the airflow user
RUN chown -R airflow: ${AIRFLOW_HOME} 

# Create test folder /opt/airflow/tests and airflow.cfg file in /opt/airflow/airflow.cfg
RUN mkdir -p ${AIRFLOW_HOME}/tests
ADD airflow.cfg .
#RUN echo "[core]" >> /opt/airflow/airflow.cfg
#RUN echo "dags_folder = /opt/airflow/dags,/opt/airflow/helper" >> /opt/airflow/airflow.cfg


USER ${AIRFLOW_UID}
ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


WORKDIR ${AIRFLOW_HOME}

CMD ["webserver"]