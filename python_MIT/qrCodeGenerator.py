import pyqrcode

# String which represents the QR code 
s = "https://github.com/yadav-jitendra"

# Generate QR code 
url = pyqrcode.create(s)

# Create and save the svg file"
url.svg("mygithub.svg", scale=8)

# Create and save the png file"
url.png('mygithub.png', scale=6)
