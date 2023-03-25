FROM python:3.10

COPY . .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "src/__main__.py", "backend"]
