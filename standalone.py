from count import *
from insert_to_sheet import *

import datetime
import time

def fun_count():

    # ct stores current date
    ct = datetime.datetime.now().date()
    img_name = "overview_{}.png".format(ct) 

    # use adjust_areas function to visualize contours being picked up by code
    min_area = 10
    max_area = 100

    # run the following when NOT using Docker Container to finetune area values.
    # min_area, max_area = adjust_areas(img_name)
    # print(f"Optimal min_area: {min_area}, max_area: {max_area}")
    # print("Waiting 2 seconds ...")
    # time.sleep(2)


    final_count, _ = count_pink_markers(img_name, min_area, max_area)
    print(f"Final count of pink markers: {final_count}")
    insert_to_sheets(str(ct), str(final_count))

    print("Waiting 2 seconds ...")
    time.sleep(2)

    print("DONE")

