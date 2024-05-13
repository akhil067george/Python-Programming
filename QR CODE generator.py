import pyqrcode
from pyqrcode import QRCode

s = "https://zycus.skillate.com/jobs?page=1&pageSize=10&department=&location=&title=&sortBy=&orderBy=ASC&minExp=0&maxExp=100&jobType=&workplaceType="
url = pyqrcode.create(s)
url.svg("Zycus.svg", scale=10)