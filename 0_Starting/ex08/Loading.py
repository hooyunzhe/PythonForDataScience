import time as Time


def generate_display(current: int, total: int, elapsed: float) -> str:
    """
    A function that calculates the necessary variables for display

    Arguments:
        current (int): the current item
        total (int): the total amount of items
        elapsed (float): the elapsed time in milliseconds

    Returns:
        the loading bar as a formatted string

    """

    # hardcoded width of the terminal
    terminal_width = 198

    # rounded percentage of the progress
    percentage = current * 100 // total

    # items per second on average
    average_speed = current / elapsed if elapsed else 0

    # estimated time needed for the remaining items
    remaining_time = (total - current) // average_speed if elapsed else 0

    # format strings according to the original tqdm
    percentage_string = f"{percentage}%|"
    progress_count_string = f"| {current}/{total} "
    elapsed_string = Time.strftime('%M:%S', Time.gmtime(elapsed))
    remaining_string = (Time.strftime('%M:%S', Time.gmtime(remaining_time))
                        if elapsed else "?")
    time_progress_string = f"{elapsed_string}<{remaining_string}"
    speed_string = f"{average_speed:.2f}it/s" if elapsed else "?it/s"
    time_string = f"[{time_progress_string}, {speed_string}]"
    progress_string = progress_count_string + time_string

    # the amount of characters left for the bar and padding
    bar_width = terminal_width - len(percentage_string) - len(progress_string)
    bar_count = bar_width * percentage // 100
    bar_string = "█" * bar_count
    padding_string = " " * (bar_width - bar_count)

    # the final string
    return percentage_string + bar_string + padding_string + progress_string


def ft_tqdm(lst: range) -> None:
    """
    A function that displays a loading bar
    that contains the following info:
        - current progress in percentage
        - current items over total items
        - elapsed time and remaining time (estimated)
        - average speed (items per second)

    Arguments:
        a range that contains the items

    Yields:
        current item
    """

    # the amount of items
    total = len(lst)

    # the current time
    start_time = Time.time()

    # the default bar at the start
    print(generate_display(0, total, 0), end='\r', flush=True)

    # update the bar for each item
    for index, item in enumerate(lst):
        yield item
        display = generate_display(index + 1, total, Time.time() - start_time)
        print(display, end='\r', flush=True)
