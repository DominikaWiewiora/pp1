products=['shoes', 'underwear', 'jacket']
washing_product=input('Washing product: ')
rinse_choice=input('Rinse: ')
if rinse_choice=='True':
    rinse=True
else:
    rinse=False
spin_choice=input('Spin: ')
if spin_choice=='True':
    spin=True
else:
    spin=False
time=0
if washing_product=='underwear':
    time+=70
if washing_product=='jacket':
    time+=40
if washing_product=='shoes':
    time+=20
if rinse==True:
    time+=15
if spin==True:
    time+=9
print(f'Total washing time: {time} minutes')