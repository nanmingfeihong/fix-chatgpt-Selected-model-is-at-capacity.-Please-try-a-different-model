🛠️ 環境需求與安裝 (Installation)
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
