import browser_cookie3
import csv


# Get all cookies from the browser (Chrome)
cookies = list(browser_cookie3.chrome())


# Export cookies to cookie.csv file
with open("cookie.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(cookies)


# Display message for user
print("Cookies have been exported to cookies.csv")


# Optional functionality to get cookie from specific domain
def get_cookies_from_domain(domain, cookie_name=''):

    Cookies = {}
    chrome_cookies = list(browser_cookie3.chrome())

    for cookie in chrome_cookies:

        if domain in cookie.domain:
            # print (cookie.name, cookie.domain,cookie.value)
            Cookies[cookie.name] = cookie.value

    if cookie_name != '':
        try:
            return cookies[cookie_name]  # return specified cookie
        except:
            return {}  # if exception raised return an empty dictionary
    else:
        return Cookies  # return all cookies or nothing


# cookies = get_cookies_from_domain("reddit", "")
# print(get_cookies_from_domain("reddit", ""))


'''
def clean_format():
    Cookies = {}
    chrome_cookies = list(browser_cookie3.chrome())

    for cookie in chrome_cookies:
        Cookies[cookie.name] = cookie.value

    return Cookies



with open("clean.txt", 'w') as file:
    for key, value in clean_format().items():
        file.write(f"{key}:{value},")
'''












