from pyicloud import PyiCloudService
import os


# 使用你的 Apple ID 和应用专用密码,认证到 iCloud


def authenticate_icloud(icloud_emial, icloud_password):
    api = PyiCloudService(icloud_emial, icloud_password)
    return api
        
 


def download_fit(icloud_emial, icloud_password):
    api = authenticate_icloud(icloud_emial, icloud_password)

    try:
        # 使用 api.drive 来访问 iCloud Drive
        files = api.drive['Blackbird'].dir()
        for f in files:
            if f.endswith(".fit"):
                base_name = os.path.splitext(f)[0]  
                fit_out_path = os.path.join("FIT_OUT", f)
                lock_file_path = os.path.join("FIT_OUT", f"{base_name}.fit.lock")
                if not os.path.exists(fit_out_path) and not os.path.exists(lock_file_path): 
                    download = api.drive['Blackbird'][f].open(stream=True)
                    with open(fit_out_path, 'wb') as opened_file:
                        opened_file.write(download.raw.read())


    except KeyError as e:
        print("发生错误：", e)
    except Exception as e:
        print("其他错误：", e)
    


    

