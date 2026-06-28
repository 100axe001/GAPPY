FROM python:3.11-slim

WORKDIR /workspace

# Copy the SDK first so it can be installed as a local package dependency
COPY lemma-platform/lemma-python /workspace/lemma-platform/lemma-python
COPY app/requirements.txt /workspace/app/requirements.txt

# Install dependencies including the local SDK
RUN pip install --no-cache-dir -r /workspace/app/requirements.txt

# Copy the remaining application files
COPY app /workspace/app

WORKDIR /workspace/app

EXPOSE 8080

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]
