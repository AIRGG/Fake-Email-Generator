import string, random

banyak = 100
st = string.ascii_letters
nm = string.digits
merge = f"{st}{nm}"

lstmerge = list(merge)
email = ["gmail", "outlook", "yahoo", "hotmail", "protonmail", "aol", "mail"]
domain = ["com", "co.ac","co.ad","co.ae","co.af","co.ag","co.ai","co.al","co.am","co.ao","co.aq","co.ar","co.as","co.at","co.au","co.aw","co.ax","co.az","co.ba","co.bb","co.bd","co.be","co.bf","co.bg","co.бг","co.bh","co.bi","co.bj","co.bm","co.bn","co.bo","co.bq","co.br","co.bs","co.bt","co.bw","co.by","co.bz","co.st","co.ca","co.cc","co.cd","co.cf","co.cg","co.ch","co.ci","co.ck","co.cl","co.cm","co.cn","co.co","co.cr","co.cu","co.cv","co.cw","co.cx","co.cy","co.cz","co.de","co.dj","co.dk","co.dm","co.do","co.dz","co.ec","co.ee","co.eg","co.er","co.es","co.et","co.eu","co.eus","co.fi","co.fj","co.fk","co.fm","co.fo","co.fr","co.ga","co.gd","co.ge","co.gf","co.gg","co.gh","co.gi","co.gl","co.gal","co.gm","co.gn","co.gp","co.gq","co.gr","co.gs","co.gt","co.gu","co.gw","co.gy","co.hk","co.hm","co.hn","co.hr","co.ht","co.hu","co.id","co.ie","co.il","co.im","co.in","co.io","co.iq","co.ir","co.is","co.it","co.je","co.jm","co.jo","co.jp","co.ke","co.kg","co.kh","co.ki","co.km","co.kn","co.kp","co.kr","co.kw","co.ky","co.kz","co.la","co.lb","co.lc","co.li","co.lk","co.lr","co.ls","co.lt","co.lu","co.lv","co.ly","co.ma","co.mc","co.md","co.me","co.mg","co.mh","co.mk","co.ml","co.mm","co.mn","co.mn","co.mo","co.mp","co.mq","co.mr","co.ms","co.mt","co.mu","co.mv","co.mw","co.mx","co.my","co.mz","co.na","co.nc","co.ne","co.nf","co.ng","co.ni","co.nl","co.no","co.np","co.nr","co.nu","co.nz","co.om","co.pa","co.pe","co.pf","co.pg","co.ph","co.pk","co.pl","co.pm","co.pn","co.pr","co.ps","co.pt","co.pw","co.py","co.qa","co.re","co.ro","co.rs","co.срб","co.ru","co.su","co.рф","co.rw","co.sa","co.sb","co.sc","co.sd","co.se","co.sg","co.sh","co.si","co.sk","co.sl","co.sm","co.sn","co.so","co.sr","co.ss","co.st","co.bz","co.su","co.sv","co.sx","co.sy","co.sz","co.tc","co.td","co.tf","co.tg","co.th","co.tj","co.tk","co.tl","co.tp","co.tm","co.tn","co.to","co.tr","co.tt","co.tv","co.tw","co.tz","co.ua","co.ug","co.uk","co.us","co.gov","co.uy","co.uz","co.va","co.vc","co.ve","co.vg","co.vi","co.vn","co.vu","co.wf","co.ws","co.ye","co.yt","co.za","co.zm","co.zw"]

lst = []
for x in range(banyak):
	a = ''.join([random.choice(lstmerge) for x in range(random.randint(15, 20))])
	b = f"{a}@{random.choice(email)}.{random.choice(domain)}"
	try:
		int(b[0])
		b = f"{random.choice(st)}{b}"
	except Exception as e:
		pass
	finally:	
		pw = ''.join([random.choice(lstmerge) for x in range(random.randint(8, 15))])
		print(b, "|", pw)
		lst.append(f"{b} | {pw}\n")

with open("fakeEmail.txt", "w", encoding="utf-8") as f:
	for x in lst:
		f.write(x)