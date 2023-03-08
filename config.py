from pydantic import BaseSettings


class DefaultSetting(BaseSettings):
    SECRET_KEY: str = "3787b2b3631f5e58b18cc7b9dfa5db08b3c8b2d2f1918172"
