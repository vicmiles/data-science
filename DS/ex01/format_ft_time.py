
import time

def main():
    seconds = time.time()
    print(f"Seconds since January 1, 1970: {seconds:,.4f} "
        f"or {seconds:.2e} in scientific notation")
    local_time = time.localtime(seconds)
    date_text = time.strftime("%b %d %Y", local_time)

    print(date_text)

if __name__ == "__main__":
    main()
