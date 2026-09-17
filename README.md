1. 安裝依賴庫
請開啟命令提示字元 (CMD) 或 Terminal 執行以下指令安裝必要套件：

Bash
python -m pip install pyautogui opencv-python pillow

💡 提示：若直接執行 pip 出現 'pip' 不是内部或外部命令，請務必使用 python -m pip install ... 的寫法。

🚀 使用方法 (Usage)
開啟並將 ChatGPT 桌面版 放置於螢幕可見區域。

在專案目錄下執行腳本：

Bash
python auto_retry_chatgpt.py
腳本將會在背景持續偵測螢幕畫面，當畫面出現容量限制重試按鈕時，自動為您點擊重試並列印日誌。

⚙️ 核心程式碼 (Code Overview)
auto_retry_chatgpt.py 內容如下：

Python
import time
import pyautogui

# 設定檢測間隔（秒）
CHECK_INTERVAL = 3

print("ChatGPT 桌面版自動重試服務已啟動...")

while True:
    try:
        # 檢測中文版 "重试" 按鈕
        button_location_zh = pyautogui.locateOnScreen('retry_button_zh.png', confidence=0.8)
        if button_location_zh is not None:
            button_point_zh = pyautogui.center(button_location_zh)
            pyautogui.click(button_point_zh)
            print(f"[{time.strftime('%H:%M:%S')}] 檢測到容量受限，已自動點擊重試！")
            time.sleep(10) # 點擊後冷卻 10 秒

        # 檢測英文版 "Retry" 按鈕
        button_location_en = pyautogui.locateOnScreen('retry_button_en.png', confidence=0.8)
        if button_location_en is not None:
            button_point_en = pyautogui.center(button_location_en)
            pyautogui.click(button_point_en)
            print(f"[{time.strftime('%H:%M:%S')}] Capacity limitation detected; Retry has been clicked automatically!")
            time.sleep(10) # 點擊後冷卻 10 秒
    except Exception as e:
        pass
    
    time.sleep(CHECK_INTERVAL)
💡 常見問題與調優 (Troubleshooting)
1. 偵測不到按鈕怎麼辦？
由於不同螢幕解析度、縮放比例（如 125%、150% DPI 縮放）或主題色調可能有所差異，若無法自動觸發：

請使用螢幕截圖工具（Windows 快捷鍵 Win + Shift + S 或 Mac Cmd + Shift + 4）。

截取您畫面上顯示的「重試 / Retry」按鈕（建議僅截取按鈕文字本體）。

覆蓋專案目錄下的 retry_button_zh.png 或 retry_button_en.png 即可。
