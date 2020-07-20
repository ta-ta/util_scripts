# lambda_template

### スクリプトによる単体実行
```
python lambda_function.py
```

### AWS Lambda による実行
```
cd lambda_template

# lambda 用のバイナリを取得
docker-compose up --build

# アップロード用zip 作成
rm lambda_src.zip
zip -r lambda_src.zip ./*
```
