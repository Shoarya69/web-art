from flask import request
def is_mobile():
    ua = request.user_agent.string.lower()
    # Basic mobile detection keywords
    return any(keyword in ua for keyword in ["iphone", "android", "mobile", "ipad"])