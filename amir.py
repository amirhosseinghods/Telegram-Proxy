import requests
import json
import telebot

bot_token = "Your_Bot_Token"
user_id = "User_id"

bot = telebot.TeleBot(bot_token)

def extract_and_send(link, user_id):
    try:
        response = requests.get(link)
        
        response.raise_for_status()
        
        json_data = response.json()
        
        extracted_data = []
        for i, item in enumerate(json_data):
                if i >= 50:
                    break
        for item in json_data:
            if "host" in item and "port" in item and "secret" in item:
                extracted_data.append({
                    "host": item["host"],
                    "port": item["port"],
                    "secret": item["secret"]
                })
        
        for data in extracted_data:
            url = f"https://t.me/proxy?server={data['host']}&port={data['port']}&secret={data['secret']}"
            bot.send_message(user_id, f"اطلاعات جدید: {url}")        

    except requests.exceptions.RequestException as e:
        print(f"خطا در درخواست: {e}")
    except json.JSONDecodeError as e:
        print(f"خطا در تبدیل به JSON: {e}")

json_link = "https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/mtproto.json"
extract_and_send(json_link, user_id)
bot.polling()
