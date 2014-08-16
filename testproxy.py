import mechanize
def testProxy(url, proxy):
  browser = mechanize.Browser()
  browser.set_proxies(proxy)
  page = browser.open(url)
  source_code = page.read()
  print source_code
url = 'http://ip.nefsc.noaa.gov/'
torGuardRussia = {'http':'31.192.111.189'}
testProxy(url, torGuardRussia)
