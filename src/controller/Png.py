from PIL import Image
from PIL import PngImagePlugin

file_name = 'empty_img.png'

im = Image.open(file_name)

info = PngImagePlugin.PngInfo()
# info.add_text("TXT", "aaaa")
# info.add_text("ZIP", "aaa")
x = 'str'
x = str(x)
info.add_text("Binning", "qqq")
info.add_text('Bit Depth = 003', str(x))
info.add_text('CCD Gain = 004', 1)
info.add_text('CCD Temperature = 005', 1.5)
info.add_text('CCD SET TEMP = 006', (72, 72))
info.add_text('CCD Type = 007', str(x))
info.add_text('Exposure = 008', str(x))
info.add_text('Filter Description = 009', str(x))
info.add_text('Filter Label = 010', str(x))
info.add_text('Filter Position = 011', str(x))
info.add_text('Filter Wavelength = 012', str(x))
info.add_text('Filter Wheel Temperature = 013', str(x))
info.add_text('Image Type = 014', str(x))
info.add_text('Latitude = 015', str(x))
info.add_text('Latitude = 016', str(x))
info.add_text('Moon Elevation = 021', str(x))
info.add_text('Moon Phase = 022', str(x))
info.add_text('Readout Speed = 023', str(x))
info.add_text('Shutter CCD = 024', str(x))
info.add_text('Shutter Lenz 025', str(x))
info.add_text('Site ID 026', str(x))
info.add_text('Start Time = 027', str(x))
info.add_text('Sun Elevation = 028', str(x))
info.add_text('Version = 028', str(x))


im.save(file_name, "PNG", pnginfo=info)

info = Image.open(file_name)
print(info.info)
