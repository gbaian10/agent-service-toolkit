from enum import Enum


class Provider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    GROQ = "groq"


class OpenAIModelName(str, Enum):
    """https://platform.openai.com/docs/models/gpt-4o"""

    GPT4O_MINI = "gpt-4o-mini"
    GPT4O = "gpt-4o"


class AnthropicModelName(str, Enum):
    """https://docs.anthropic.com/en/docs/about-claude/models#model-names"""

    HAIKU3 = "claude-3-haiku-20240307"  # TODO 3.5 coming soon
    SONNET35 = "claude-3-5-sonnet-20241022"


class GoogleModelName(str, Enum):
    GEMINI15_FLASH = "gemini-1.5-flash"


class GroqModelName(str, Enum):
    """https://console.groq.com/docs/models"""

    LLAMA31_70B = "llama-3.1-70b-versatile"
    LLAMA31_8B = "llama-3.1-8b-instant"

    LlAMA_GUARD_3_8B = "llama-guard-3-8b"
