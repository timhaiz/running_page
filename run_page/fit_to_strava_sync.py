import argparse
import os
import time
from icloud_update_to_fitout import download_fit

from strava_sync import run_strava_sync
from config import FIT_FOLDER
from stravalib.exc import ActivityUploadFailed, RateLimitTimeout
from utils import get_strava_last_time, make_strava_client, upload_file_to_strava


def get_to_generate_files(last_time):
    """
    Return two values: one dict for upload
    and one sorted list for next time upload.
    """
    file_names = os.listdir(FIT_FOLDER)
    fit_files = []
    for f in file_names:
        if f.endswith(".fit"):
            file_path = os.path.join(FIT_FOLDER, f)
            # Since .fit files need special handling, you might not need to parse them like .fit
            # You can directly append to the list for uploading
            fit_files.append(file_path)

    # Use modification time or any other criteria as needed
    fit_files_dict = {
        int(os.path.getmtime(f)): f
        for f in fit_files
        if int(os.path.getmtime(f)) > last_time
    }
    
    return sorted(list(fit_files_dict.keys())), fit_files_dict

if __name__ == "__main__":
    #从icloud下载fit文件
    download_fit()
    
    if not os.path.exists(FIT_FOLDER):
        os.mkdir(FIT_FOLDER)
    parser = argparse.ArgumentParser()
    parser.add_argument("client_id", help="strava client id")
    parser.add_argument("client_secret", help="strava client secret")
    parser.add_argument("strava_refresh_token", help="strava refresh token")

    parser.add_argument(
        "--all",
        dest="all",
        action="store_true",
        help="if upload to strava all without check last time",
    )
 
    options = parser.parse_args()
    print("Need to load all .fit files, maybe take some time")
    last_time = 0
    client = make_strava_client(
        options.client_id, options.client_secret, options.strava_refresh_token
    )
    
    if not options.all:
        last_time = get_strava_last_time(client, is_milliseconds=False)
    
    to_upload_time_list, to_upload_dict = get_to_generate_files(last_time)
    index = 1
    print(f"{len(to_upload_time_list)} .fit files are going to upload")
    
    for i in to_upload_time_list:
        fit_file = to_upload_dict.get(i)
        try:
            upload_file_to_strava(client, fit_file, "fit")
            



            
        except RateLimitTimeout as e:
            timeout = e.timeout
            print(f"Strava API Rate Limit Timeout. Retry in {timeout} seconds\n")
            time.sleep(timeout)
            # Try previous upload again
            upload_file_to_strava(client, fit_file, "fit")


        except ActivityUploadFailed as e:
            print(f"Upload failed with error: {str(e)}")
        
        # Spider rule
        time.sleep(1)


    time.sleep(10)
    run_strava_sync(
        options.client_id, options.client_secret, options.strava_refresh_token
    )
