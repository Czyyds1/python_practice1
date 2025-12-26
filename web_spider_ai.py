import requests
from bs4 import BeautifulSoup

def get_web_content(url,preview_length=1000):
    # 1. 打印调试信息：确认传入的网址
    print(f"=== 开始抓取网址：{url} ===")

    # 2. 配置请求头（模拟浏览器，避免被反爬）
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Referer": "https://www.baidu.com"
    }

    try:
        # 3. 发送请求（自动处理重定向，超时10秒）
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        # 检查请求是否成功（状态码200表示成功）
        response.raise_for_status()
        # 设置正确的编码（避免乱码）
        response.encoding = response.apparent_encoding

        # 4. 打印调试信息：确认响应状态和内容长度
        print(f"请求成功！状态码：{response.status_code}")
        print(f"网页原始内容长度：{len(response.text)} 字符")

        # 5. 解析网页（优化：提取所有可见文本，而非仅<p>标签）
        soup = BeautifulSoup(response.text, 'html.parser')
        # 去除脚本、样式等无关标签
        for script in soup(["script", "style"]):
            script.decompose()
        # 提取所有文本并清理空白
        full_text = soup.get_text(strip=True)

        # 6. 打印调试信息：确认提取的文本内容
        print(f"提取的文本长度：{len(full_text)} 字符")
        if len(full_text) > 0:
            if preview_length and len(full_text) > preview_length:
                print(f"提取的文本前{preview_length}字符：{full_text[:preview_length]}...")
            else:
                print(f"提取的完整文本：{full_text}")  # 预览全部文本
        else:
            print("警告：未提取到任何文本！")

        return full_text

    except requests.exceptions.RequestException as e:
        # 7. 详细打印异常信息（定位失败原因）
        error_msg = f"抓取失败！原因：{str(e)}"
        print(error_msg)
        return error_msg

# 测试调用（替换成你的短链接/目标网址）
if __name__ == "__main__":
    target_url = "https://baijiahao.baidu.com/s?id=1852551459715659189"  # 替换成你要抓取的短链接
    content = get_web_content(target_url,preview_length=1000)
    # 最终输出结果
    print("\n=== 最终结果 ===")
    print(content)