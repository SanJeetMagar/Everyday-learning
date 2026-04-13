from fastapi import FastAPI, Request

app = FastAPI()
@app.post("/sms-status")
async def sms_status(request: Request):
    data = await request.form()
    
    print("📩 Webhook received!")
    print(f"SID: {data.get('MessageSid')}")
    print(f"Status: {data.get('MessageStatus')}")
    print(f"Error Code: {data.get('ErrorCode')}")
    print(f"Error Message: {data.get('ErrorMessage')}")
    
    return {"status": "received"}