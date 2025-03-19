from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str

# Load the model and tokenizer
model_name = "chrisdepallan/mbart-en-ml"
tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application!"}

@app.post("/translate")
def translate(request: TranslationRequest):
    try:
        # Tokenize the input text
        inputs = tokenizer(request.text, return_tensors="pt")

        # Generate translation
        translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["ml_IN"])
        translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)