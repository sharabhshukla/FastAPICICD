from fastapi import FastAPI, status, Response


app = FastAPI()

@app.get("/")
def read_root():
    return Response(content="API Root, visit /docs for documentation related to the api",
                    status_code=status.HTTP_200_OK)

@app.get("/health-ping")
def health_ping():
    return Response(content="Ok",
                    status_code=status.HTTP_200_OK)



