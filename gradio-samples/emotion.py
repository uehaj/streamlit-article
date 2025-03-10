import gradio as gr
from transformers import pipeline

# 1) Hugging Faceのパイプラインを利用し、感情分析モデルをロード
sentiment_pipeline = pipeline("sentiment-analysis")

# 2) Gradioで呼び出す関数を定義
def analyze_sentiment(text):
    """
    入力テキストに対して感情分析を行い、結果を文字列で返す。
    """
    # モデルの結果は List[dict] 形式
    #   例: [{"label": "POSITIVE", "score": 0.99}, ...]
    results = sentiment_pipeline(text)
    # 単純に最初の結果を文字列化する
    label = results[0]["label"]
    score = results[0]["score"]
    return f"Label: {label}, Score: {score:.3f}"

# 3) Gradioインターフェースを定義
iface = gr.Interface(
    fn=analyze_sentiment,        # 実行する関数
    inputs="text",               # ユーザーからの入力はテキスト
    outputs="text",              # 出力はテキストで表示
    title="Hugging Face Sentiment Demo",
    description="入力した文章の感情を推定します。"
)

# 4) 起動
if __name__ == "__main__":
    iface.launch()

