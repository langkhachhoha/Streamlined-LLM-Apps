from pprint import pprint
import base64
from openai import OpenAI
from pydantic import BaseModel, Field
import json

BASE_URL = "https://mkp-api.fptcloud.com"
FPT_API_KEY = "sk-pkXO_SaUE_BIWGz3P-cTow"
MODEL_NAME = 'Llama-4-Scout-17B-16E'

client = OpenAI(
    api_key=f"{FPT_API_KEY}",
    base_url=BASE_URL
)

# Encode Image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_path = "/Users/apple/Desktop/LLM-apps/image.jpeg"

# Getting the Base64 string
base64_image = encode_image(image_path)


class ImageDescription(BaseModel):
    so_cccd: str = Field(description="Số căn cước công dân")
    ho_ten: str = Field(description="Họ và tên")
    ngay_sinh: str = Field(description="Ngày sinh")
    gioi_tinh: str = Field(description="Giới tính")
    quoc_tich: str = Field(description="Quốc tịch")
    que_quan: str = Field(description="Quê quán")
    noi_thuong_tru: str = Field(description="Nơi thường trú")


class ImageDescriptionEN(BaseModel):
    id_number: str = Field(description="Citizen Identity Number")
    full_name: str = Field(description="Full name")
    date_of_birth: str = Field(description="Date of birth")
    sex: str = Field(description="Sex")
    nationality: str = Field(description="Nationality")
    place_of_origin: str = Field(description="Place of origin")
    place_of_residence: str = Field(description="Place of residence")


extract = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": (
                        """Trích xuất thông tin từ hình ảnh. """
                    )
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        },
    ],
    model=MODEL_NAME,
    response_format={
        "type": "json_object",
        "schema": ImageDescriptionEN.model_json_schema(),
    },
)


output = json.loads(extract.choices[0].message.content)

# In ra với tiếng Việt hiển thị đúng
print("=" * 50)
print("THÔNG TIN TRÍCH XUẤT TỪ CCCD:")
print("=" * 50)
for key, value in output.items():
    print(f"{key}: {value}")

print("\n" + "=" * 50)
print("JSON FORMAT (UTF-8):")
print("=" * 50)
# Sử dụng ensure_ascii=False để hiển thị tiếng Việt
print(json.dumps(output, indent=2, ensure_ascii=False))


