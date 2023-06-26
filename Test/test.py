import pandas as pd
import webbrowser
import pyautogui

data = pd.read_excel('KNX23.xlsx')

for index, row in data.iterrows():
    link = row['Upload your photograph']
    title = row['Name']

    try:  
        title = title.title().strip()
        id = link.split('=')[-1]
        converted_url = f"https://drive.google.com/u/0/uc?id={id}"
        webbrowser.open_new_tab(converted_url)

        # Wait for the page to load and then press Ctrl + S to save the image in the Downloads folder
        pyautogui.sleep(4)
        pyautogui.hotkey('ctrl', 's')
        pyautogui.sleep(2)
        pyautogui.typewrite(title)
        pyautogui.sleep(2)
        pyautogui.press('enter')

        # Close the tab
        pyautogui.sleep(2)
        pyautogui.hotkey('ctrl', 'w')
        print(f'Successfully downloaded and saved {title}.jpg. {index}/{len(data)}')

    except Exception as e:
        print(f'Error occurred while downloading {title}: {e}')

# Convert the excel file to json
# data.to_json('dat.json', orient='records')

# Read from json file
# json = pd.read_json('out.json')
# json = json.transpose()

# # JSON file has nums as key and {email, techLink, other} as value
# # Append techLink and other to the dataframe as new columns and save it to excel
# for index, row in json.iterrows():
#     email = row['email']
#     id = row['id']
#     data.loc[data['email'] == email, 'id'] = id

# data.to_excel('out.xlsx', index=False)

# remove rows with no id
# data = data[data['id'].notna()]
# data.to_excel('out2.xlsx', index=False)