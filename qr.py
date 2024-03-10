import qrcode
import image


# Get user input for the link
data = input("Enter the link: ")

# Create a QR code object
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5,
)

# Add the user input data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill="black", back_color="white")

# Save the QR code image
img.save("test.png")
