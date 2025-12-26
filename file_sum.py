import os
from openai import OpenAI

# 1. 配置 AI
client = OpenAI(api_key="sk-57cc50534ac54e7da22763792d0f498a", base_url="https://api.deepseek.com")

# 2. 指定要读取的文件夹路径
folder_path = "my_files"
output_file = "总结结果.txt"

print(f"开始处理文件夹：{folder_path}...")

# 3. 遍历文件夹里的每一个文件
with open(output_file, "w", encoding="utf-8") as f_out:
    for filename in os.listdir(folder_path):
        # 只处理 .txt 文件
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            # 读取文件内容
            with open(file_path, "r", encoding="utf-8") as f_in:
                content = f_in.read()

            print(f"正在分析：{filename}...")

            # 4. 调用 AI 进行总结
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是一个行政助手，请用一句话总结用户提供的文档内容。"},
                    {"role": "user", "content": content}
                ]
            )

            summary = response.choices[0].message.content

            # 5. 将结果写入新文件
            f_out.write(f"文件名: {filename}\n总结: {summary}\n{'-' * 30}\n")

print(f"全部处理完成！请查看：{output_file}")