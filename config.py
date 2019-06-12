import platform


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

total_parsed = 0
platform_type = platform.system()
if platform_type == 'Windows':
    os_type = platform_type
else:
    os_type = 'Linux'

#PhantomJS config
user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)
#
# user_agent = (
#     "Mozilla/5.0 (Linux; Android 4.4.4; SM-G900F Build/KTU84Q) " +
#     "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36"
# )


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent
service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any']



