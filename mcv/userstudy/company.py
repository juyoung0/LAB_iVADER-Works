companyName = ["AMC","Audi","BMW","Buick","Cadillac","Chevrolet","Chevy","Chrysler","Citroen","Datsun","Dodge","Fiat","Ford","Hi","Honda","Mazda","Mercedes-Benz","Mercury","Nissan","Oldsmobile","Opel","Peugeot","Plymouth","Pontiac","Renault","Saab","Subaru","Toyota","Triumph","Volkswagen","Volvo"];

bar =470 / float(len(companyName)-1)
loc = 0
locs = companyName

for i in range(len(companyName)):
	locs[i] = round(loc,2)
	loc += bar

print locs
