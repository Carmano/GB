names = ['Тумен', "Салам", "Вика"]
sts = [1500, 1500, 1500]
prs = ['0%', '10.5%', '10.5%']
my_dict = {name: st * float(pr.replace('%', '')) for name, st, pr in zip(names, sts, prs)}

for key, value in my_dict.items():
    print(key, value)
