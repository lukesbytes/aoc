import os
import requests

import aoc.common.identity


def fetch_input(year, day):
    url_input = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = aoc.common.identity.get_cookies()
    p = requests.request("GET", url_input, cookies=cookies, verify=False)
    if p.status_code == 200:
        return p.text.strip()
    else:
        raise IOError("No data available (yet)")


def read_input(year, day, split=None):
    data_path = f"data/inputs/in_{year}_{day:02d}.dat"
    if not os.path.isfile(data_path):
        os.makedirs(os.path.split(data_path)[0], exist_ok=True)
        input_text = fetch_input(year, day)
        with open(data_path, "w") as f:
            f.write(input_text)
    else:
        with open(data_path) as f:
            input_text = f.read()

    return input_text if split is None else input_text.split(split)


if __name__ == "__main__":
    import sys
    m_year = int(sys.argv[1])
    m_day = int(sys.argv[2])
    text = read_input(m_year, m_day, split='\n')
    print(text)

