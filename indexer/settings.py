import os

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_USERNAME = os.getenv("REDIS_USERNAME")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
EMBEDDINGS_ENDPOINT = os.getenv("EMBEDDINGS_ENDPOINT")
S3_API_HOST = os.getenv("S3_API_HOST")
S3_API_PORT = os.getenv("S3_API_PORT")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")
