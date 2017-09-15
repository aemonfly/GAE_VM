# 前置準備
 - 先利用Compute engine建立一個Virtual Machine Instance
 - 啟用Compute engine API 
# 使用方式
 - 開啟google cloud shell
 - 建立資料夾
   > mkdir src
 - 切換至剛剛建立的資料夾
   > cd src
 - 下載本專案
   > git clone https://github.com/playerlove1/GAE_VM.git
 - 切換至本專案目錄
   >cd GAE_VM
 - 安裝相依套件
   > pip install -t lib -r requirements.txt
 - 修改main.py中的相關個人資訊  (替換成 要開啟之 VM的名稱 VM所在區域  VM所屬專案)
   > INSTANCE_NAME = 'your_instance_name'
   
   > INSTANCE_ZONE = 'your_instance_zone'
   
   > PROJECT = 'your_instance_project'
   
 - 部署到Google App Engine
   > gcloud app deploy app.yaml
# 測試
- 開啟VM
  >https://專案ID.appspot.com/vm/start
- 關閉VM
  >https://專案ID.appspot.com/vm/stop
  
(Note: 修改自 [app-engine-start-vm](https://github.com/fivunlm/app-engine-start-vm)
由於原先程式碼使用discover 取得的result 會超過 memcache 可以接受的範圍
ValueError: Values may not be more than 1000000 bytes in length; received 1014315 bytes
因此改為使用http.request的方式送出API請求)