from notion_client import Client
import os

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DB_ID")
notion = Client(auth=NOTION_TOKEN)

data = [
    {
        "資產類別": "核心成長股 (NVDA, AAPL, PLTR, GOOG)",
        "保守型配置 (%)": 40,
        "進攻型配置 (%)": 55,
        "切換建議說明": "持有或定期加碼，視VIX與美元指數調整"
    },
    {
        "資產類別": "高股息與REIT (O, SCHD, VYM)",
        "保守型配置 (%)": 25,
        "進攻型配置 (%)": 15,
        "切換建議說明": "穩定收益來源，適合防禦市場波動時加碼"
    },
    {
        "資產類別": "美元短債/現金 (BIL, SHY)",
        "保守型配置 (%)": 20,
        "進攻型配置 (%)": 10,
        "切換建議說明": "市場不穩時調高比重，作為流動性備援"
    },
    {
        "資產類別": "避險型 ETF (QQQH)",
        "保守型配置 (%)": 10,
        "進攻型配置 (%)": 5,
        "切換建議說明": "若台幣升值趨勢強，可加強避險比例"
    },
    {
        "資產類別": "高波動成長股 (TSLA)",
        "保守型配置 (%)": 3,
        "進攻型配置 (%)": 10,
        "切換建議說明": "若科技與成長股走勢明確，可加重配置"
    },
    {
        "資產類別": "槓桿與主題型 (SOXL, TMF)",
        "保守型配置 (%)": 2,
        "進攻型配置 (%)": 5,
        "切換建議說明": "僅保留少量波段倉位，技術面確認再操作"
    },
]

for row in data:
    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "資產類別": {"title": [{"text": {"content": row["資產類別"]}}]},
            "保守型配置 (%)": {"number": row["保守型配置 (%)"]},
            "進攻型配置 (%)": {"number": row["進攻型配置 (%)"]},
            "切換建議說明": {"rich_text": [{"text": {"content": row["切換建議說明"]}}]}
        }
    )
print("✅ Notion 更新成功")
