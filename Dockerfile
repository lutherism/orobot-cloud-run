# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM us.gcr.io/robots-gateway/orobot-cloud-run/orobot-cloud-run:ce83659c46a4cc1c3956042918dbd0fb79c65e14
RUN apt-get update && apt-get install -y git make gcc clang clang-tools cmake python3 python3-pip libassimp-dev

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip3 install --no-cache-dir -r requirements.txt
#RUN mkdir /home/git; \
#    cd /home/git; \
#    git clone https://github.com/assimp/assimp.git -b master;

# RUN cd /home/git/assimp; \
#    cmake CMakeLists.txt -G 'Unix Makefiles'; \
#    make; \
#    make install;
#    ldconfig;

#RUN assimp help
#CMD rm -rf /home/out/* && mv /home/git/assimp/bin /home/out/bin && mv /home/git/assimp/lib /home/out/lib

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 src.main:app
