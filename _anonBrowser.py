import mechanize
import cookielib
import random

class anonBrowser(mechanize.Browser):
	def __init__(self, proxies = [], user_agents = []):
		mechanize.Browser.__init__(self)
		self.set_handle_robots(False)
		self.proxies = proxies
		self.user_agents = user_agents + ['Mozilla/4.0 ','FireFox/6.01','ExactSearch','Nokia7110/1.0']
		self.cookie_jar = cookielib.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)
		self.anonymize()
	def clear_cookies(self):
		self.cookie_jar = cookielib_LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)
	def change_user_agent(self):
		index = random.randrange(0, len(self.user_agents))
		self.addheaders = [('User-agent', (self.user_agents[index]))]
	def change_proxy(self):
		if self.proxies:
			index = random.randrange(0, len(self.proxies))
			self.set_proxies({'http': self.proxies[index]})
	def anonymize(self, sleep = False):
		self.clear_cookies()
		self.change_user_agent()
		self.change_proxy()
		if sleep:
			tim.sleep(2)  # seconds between checking next site

#figuring out how to use the anonBrowser****************************
myopener = anonBrowser()
page = myopener.open('http://www.lens.org/lens/patent/US_6300863_B1/regulatory')  #also try https://www.google.com/patents/US5816918
info = page.read()
print info
