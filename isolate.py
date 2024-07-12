import time
 
from upload import * 
from standalone import *
from count import *

print("Running isolate.py")

# run function in standalone.py (and also count.py + insert_to_sheet.py) to update values in "count_dots" Google Sheet
fun_count()


time.sleep(1)
# run upload.py function to upload screenshot to Google Drive folder provided
fun_upload()

time.sleep(2)