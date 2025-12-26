from openai import OpenAI

# 1. 配置你的 API Key
# 注意：如果是 DeepSeek，base_url 填 https://api.deepseek.com
# 如果是 OpenAI，则去掉 base_url 或填其官方地址
client = OpenAI(
    api_key="sk-57cc50534ac54e7da22763792d0f498a",
    base_url="https://api.deepseek.com"
)

print("--- 你的私人 AI 助手已上线 (输入 '退出' 结束对话) ---")

# 2. 开启循环，让程序不运行一次就结束
while True:
    user_input = input("我：")

    # 设置退出开关
    if user_input.lower() in ['退出', 'exit', 'quit']:
        print("助手：再见！祝你学习愉快！")
        break

    # 3. 调用 AI 接口
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": user_input},
            ]
        )

        # 4. 打印结果
        answer = response.choices[0].message.content
        print(f"助手：{answer}\n")

    except Exception as e:
        print(f"发生错误：{e}")