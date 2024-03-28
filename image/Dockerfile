FROM public.ecr.aws/lambda/python:3.12

# Install dependencies
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install specified packages
RUN pip install -r requirements.txt

COPY src/* ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD ["brandforge_api.handler"]