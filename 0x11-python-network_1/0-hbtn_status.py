# !/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
And must use the urllib package
"""


if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        result = response.read()
        print("Body response:")
        print(f"\t- type: {type(result)}")
        print(f"\t- content: {result}")
        print(f"\t- utf8 content: {result.decode('utf-8')}")
