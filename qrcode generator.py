import qrcode
data="https://www.flipkart.com/"  # Data for the QR code
 
# Generate QR code
qr= qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
    )
qr.add_data("https://www.flipkart.com/")
qr.make(fit=True)

# Create an image of the QR code
img= qr.make_image(fill_colour="black",back_colour="white")

# Save the image or display it
img.save("qrcode.png")
img.show()

