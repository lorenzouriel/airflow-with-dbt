FROM quay.io/astronomer/astro-runtime:12.2.0
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
