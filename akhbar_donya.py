import requests
a = input('enter the country : ')

b = requests.get('https://api.codebazan.ir/khabar/?kind='+a)

b.json()
("{        crated by : @e_l_f__6_6_6"
      +b.json()+   
                   '''  } ''')
