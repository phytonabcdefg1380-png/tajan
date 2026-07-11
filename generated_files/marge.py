### This is so that you can add the items you want to the database.

# You need to create a file called new_intents.json and then put all the data you want in it with the same structure as the original dataset.
# Remember to change the name of the original dataset from intents.json to intents_o.json


import json
import os
import pandas as pd 

def merge_intent_files(original_file, new_file, output_file="intents.json"):
    if not os.path.exists(new_file):
        print(f"❌ فایل {new_file} وجود ندارد!")
        return

    if os.path.getsize(new_file) == 0:
        print(f"❌ فایل {new_file} خالی است!")
        return

    try:
        with open(original_file, 'r', encoding='utf-8-sig') as f:
            original_data = json.load(f)
    except Exception as e:
        print(f"❌ خطا در فایل اصلی: {e}")
        return

    try:
        with open(new_file, 'r', encoding='utf-8-sig') as f:
            new_content = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ خطای JSON در فایل جدید: {e}")
        return

    if isinstance(new_content, list):

        new_intents = new_content
        print("ℹ️ فایل جدید به صورت آرایه تشخیص داده شد.")
    elif isinstance(new_content, dict) and 'intents' in new_content:
        new_intents = new_content['intents']
        print("ℹ️ فایل جدید به صورت شیء با کلید intents تشخیص داده شد.")
    else:
        print("❌ فایل جدید نه آرایه است و نه شیء معتبر با کلید intents.")
        return

    existing_tags = {intent['tag'] for intent in original_data['intents']}
    added = 0
    skipped = []

    for intent in new_intents:
        if intent['tag'] not in existing_tags:
            original_data['intents'].append(intent)
            added += 1
            print(f"✅ افزوده شد: {intent['tag']}")
        else:
            skipped.append(intent['tag'])
            print(f"⚠️ تکرار: {intent['tag']}")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(original_data, f, ensure_ascii=False, indent=4)

    print(f"\n✅ خلاصه: {added} آیتم جدید اضافه شد. {len(skipped)} آیتم تکراری نادیده گرفته شد.")
    print(f"📁 ذخیره شد در: {output_file}")

if __name__ == "__main__":
    merge_intent_files("intents_o.json", "new_intents.json", "intents.json")
print("\n")
#___________________________________________________________________________________________________________
c,p=0,0
a = pd .read_json("intents.json")["intents"]
for i,v in enumerate(a):
    for b in v["patterns"]:
        p+=1
for o in a:
    for b in o["context"]:
        c+=1
print("n(pattern):",p)
print("n(context):",c)
print("n(tag):",i)
print("patterns / tags:",p/i)
print()

