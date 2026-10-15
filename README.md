# DS102 - Thực hành 1

## Nội dung
- **Câu 1 – Newton-Raphson:** Tìm điểm dừng của hàm số bằng phương pháp Newton-Raphson.
- **Câu 2 – Thu thập dữ liệu:** Thu thập dữ liệu dân số Việt Nam từ World Bank API và lưu vào file CSV.

## Cấu trúc thư mục
```text
newton-raphson-web-scraping/
├── question_1_newton_raphson/
│   └── DS102.R11.CNVN_TH1.1.py
├── question_2_web_scraping/
│   ├── DS102.R11.CNVN_TH1.2.py
│   └── population_vietnam.csv
├── README.md
└── requirements.txt
```

## Cài đặt thư viện
```bash
py -m pip install -r requirements.txt
```

## Chạy chương trình
```bash
py question_1_newton_raphson/DS102.R11.CNVN_TH1.1.py
py question_2_web_scraping/DS102.R11.CNVN_TH1.2.py
```

## Nguồn dữ liệu
World Bank Open Data – Population, total:  
https://data.worldbank.org/indicator/SP.POP.TOTL?locations=VN