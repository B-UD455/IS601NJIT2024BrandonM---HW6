import qrcode
import os

# Get environment variables for QR customization
url = os.getenv('QR_DATA_URL', 'https://github.com/kaw393939')  # Use your GitHub homepage by default
fill_color = os.getenv('FILL_COLOR', 'black')
back_color = os.getenv('BACK_COLOR', 'white')
output_dir = os.getenv('QR_CODE_DIR', './qr_codes')
filename = os.getenv('QR_CODE_FILENAME', 'github_qr.png')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Create QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color=fill_color, back_color=back_color)

# Save QR code as PNG
output_path = os.path.join(output_dir, filename)
img.save(output_path)
print(f"QR code saved at {output_path}")

