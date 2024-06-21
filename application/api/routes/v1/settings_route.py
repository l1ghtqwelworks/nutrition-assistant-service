import logging

from fastapi import status
from fastapi.routing import APIRouter

from application.schemas.v1.answers_schema import AnswerResponseV1, AnswerV1

router = APIRouter()
logger = logging.getLogger(__name__)



@router.put(
    '/ask', response_description='Settings updated successfuly'
)
async def ask_question(prompt: str) -> AnswerResponseV1:
    return AnswerResponseV1(message='pp', data=AnswerV1(message=prompt))
