import logging
logger = logging.getLogger(__name__)
from datetime import date
import os
from pydantic import BaseModel

from typing import Optional

from fastapi import FastAPI, HTTPException, Request, Response, status
import json
app = FastAPI() 


ENCODEING="utf-8"

# Class: lambda parameters
# field: codes (str), requirements_txt(str)

class LambdaCodes(BaseModel):
    codes: str
    requirements_txt: Optional[str] = None
    environment_variables: Optional[str]= None


@app.post("/v1/exec_aws_lambda/")
async def execute_lambda_code(lambdaCodes: LambdaCodes):
    logger.info('Got lambda parameters: %s', lambdaCodes)
    save_status=False
    return {"status": "ok"}

@app.get("/v1/health-check")
async def health_check():
    return {"status": "ok"}

