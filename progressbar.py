# progressbar.py
# 显示进度条

import sys


def print_progress_bar(progress):
    """
    Call in a loop to create terminal progress bar with color.
    @param:
        progress - Required : the progress as a fraction between 0 and 1 (Float)
    """
    # Set the length of the progress bar
    length = 50
    # Convert progress to percentage and then to an integer for the bar length
    percentage_int = int(progress * length)
    # Create the progress bar string
    green_bar = "\033[92m" + "-" * percentage_int + "\033[0m"
    red_bar = "\033[91m" + "-" * (length - percentage_int) + "\033[0m"
    # Create the full progress bar with start and end symbols
    if progress == 1.0:
        bar = "\033[92m|" + green_bar + "\033[92m|"  # Both ends green for 100%
    else:
        bar = "\033[92m|" + green_bar + red_bar + "\033[91m|"
    # Create the percentage string
    percent = f"{progress:.2%}"
    # Write the progress bar to stdout with light blue color for percentage
    sys.stdout.write(f"\r{bar} \033[94m{percent}\033[0m")
    # Flush stdout to ensure the output is printed immediately
    sys.stdout.flush()
    # If progress is 100%, print "Complete!" and a newline
    if progress == 1.0:
        print(f"\r{bar} \033[92m{percent}\033[0m")
        print("Complete!")
