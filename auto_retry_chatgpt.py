import time
import pyautogui

# 設定檢測間隔（秒）
CHECK_INTERVAL = 3

print("ChatGPT 桌面版自動重試服務已啟動...")

while True:
    try:
        # 方法 A：尋找 ChatGPT 桌面版上的 "Try again" 或 "Retry" 按鈕
        # 需先擷取 Try again 按鈕的局部截圖存為 retry_button.png 置於同目錄
        button_location_zh = pyautogui.locateOnScreen('retry_button_zh.png', confidence=0.8)
        
        if button_location_zh is not None:
            button_point_zh = pyautogui.center(button_location_zh)
            pyautogui.click(button_point_zh)
            print(f"[{time.strftime('%H:%M:%S')}] 檢測到容量受限，已自動點擊重試！")
            time.sleep(10) # 點擊後冷卻 10 秒

        button_location_en = pyautogui.locateOnScreen('retry_button_en.png', confidence=0.8)
        
        if button_location_en is not None:
            button_point_en = pyautogui.center(button_location_en)
            pyautogui.click(button_point_en)
            print(f"[{time.strftime('%H:%M:%S')}] Capacity limitation detected; Retry has been clicked automatically!！")
            time.sleep(10) # 點擊後冷卻 10 秒
    except Exception as e:
        pass
    
    time.sleep(CHECK_INTERVAL)