from pyicloud import PyiCloudService
import os


# 使用你的 Apple ID 和应用专用密码,认证到 iCloud
email = os.environ['ICLOUD_EMAIL']
password = os.environ['ICLOUD_PASSWORD']

def download_fit():
    api = PyiCloudService(email, password)
    try:
        # 使用 api.drive 来访问 iCloud Drive
        files = api.drive['Blackbird'].dir()
        for f in files:
            if f.endswith(".fit"):
                base_name = os.path.splitext(os.path.basename(f))[0]
                fit_out_path = os.path.join("FIT_OUT", os.path.basename(f))
                lock_file_path = os.path.join("FIT_OUT", f"{base_name}.fit.lock")
                print('f':f,'fit_out_path':fit_out_path,'lock_file_path':lock_file_path)
                if not os.path.exists(fit_out_path) and not os.path.exists(lock_file_path):
                    download = api.drive['Blackbird'][f].open(stream=True)
                    with open(fit_out_path, 'wb') as opened_file:
                        opened_file.write(download.raw.read())
    except KeyError as e:
        print("发生错误：", e)
    except Exception as e:
        print("其他错误：", e)
    


    





