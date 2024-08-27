from mitmproxy import http
import config

# 拦截特定请求并返回自定义响应

def request(flow: http.HTTPFlow) -> None:
    print(f"->>>> {flow.request.pretty_url}")

    for mock in config.mock_config:
        if mock['url'] in flow.request.pretty_url:
            print(f"拦截请求{flow.request.pretty_url}")
            # 返回自定义的模拟数据
            flow.response = http.Response.make(
                status_code=mock['status_code'],
                content=mock['content'],
                headers=mock['headers']
            )

# mitmdump -s request_interceptor.py
