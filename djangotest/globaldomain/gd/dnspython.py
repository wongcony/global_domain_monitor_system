import dns.resolver
import thread
import threading
from time import sleep,time
import MySQLdb
import datetime
#from models import resultdb
domain=['www.google.com','www.baidu.com','www.youku.com','www.mi.com','www.facebook.com','www.twitter.com','www.youtube.com','www.bbc.com']
dnsip=['8.8.8.8','8.8.4.4','127.0.0.1']
class threads(threading.Thread):
	def __init__(self,domain):
		threading.Thread.__init__(self)
		self.domain=domain
	def run(self):
		for ip in dnsip:
			my_resolver=dns.resolver.Resolver()
			my_resolver.nameservers=[ip]
			beftime=datetime.datetime.now()
			answers=my_resolver.query(self.domain)
			aftertime=datetime.datetime.now()
			usetime=int(((aftertime-beftime).microseconds)/1000)
			for rdata in answers:
				locks=thread.allocate_lock()
				locks.acquire()
				r=str(rdata)
				if len(r)>15:
					r='CANNOT REACH.'
				id=None
				v=[id,beftime,ip,self.domain,r,usetime]
				con=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="globaldomaindb")
				cur=con.cursor()
				cur.execute('insert into gd_resultdb values (%s,%s,%s,%s,%s,%s)',v)
				cur.execute('commit')
				cur.close()
				con.close()
				locks.release()
if __name__=='__main__':
	for d in domain:
		th=threads(d)
		th.start()


