# Base image with Python installed
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install necessary Python packages
RUN pip install qrcode[pil]

# Environment variables with default values
ENV QR_DATA_URL=https://github.com/kaw393939
ENV QR_CODE_DIR=/app/qr_codes
ENV QR_CODE_FILENAME=github_qr.png
ENV FILL_COLOR=black
ENV BACK_COLOR=white

# Run the QR generator script
CMD ["python", "generate_qr.py"]

