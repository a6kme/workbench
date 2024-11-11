import pytest
import vcr  # type: ignore
from httpx import AsyncClient

from api.forge import app as forge_app
from api.settings import settings


def before_record_request(request):  # type: ignore
    """
    Filter the request before saving it to the cassette
    """
    # Remove the Authorization header from the request
    if "localhost" in request.host:  # type: ignore
        return None
    return request  # type: ignore


@pytest.mark.anyio
@vcr.use_cassette(  # type: ignore
    f"{settings.BASE_DIR}/tests/vcr_cassettes/test_user_creation.yaml",
    filter_headers=["apikey"],
    before_record_request=before_record_request,
)
async def test_user_creation(async_client: AsyncClient):
    """
    Need to define the test as async test since fastapi async client was complaining that the event
    loop is closed.
    """
    valid_auth_token = "eyJhbGciOiJIUzI1NiIsImtpZCI6IjVhYUpxR0F1L0EyRHAvU3giLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2V4aGdzb2t0YmR4Z2JjbHFleWxtLnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiI1ZjM0NzU5Yi1iZjhhLTRhNGYtODgwMS0wNGUyYzZiMzhiNDkiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzMxMDc0NTcxLCJpYXQiOjE3MzEwNzA5NzEsImVtYWlsIjoiYWJoaS5oYWt1bmFtYXRhdGFAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJnb29nbGUiLCJwcm92aWRlcnMiOlsiZ29vZ2xlIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NMVWxOQUF4X09UN3Uzd2tPSVl1VWM2dHZLbTd3UTM0OXRZQ2xqNm16TVdSU0VCSmgxUVJ3PXM5Ni1jIiwiZW1haWwiOiJhYmhpLmhha3VuYW1hdGF0YUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiQWJoaXNoZWsga3VtYXIiLCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYW1lIjoiQWJoaXNoZWsga3VtYXIiLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NMVWxOQUF4X09UN3Uzd2tPSVl1VWM2dHZLbTd3UTM0OXRZQ2xqNm16TVdSU0VCSmgxUVJ3PXM5Ni1jIiwicHJvdmlkZXJfaWQiOiIxMTE4NDQwMDI3MjQxNzExMjczMDkiLCJzdWIiOiIxMTE4NDQwMDI3MjQxNzExMjczMDkifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTczMDk5Njg1NX1dLCJzZXNzaW9uX2lkIjoiMTI0Njk5NDUtNDIzYy00N2U0LWExZDktNzQ0MWY0YTUzNzlkIiwiaXNfYW5vbnltb3VzIjpmYWxzZX0.esCxax9fJxX7Adg2BIESlP6gnFp1r17jSoL8oYjyeGU"
    invalid_auth_token = "eyJhbGciOiJIUzI1NiIsImtpZCI6IjVhYUpxR0F1L0EyRHAvU3giLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2V4aGdzb2t0YmR4Z2JjbHFleWxtLnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiI1ZjM0NzU5Yi1iZjhhLTRhNGYtODgwMS0wNGUyYzZiMzhiNDkiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzMxMDc0NTcxLCJpYXQiOjE3MzEwNzA5NzEsImVtYWlsIjoiYWJoaS5oYWt1bmFtYXRhdGFAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJnb29nbGUiLCJwcm92aWRlcnMiOlsiZ29vZ2xlIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NMVWxOQUF4X09UN3Uzd2tPSVl1VWM2dHZLbTd3UTM0OXRZQ2xqNm16TVdSU0VCSmgxUVJ3PXM5Ni1jIiwiZW1haWwiOiJhYmhpLmhha3VuYW1hdGF0YUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiQWJoaXNoZWsga3VtYXIiLCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYW1lIjoiQWJoaXNoZWsga3VtYXIiLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NMVWxOQUF4X09UN3Uzd2tPSVl1VWM2dHZLbTd3UTM0OXRZQ2xqNm16TVdSU0VCSmgxUVJ3PXM5Ni1jIiwicHJvdmlkZXJfaWQiOiIxMTE4NDQwMDI3MjQxNzExMjczMDkiLCJzdWIiOiIxMTE4NDQwMDI3MjQxNzExMjczMDkifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTczMDk5Njg1NX1dLCJzZXNzaW9uX2lkIjoiMTI0Njk5NDUtNDIzYy00N2U0LWExZDktNzQ0MWY0YTUzNzlkIiwiaXNfYW5vbnltb3VzIjpmYWxzZX0.esDxax9fJxX7Adg2BIESlP6gnFp1r17jSoL8oYjyeGU"
    federated_user_id = "5f34759b-bf8a-4a4f-8801-04e2c6b38b49"

    # ensure user does not exist
    user = forge_app.DATABASE.get_user(federated_user_id=federated_user_id)

    assert user is None

    # try to get the user profile. The user must get created
    response = await async_client.get(
        "/api/v1/user/profile/", headers={"Authorization": f"Bearer {valid_auth_token}"}
    )
    assert response.status_code == 200

    user = forge_app.DATABASE.get_user(federated_user_id=federated_user_id)

    # the user must exist now
    assert user is not None

    # hit the same url again just to be sure the user is not created again
    response = await async_client.get(
        "/api/v1/user/profile/", headers={"Authorization": f"Bearer {valid_auth_token}"}
    )

    assert response.status_code == 200

    # hit one request with invalid token
    response = await async_client.get(
        "/api/v1/user/profile/",
        headers={"Authorization": f"Bearer {invalid_auth_token}"},
    )

    assert response.status_code == 401
    assert response.json() == {"detail": "bad authentication token"}
