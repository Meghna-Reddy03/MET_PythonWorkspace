def add_vendor(id,name,**object):
    info ={
    'id ': id,
    'name':name,
}
    for key, value in info.items():
        info[key] = value
    return info,object

vendor = add_vendor(12344,'Priyam',c_rate = 1000,p_terms = 'cash on delivery', compliment = 'thankyou')

print(vendor)