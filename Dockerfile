FROM python:3.10.1-slim-buster

# Build the wheel
RUN pip install build && \
    python -m build --wheel

# Install the wheel and run tests
RUN pip install --no-cache-dir dist/*.whl pytest && \
    pytest


FROM python:3.10.1-slim-buster

COPY --from=0 /py-find/dist/py_find-*.whl ./
RUN pip install py_find-*.whl
