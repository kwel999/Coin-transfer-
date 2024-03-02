import k_amino
from tqdm import tqdm

client = k_amino.Client(randomAgent=True,randomDevice=True)

print("""  
         𝗖𝗛𝗔𝗧𝗥𝗢𝗢𝗠 𝗖𝗢𝗜𝗡 𝗧𝗥𝗔𝗡𝗦𝗙𝗘𝗥 𝒃𝒚 𝘒𝘞𝘌𝘓999

                  """)
email = ""
secret= ""
client.login(email= email,secret=secret)

balance = client.get_wallet_info().totalCoins
print(f"Total Coins : {balance}")



def chats():
    prefix =""
    link =  f"http://aminoapps.com/p/{prefix}"
    chat_link = client.get_from_link(link)
    print(link)
    chat_id = chat_link.objectId
    total =int(input("Amount to donate: "))
    count = 0
    try:
        client.join_community(comId = chat_link.comId)
    except:
        print("looks like community is lock , join the communuty manually with code")
    sub_client = k_amino.SubClient(comId=chat_link.comId,client=client)
    for i in tqdm(range(total // 500)):
        try:
            sub_client.tip_coins(coins= 500, chatId=chat_id)
            count += 500
        except Exception as e:
            print(e)
    print(f"total balance you sent : {count}")

chats()
