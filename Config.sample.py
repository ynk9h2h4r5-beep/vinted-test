# SMTP Settings for e-mail notification
smtp_username = ""
smtp_psw = ""
smtp_server = ""
smtp_toaddrs = ["User <example@example.com>"]

# Slack WebHook for notification
slack_webhook_url = ""

# Telegram Token and ChatID for notification
telegram_bot_token = "8376448352:AAHUweH-FOtF4QTENry8gDseBcFpdcLCQgw"
telegram_chat_id = "t.me/vinted_uk_bot"

# Vinted URL: change the TLD according to your country (.fr, .es, etc.)
vinted_url = "https://www.vinted.co.uk"

# Vinted queries for research
# "page", "per_page" and "order" you may not edit them
# "search_text" is the free search field, this field may be empty if you wish to search for the entire brand.
# "catalog_ids" is the category in which to eventually search, if the field is empty it will search in all categories. Vinted assigns a numeric ID to each category, e.g. 2996 is the ID for e-Book Reader
# "brand_ids" if you want to search by brand. Vinted assigns a numeric ID to each brand, e.g. 417 is the ID for Louis Vuitton
# "order" you can change it to relevance, newest_first, price_high_to_low, price_low_to_high

queries = [
    {
        'page': '1',
        'per_page': '96',
        'search_text': 'nike running',
        'catalog_ids': '',
        'brand_ids' : 'nike',
        'order': 'newest_first',
    },
    {
        'page': '1',
        'per_page': '96',
        'search_text': 'nike running division',
        'catalog_ids': '',
        'brand_ids' : '',
        'order': 'newest_first',
    },
    {
        'page': '1',
        'per_page': '96',
        'search_text': 'nike future fast',
        'catalog_ids': '',
        'brand_ids' : 'nike',
        'order': 'newest_first',
    },

]
