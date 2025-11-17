import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

notion = Client(auth=os.getenv("NOTION_API_KEY"))
parent_page_id = os.getenv("NOTION_PARENT_PAGE_ID")

def create_page(title: str, content: str):
    notion.pages.create(
        parent={"page_id": parent_page_id},
        properties={
            "title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            }
        },
        children=[
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text":
                                {
                                    "content": content
                                }
                        }
                    ]
                }
            }
        ]
    )

if __name__ == "__main__":
    create_page("Sample Page Title", "This is the content of the sample page.")
    print("Page created successfully.")