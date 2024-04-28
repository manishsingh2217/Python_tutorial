import qrcode as qr  #  we can call qrcode as qr
img=qr.make("https://www.youtube.com/@mkvlogs2217")  # make("link where qr redirect")
img.save("MK_VLOG.png")  #variableNam.save("pic or qr name")