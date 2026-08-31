import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()
with open("asset_report.json", "r", encoding="utf-8") as f:
    asset_data = json.load(f)
    
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "user",
            "content": f"""
        请分析下面这个 UE5 资产。

        请从 Technical Artist 的角度：
        1. 分析资产结构
        2. 找出可能存在的问题
        3. 指出哪些问题可以从扫描数据直接确认
        4. 对无法确认的问题明确说“无法从当前扫描数据判断”
        5. 给出后续检查建议

        资产扫描结果：

        {json.dumps(asset_data, indent=2, ensure_ascii=False)}
        """
        }
    ]
)

print(response.choices[0].message.content)